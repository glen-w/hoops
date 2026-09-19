#!/usr/bin/env python3
"""
Fetch team logos from Wikimedia Commons.

Downloads logo files from Commons for teams in teams.csv,
verifies licenses, computes SHA-256 hashes, and updates logos.csv.

IMPORTANT: Skips fair-use logos to ensure redistribution compliance.

Usage:
    uv run python -m hoops_data.teams.fetch_logos
    uv run python -m hoops_data.teams.fetch_logos --dry-run
"""

import argparse
import hashlib
import json
import time
from pathlib import Path
from typing import Any
from urllib.parse import quote

import pandas as pd
import requests


# Fair-use / non-free licenses to skip
SKIP_LICENSES = {
    "fair use",
    "fairuse",
    "non-free",
    "nonfree",
    "copyright",
    "trademarked",
}


def get_commons_file_info(filename: str) -> dict[str, Any] | None:
    """
    Query Wikimedia Commons API for file metadata.
    
    Args:
        filename: Commons filename (e.g., "File:Lakers_logo.svg")
        
    Returns:
        File info dict with license, URL, mime type, or None if error
    """
    # Strip "File:" prefix if present
    if filename.startswith("File:"):
        filename = filename[5:]
    
    api_url = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": f"File:{filename}",
        "prop": "imageinfo",
        "iiprop": "url|mime|extmetadata",
    }
    
    try:
        response = requests.get(api_url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        pages = data.get("query", {}).get("pages", {})
        page = next(iter(pages.values()), {})
        
        if "imageinfo" not in page:
            return None
        
        imageinfo = page["imageinfo"][0]
        extmetadata = imageinfo.get("extmetadata", {})
        
        # Extract license
        license_short_name = extmetadata.get("LicenseShortName", {}).get("value", "")
        license_url = extmetadata.get("LicenseUrl", {}).get("value", "")
        attribution = extmetadata.get("Artist", {}).get("value", "")
        
        return {
            "url": imageinfo.get("url"),
            "mime": imageinfo.get("mime"),
            "license_short_name": license_short_name,
            "license_url": license_url,
            "attribution": attribution,
            "commons_url": imageinfo.get("descriptionurl"),
        }
        
    except Exception as e:
        print(f"  ✗ Error fetching Commons info for {filename}: {e}")
        return None


def is_free_license(license_name: str) -> bool:
    """
    Check if a license allows redistribution.
    
    Skips fair-use, non-free, and trademarked content.
    """
    license_lower = license_name.lower()
    
    # Check for skip patterns
    for skip in SKIP_LICENSES:
        if skip in license_lower:
            return False
    
    # Allow common free licenses
    free_patterns = ["cc", "public domain", "pd", "gpl", "lgpl", "apache", "mit"]
    return any(pattern in license_lower for pattern in free_patterns)


def download_file(url: str, output_path: Path) -> bool:
    """
    Download file from URL to local path.
    
    Returns True if successful, False otherwise.
    """
    try:
        response = requests.get(url, timeout=60, stream=True)
        response.raise_for_status()
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        return True
        
    except Exception as e:
        print(f"  ✗ Error downloading {url}: {e}")
        return False


def compute_file_hash(file_path: Path) -> str:
    """Compute SHA-256 hash of file."""
    sha256 = hashlib.sha256()
    
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    
    return sha256.hexdigest()


def extract_commons_filename_from_url(url: str) -> str | None:
    """Extract Commons filename from Wikidata logo URL."""
    # Example URL: http://commons.wikimedia.org/wiki/Special:FilePath/Lakers_logo.svg
    if "Special:FilePath/" in url:
        return url.split("Special:FilePath/")[-1]
    return None


def process_team_logo(
    team_row: dict[str, Any],
    raw_team_data: dict[str, Any],
    output_dir: Path,
    dry_run: bool = False,
) -> dict[str, Any] | None:
    """
    Process logo for a single team.
    
    Args:
        team_row: Row from teams.csv
        raw_team_data: Raw Wikidata data with logo URL
        output_dir: Base directory for logo storage
        dry_run: If True, don't download files
        
    Returns:
        Logo row dict or None if skipped
    """
    logo_url = raw_team_data.get("logo_url")
    if not logo_url:
        return None
    
    team_id = team_row["team_id"]
    
    # Extract filename from URL
    commons_filename = extract_commons_filename_from_url(logo_url)
    if not commons_filename:
        print(f"  ⚠ Could not extract Commons filename from {logo_url}")
        return None
    
    print(f"  Processing {commons_filename} for {team_id}...")
    
    # Fetch Commons metadata
    file_info = get_commons_file_info(commons_filename)
    if not file_info:
        return None
    
    # Check license
    license_name = file_info.get("license_short_name", "")
    if not is_free_license(license_name):
        print(f"    ⚠ Skipping fair-use/non-free license: {license_name}")
        return {
            "team_id": team_id,
            "logo_kind": "current",
            "year_start": None,
            "year_end": None,
            "commons_title": f"File:{commons_filename}",
            "commons_url": file_info.get("commons_url"),
            "local_path": None,
            "mime": None,
            "sha256": None,
            "license": "fair_use_skip",
            "attribution": file_info.get("attribution", ""),
            "as_of": pd.Timestamp.now().date().isoformat(),
            "confidence": "MEDIUM",
        }
    
    # Determine file extension from mime
    mime = file_info.get("mime", "")
    ext_map = {
        "image/svg+xml": ".svg",
        "image/png": ".png",
        "image/jpeg": ".jpg",
        "image/gif": ".gif",
    }
    ext = ext_map.get(mime, ".bin")
    
    # Download file
    team_dir = output_dir / team_id
    local_filename = f"current{ext}"
    local_path = team_dir / local_filename
    
    if not dry_run:
        download_url = file_info["url"]
        if download_file(download_url, local_path):
            # Compute hash
            sha256 = compute_file_hash(local_path)
            print(f"    ✓ Downloaded and hashed: {sha256[:16]}...")
        else:
            return None
    else:
        sha256 = "dry_run_placeholder"
        print(f"    (dry-run: would download to {local_path})")
    
    return {
        "team_id": team_id,
        "logo_kind": "current",
        "year_start": None,
        "year_end": None,
        "commons_title": f"File:{commons_filename}",
        "commons_url": file_info.get("commons_url"),
        "local_path": f"data/raw/logos/{team_id}/{local_filename}",
        "mime": mime,
        "sha256": sha256,
        "license": license_name,
        "attribution": file_info.get("attribution", ""),
        "as_of": pd.Timestamp.now().date().isoformat(),
        "confidence": "HIGH",
    }


def main():
    parser = argparse.ArgumentParser(
        description="Fetch team logos from Wikimedia Commons"
    )
    parser.add_argument(
        "--teams-csv",
        type=Path,
        default=Path("data/derived/teams/teams.csv"),
        help="Path to teams.csv",
    )
    parser.add_argument(
        "--raw-dir",
        type=Path,
        default=Path("data/raw/wikidata"),
        help="Directory with raw team JSONL",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/raw/logos"),
        help="Output directory for logo files",
    )
    parser.add_argument(
        "--logos-csv",
        type=Path,
        default=Path("data/derived/teams/logos.csv"),
        help="Path to logos.csv (output)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Don't download files, just check licenses",
    )
    parser.add_argument(
        "--rate-limit",
        type=float,
        default=1.0,
        help="Seconds to wait between API requests",
    )
    
    args = parser.parse_args()
    
    # Load teams
    if not args.teams_csv.exists():
        print(f"Error: {args.teams_csv} not found. Run normalize_teams.py first.")
        return 1
    
    teams_df = pd.read_csv(args.teams_csv)
    print(f"Loaded {len(teams_df)} teams from {args.teams_csv}")
    
    # Load raw data for logo URLs
    raw_teams_by_id = {}
    for league_id in teams_df["league_id"].unique():
        jsonl_path = args.raw_dir / f"{league_id}_teams.jsonl"
        if jsonl_path.exists():
            with open(jsonl_path) as f:
                for line in f:
                    if line.strip():
                        raw_team = json.loads(line)
                        team_qid = raw_team["team_qid"]
                        raw_teams_by_id[team_qid] = raw_team
    
    # Process logos
    logo_rows = []
    for _, team_row in teams_df.iterrows():
        team_qid = team_row["wikidata_qid"]
        raw_team = raw_teams_by_id.get(team_qid)
        
        if not raw_team:
            continue
        
        logo_row = process_team_logo(
            team_row.to_dict(),
            raw_team,
            args.output_dir,
            dry_run=args.dry_run,
        )
        
        if logo_row:
            logo_rows.append(logo_row)
        
        # Rate limiting
        time.sleep(args.rate_limit)
    
    # Write logos.csv
    logos_df = pd.DataFrame(logo_rows)
    logos_df.to_csv(args.logos_csv, index=False)
    print(f"\n✓ Wrote {len(logos_df)} logo entries to {args.logos_csv}")
    
    # Summary
    free_logos = len([r for r in logo_rows if r["license"] != "fair_use_skip"])
    skipped_logos = len([r for r in logo_rows if r["license"] == "fair_use_skip"])
    print(f"  {free_logos} free licenses downloaded")
    print(f"  {skipped_logos} fair-use logos skipped")
    
    return 0


if __name__ == "__main__":
    exit(main())
