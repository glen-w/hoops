#!/usr/bin/env python3
"""
Normalize raw Wikidata team data into derived CSVs.

Reads JSONL from data/raw/wikidata/ and writes structured
leagues.csv and teams.csv. Replaces only leagues marked active in
src/hoops_data/teams/leagues_seed.yaml. Other leagues already in those
files, including EuroLeague, are kept.

Usage:
    uv run python -m hoops_data.teams.normalize_teams
"""

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd
import yaml


def slugify(text: str) -> str:
    """Convert text to lowercase slug."""
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def extract_year_from_date(date_str: str | None) -> int | None:
    """Extract year from ISO date string."""
    if not date_str:
        return None
    try:
        return int(date_str.split("-")[0])
    except (ValueError, IndexError):
        return None


def hex_from_color_label(color_label: str | None) -> str | None:
    """
    Map color label to hex (basic mapping).
    
    Returns None for now - we won't invent colors.
    Real implementation would query Wikidata for P465 (hex color code).
    """
    # Don't invent colors - leave blank
    return None


def load_raw_teams(raw_dir: Path, league_id: str) -> list[dict[str, Any]]:
    """Load raw team data from JSONL."""
    jsonl_path = raw_dir / f"{league_id}_teams.jsonl"
    
    if not jsonl_path.exists():
        print(f"Warning: {jsonl_path} not found")
        return []
    
    teams = []
    with open(jsonl_path) as f:
        for line in f:
            if line.strip():
                teams.append(json.loads(line))
    
    return teams


def normalize_league(
    league_seed: dict[str, Any],
    season_label: str = "2025-26",
    as_of: str | None = None,
) -> dict[str, Any]:
    """
    Normalize league seed data into leagues.csv row.
    
    Args:
        league_seed: League entry from leagues_seed.yaml
        season_label: Current season label
        as_of: ISO date for data snapshot
        
    Returns:
        Dictionary matching leagues.csv schema
    """
    if as_of is None:
        as_of = datetime.now(timezone.utc).date().isoformat()
    
    return {
        "league_id": league_seed["league_id"],
        "name": league_seed["name"],
        "gender": league_seed["gender"],
        "tier": league_seed["tier"],
        "country_or_region": league_seed["country_or_region"],
        "governing_body": league_seed["governing_body"],
        "wikidata_qid": league_seed["wikidata_qid"],
        "wikipedia_en": league_seed["wikipedia_en"],
        "season_label": season_label,
        "as_of": as_of,
        "source_url": f"https://www.wikidata.org/wiki/{league_seed['wikidata_qid']}",
        "confidence": "HIGH" if league_seed.get("status") == "active" else "MEDIUM",
    }


OWNERSHIP_STRUCTURE_VOCAB = ["sole", "majority", "group", "public", "municipal", "unknown"]

# Country QID to ISO-3166-1 alpha-2 mapping
COUNTRY_CODE_MAP = {
    "Q30": "US",  # United States
    "Q16": "CA",  # Canada
}


def map_ownership_structure(owner_label: str | None) -> str:
    """
    Map owner to ownership_structure vocabulary.
    
    Conservative mapping - only map when confident.
    Default to 'unknown' when unsure.
    """
    if not owner_label:
        return "unknown"
    
    owner_lower = owner_label.lower()
    
    # Sole ownership indicators
    if any(indicator in owner_lower for indicator in [
        "family",  # e.g., "DeVos family"
    ]):
        return "sole"
    
    # Group ownership indicators
    if any(indicator in owner_lower for indicator in [
        " & ",  # e.g., "Maple Leaf Sports & Entertainment"
        "entertainment",
        "sports",
        "group",
        "llc",
    ]):
        return "group"
    
    # Municipal/tribal ownership
    if any(indicator in owner_lower for indicator in [
        "tribe",  # e.g., "Mohegan Tribe"
        "tribal",
    ]):
        return "municipal"
    
    # Default: unknown (includes individual owners that we can't confidently classify)
    return "unknown"


def normalize_team(raw_team: dict[str, Any]) -> dict[str, Any]:
    """
    Normalize raw Wikidata team data into teams.csv row.
    
    Args:
        raw_team: Team data from fetch_wikidata_teams.py
        
    Returns:
        Dictionary matching teams.csv schema
    """
    team_qid = raw_team["team_qid"]
    league_id = raw_team["league_id"]
    
    # Build team_id slug
    team_label = raw_team.get("team_label", "")
    # Extract short name (e.g., "Los Angeles Lakers" -> "lakers")
    short_name_slug = slugify(team_label.split()[-1]) if team_label else team_qid
    team_id = f"{league_id}_{short_name_slug}_{team_qid.lower()}"
    
    # Extract Wikipedia title from URL
    wikipedia_en = None
    if raw_team.get("wikipedia_en"):
        wikipedia_en = raw_team["wikipedia_en"].replace("_", " ")
    
    # Extract city from HQ or venue
    city = raw_team.get("hq_label")
    
    # Country: map QID to ISO-3166-1 alpha-2
    country_qid = raw_team.get("country_qid")
    country = COUNTRY_CODE_MAP.get(country_qid) if country_qid else None
    
    # Founded year from inception
    founded_year = extract_year_from_date(raw_team.get("inception"))
    
    # Abbreviation: extract from stub data or leave blank
    abbr = raw_team.get("abbr")  # Will be added to stub data
    
    # Former names: pipe-separated if available
    former_names = raw_team.get("former_names")
    
    # Colors: ONLY official hex from Wikidata P465 or official sources
    # NEVER sample from logo pixels or invent colors
    # Leave blank + confidence=gap if no official color claim
    colours_primary_hex = None
    colours_secondary_hex = None
    colours_accent_hex = None
    colours_source = None
    
    # Arena capacity
    arena_capacity = None
    if raw_team.get("venue_capacity"):
        try:
            arena_capacity = int(float(raw_team["venue_capacity"]))
        except ValueError:
            pass
    
    # Ownership structure: locked vocabulary only
    # Map from owner_label using conservative heuristics
    ownership_structure = map_ownership_structure(raw_team.get("owner_label"))
    
    # Confidence: HIGH if we have Wikipedia + QID, MEDIUM if partial, GAP if minimal
    confidence = "GAP"
    if team_label and wikipedia_en and raw_team.get("venue_label"):
        confidence = "HIGH"
    elif team_label and wikipedia_en:
        confidence = "MEDIUM"
    
    return {
        "team_id": team_id,
        "league_id": league_id,
        "name": team_label,
        "abbr": abbr,
        "short_name": team_label.split()[-1] if team_label else None,
        "former_names": former_names,
        "city": city,
        "country": country,
        "arena": raw_team.get("venue_label"),
        "arena_capacity": arena_capacity,
        "founded_year": founded_year,
        "colours_primary_hex": colours_primary_hex,
        "colours_secondary_hex": colours_secondary_hex,
        "colours_accent_hex": colours_accent_hex,
        "colours_source": colours_source,
        "mascot": raw_team.get("mascot_label"),
        "owner": raw_team.get("owner_label"),  # Free text
        "ownership_structure": ownership_structure,  # Locked vocab only
        "wikidata_qid": team_qid,
        "wikipedia_en": wikipedia_en,
        "official_url": raw_team.get("official_website"),
        "as_of": datetime.now(timezone.utc).date().isoformat(),
        "source_url": f"https://www.wikidata.org/wiki/{team_qid}",
        "confidence": confidence,
    }


def _keep_other_leagues(path: Path, refreshed: pd.DataFrame) -> pd.DataFrame:
    """Keep rows for leagues this run did not refresh.

    The NBA normalizer and the EuroLeague fetcher share teams.csv.
    Each writer may replace only the league_ids it just produced.
    """
    if refreshed.empty or "league_id" not in refreshed.columns or not path.exists():
        return refreshed

    existing = pd.read_csv(path, dtype=str).fillna("")
    if "league_id" not in existing.columns:
        return refreshed

    refreshed_ids = set(refreshed["league_id"].dropna().astype(str))
    kept = existing[~existing["league_id"].isin(refreshed_ids)].copy()
    if kept.empty:
        return refreshed

    for column in refreshed.columns:
        if column not in kept.columns:
            kept[column] = ""
    kept = kept[list(refreshed.columns)]
    return pd.concat([refreshed.fillna(""), kept], ignore_index=True)


def main():
    parser = argparse.ArgumentParser(
        description="Normalize raw Wikidata teams into derived CSVs"
    )
    parser.add_argument(
        "--seed",
        type=Path,
        default=Path("src/hoops_data/teams/leagues_seed.yaml"),
        help="Path to leagues seed YAML",
    )
    parser.add_argument(
        "--raw-dir",
        type=Path,
        default=Path("data/raw/wikidata"),
        help="Input directory with raw JSONL",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/derived/teams"),
        help="Output directory for CSVs",
    )
    
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    
    # Load leagues seed
    with open(args.seed) as f:
        seed_data = yaml.safe_load(f)
    
    # Normalize leagues
    print("Normalizing leagues...")
    leagues = []
    for league_seed in seed_data["leagues"]:
        if league_seed.get("status") == "active":
            league_row = normalize_league(league_seed)
            leagues.append(league_row)
    
    leagues_df = pd.DataFrame(leagues)
    leagues_path = args.output_dir / "leagues.csv"
    leagues_df = _keep_other_leagues(leagues_path, leagues_df)
    leagues_df.to_csv(leagues_path, index=False)
    print(f"  ✓ Wrote {len(leagues_df)} leagues to {leagues_path}")
    
    # Normalize teams
    print("Normalizing teams...")
    teams = []
    for league_seed in seed_data["leagues"]:
        if league_seed.get("status") == "active":
            league_id = league_seed["league_id"]
            raw_teams = load_raw_teams(args.raw_dir, league_id)
            
            for raw_team in raw_teams:
                team_row = normalize_team(raw_team)
                teams.append(team_row)
            
            print(f"  ✓ Normalized {len(raw_teams)} teams from {league_id}")
    
    teams_df = pd.DataFrame(teams)
    teams_path = args.output_dir / "teams.csv"
    teams_df = _keep_other_leagues(teams_path, teams_df)
    teams_df.to_csv(teams_path, index=False)
    print(f"  ✓ Wrote {len(teams_df)} teams to {teams_path}")

    # Do not wipe logo rows that another pass already recorded.
    logos_path = args.output_dir / "logos.csv"
    if not logos_path.exists():
        print("Creating empty logos.csv...")
        logos_columns = [
            "team_id",
            "logo_kind",
            "year_start",
            "year_end",
            "commons_title",
            "commons_url",
            "local_path",
            "mime",
            "sha256",
            "license",
            "attribution",
            "as_of",
            "confidence",
        ]
        pd.DataFrame(columns=logos_columns).to_csv(logos_path, index=False)
        print(f"  ✓ Created {logos_path} (schema only)")
    
    print(f"\n✓ Complete. Wrote {len(leagues_df)} leagues, {len(teams_df)} teams.")
    return 0


if __name__ == "__main__":
    exit(main())
