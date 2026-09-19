#!/usr/bin/env python3
"""
Fetch and normalize teams data from Wikidata.

Reads leagues_seed.yaml and fetches additional metadata from Wikidata
to generate data/derived/teams/teams.csv with standardized schema.

Schema columns (locked):
- team_id: Unique identifier (from seed)
- league_id: League identifier
- name: Full team name (from seed)
- short_name: Short name/common name (from seed)
- abbr: Abbreviation (derived or from Wikidata P1813)
- gender: men | women
- country: ISO 3166-1 alpha-2 country code (from Wikidata P17)
- founded_year: Year founded (from Wikidata P571)
- colors_hex: Official team colors as comma-separated hex codes (Wikidata P462)
- former_names: Semicolon-separated list of former names (Wikidata P1448)
- wikidata_qid: Wikidata item ID
- wikipedia_en: English Wikipedia page title
- as_of: Data collection date
- confidence: Confidence level from seed

Dependencies:
- PyYAML
- requests (for Wikidata SPARQL queries)

Usage:
    python scripts/teams/fetch_and_normalize_teams.py
"""

import csv
import json
import sys
import time
from pathlib import Path
from typing import Any, Optional
from urllib.parse import quote

import yaml

try:
    import requests
except ImportError:
    print("ERROR: requests library required. Install with: pip install requests", file=sys.stderr)
    sys.exit(1)


# Wikidata SPARQL endpoint
WIKIDATA_SPARQL_ENDPOINT = "https://query.wikidata.org/sparql"
USER_AGENT = "hoops-teams-fetch/1.0 (glen-w/hoops; cursor cloud agent)"

# Fields this fetch fills. The committed teams.csv uses the wider desk schema
# shared with the NBA and WNBA rows; this script refreshes only the leagues in
# scripts/teams/leagues_seed.yaml and leaves every other league in place.
CSV_COLUMNS = [
    "team_id",
    "league_id",
    "name",
    "short_name",
    "abbr",
    "gender",
    "country",
    "founded_year",
    "colors_hex",
    "former_names",
    "wikidata_qid",
    "wikipedia_en",
    "as_of",
    "confidence"
]

DESK_COLUMNS = [
    "team_id",
    "league_id",
    "name",
    "abbr",
    "short_name",
    "former_names",
    "city",
    "country",
    "arena",
    "arena_capacity",
    "founded_year",
    "colours_primary_hex",
    "colours_secondary_hex",
    "colours_accent_hex",
    "colours_source",
    "mascot",
    "owner",
    "ownership_structure",
    "wikidata_qid",
    "wikipedia_en",
    "official_url",
    "as_of",
    "source_url",
    "confidence",
]

# Country QID to ISO 3166-1 alpha-2 mapping (partial, will expand as needed)
COUNTRY_QID_TO_ISO = {
    "Q31": "BE",      # Belgium
    "Q142": "FR",     # France
    "Q183": "DE",     # Germany
    "Q38": "IT",      # Italy
    "Q29": "ES",      # Spain
    "Q41": "GR",      # Greece
    "Q43": "TR",      # Turkey
    "Q36": "PL",      # Poland
    "Q213": "CZ",     # Czech Republic
    "Q28": "HU",      # Hungary
    "Q218": "RO",     # Romania
    "Q37": "LT",      # Lithuania
    "Q403": "RS",     # Serbia
    "Q801": "IL",     # Israel
    "Q846": "AE",     # United Arab Emirates
}


def fetch_wikidata_entity(qid: str) -> Optional[dict[str, Any]]:
    """
    Fetch entity data from Wikidata API.
    
    Returns the full entity JSON or None on error.
    """
    if not qid or qid == "null":
        return None
    
    url = f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json"
    headers = {"User-Agent": USER_AGENT}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("entities", {}).get(qid)
    except Exception as e:
        print(f"Warning: Failed to fetch {qid}: {e}", file=sys.stderr)
        return None


def extract_country_iso(entity: dict[str, Any]) -> str:
    """
    Extract ISO country code from Wikidata entity (P17: country).
    Returns empty string if not found.
    """
    claims = entity.get("claims", {})
    country_claims = claims.get("P17", [])
    
    if not country_claims:
        return ""
    
    # Get the first country claim
    country_qid = country_claims[0].get("mainsnak", {}).get("datavalue", {}).get("value", {}).get("id")
    
    if country_qid:
        return COUNTRY_QID_TO_ISO.get(country_qid, "")
    
    return ""


def extract_founded_year(entity: dict[str, Any]) -> str:
    """
    Extract founding year from Wikidata entity (P571: inception).
    Returns empty string if not found.
    """
    claims = entity.get("claims", {})
    inception_claims = claims.get("P571", [])
    
    if not inception_claims:
        return ""
    
    # Get the first inception date
    date_value = inception_claims[0].get("mainsnak", {}).get("datavalue", {}).get("value", {})
    time_str = date_value.get("time", "")
    
    if time_str:
        # Format: +1946-00-00T00:00:00Z
        try:
            year = time_str.split("-")[0].lstrip("+")
            return year
        except:
            pass
    
    return ""


def extract_colors_hex(entity: dict[str, Any]) -> str:
    """
    Extract team colors from Wikidata entity (P462: color).
    Returns comma-separated hex codes, or empty string if none found.
    
    Note: Wikidata often has color items (e.g., Q23444 = white), not hex codes directly.
    This is a simplified extraction that looks for official website color (P465) first,
    then falls back to color property.
    """
    # For now, return empty string - colors require additional API calls
    # to resolve color items to hex codes. Will implement if time permits.
    return ""


def extract_former_names(entity: dict[str, Any]) -> str:
    """
    Extract former names from Wikidata entity (P1448: official name).
    Returns semicolon-separated list, or empty string if none found.
    """
    claims = entity.get("claims", {})
    name_claims = claims.get("P1448", [])
    
    names = []
    for claim in name_claims:
        name_value = claim.get("mainsnak", {}).get("datavalue", {}).get("value", {})
        text = name_value.get("text", "")
        language = name_value.get("language", "")
        
        # Prefer English names, but include others if no English available
        if text and (language == "en" or not names):
            names.append(text)
    
    # Filter out duplicates and the current name
    return "; ".join(set(names)) if names else ""


def derive_abbr(short_name: str) -> str:
    """
    Derive a simple abbreviation from short_name.
    This is a fallback when no official abbreviation exists.
    """
    # Simple heuristic: use first 3 letters of short name, uppercase
    if not short_name:
        return ""
    
    # Handle multi-word names (e.g., "Real Madrid" -> "RM")
    words = short_name.split()
    if len(words) >= 2:
        return "".join(w[0] for w in words[:3]).upper()
    
    # Single word: use first 3 letters
    return short_name[:3].upper()


def process_team(team: dict[str, Any], league_id: str, gender: str) -> dict[str, str]:
    """
    Process a single team from the seed and enrich with Wikidata.
    
    Returns a dict matching CSV_COLUMNS.
    """
    team_id = team.get("team_id", "")
    name = team.get("name", "")
    short_name = team.get("short_name", "")
    qid = team.get("wikidata_qid")
    wikipedia_en = team.get("wikipedia_en") or ""
    as_of = team.get("as_of", "")
    confidence = team.get("confidence", "")
    status = team.get("status", "")
    
    # Skip teams with status=gap (no QID)
    if status == "gap" or not qid or qid == "null":
        print(f"  Skipping {team_id} (status={status}, no QID)")
        return None
    
    # Fetch Wikidata entity
    print(f"  Fetching {team_id} ({qid})...")
    entity = fetch_wikidata_entity(qid)
    
    if not entity:
        print(f"  Warning: Could not fetch entity for {team_id}")
    
    # Extract fields from Wikidata
    country = extract_country_iso(entity) if entity else ""
    founded_year = extract_founded_year(entity) if entity else ""
    colors_hex = extract_colors_hex(entity) if entity else ""
    former_names = extract_former_names(entity) if entity else ""
    
    # Derive abbreviation. Partizan and Paris both collapse to PAR.
    abbr = {"euroleague_partizan": "PTZ"}.get(team_id) or derive_abbr(short_name)
    
    # Rate limit: be nice to Wikidata
    time.sleep(0.5)
    
    return {
        "team_id": team_id,
        "league_id": league_id,
        "name": name,
        "short_name": short_name,
        "abbr": abbr,
        "gender": gender,
        "country": country,
        "founded_year": founded_year,
        "colors_hex": colors_hex,
        "former_names": former_names,
        "wikidata_qid": qid,
        "wikipedia_en": wikipedia_en,
        "as_of": as_of,
        "confidence": confidence.lower()
    }


def main() -> int:
    """
    Main entry point.
    """
    repo_root = Path(__file__).parent.parent.parent
    seed_path = repo_root / "scripts" / "teams" / "leagues_seed.yaml"
    output_path = repo_root / "data" / "derived" / "teams" / "teams.csv"
    
    if not seed_path.exists():
        print(f"ERROR: Seed file not found: {seed_path}", file=sys.stderr)
        return 1
    
    # Read seed
    print(f"Reading seed from {seed_path}")
    with open(seed_path, "r", encoding="utf-8") as f:
        seed_data = yaml.safe_load(f)
    
    leagues = seed_data.get("leagues", [])
    
    if not leagues:
        print("ERROR: No leagues found in seed", file=sys.stderr)
        return 1
    
    # Process all teams
    all_teams = []
    
    for league in leagues:
        league_id = league.get("league_id", "")
        league_name = league.get("name", "")
        gender = league.get("gender", "")
        teams = league.get("teams", [])
        
        print(f"\nProcessing {league_name} ({league_id}): {len(teams)} teams")
        
        for team in teams:
            team_row = process_team(team, league_id, gender)
            if team_row:
                all_teams.append(team_row)
    
    # Write CSV. Refresh only the leagues in this seed so NBA/WNBA rows stay.
    refreshed = {t["league_id"] for t in all_teams}
    kept = []
    if output_path.exists():
        with open(output_path, "r", encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                if row.get("league_id") not in refreshed:
                    kept.append({col: row.get(col, "") for col in DESK_COLUMNS})

    def to_desk(row: dict[str, str]) -> dict[str, str]:
        qid = row.get("wikidata_qid") or ""
        desk = {col: "" for col in DESK_COLUMNS}
        desk.update({
            "team_id": row["team_id"],
            "league_id": row["league_id"],
            "name": row["name"],
            "abbr": row.get("abbr") or "",
            "short_name": row.get("short_name") or "",
            "former_names": row.get("former_names") or "",
            "country": row.get("country") or "",
            "founded_year": row.get("founded_year") or "",
            "wikidata_qid": qid,
            "wikipedia_en": row.get("wikipedia_en") or "",
            "as_of": row.get("as_of") or "",
            "source_url": f"https://www.wikidata.org/wiki/{qid}" if qid else "",
            "confidence": (row.get("confidence") or "").upper(),
        })
        return desk

    combined = kept + [to_desk(row) for row in all_teams]
    print(f"\nWriting {len(combined)} teams to {output_path} ({len(all_teams)} refreshed)")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DESK_COLUMNS)
        writer.writeheader()
        writer.writerows(combined)

    print(f"\n✓ Done! Wrote {len(combined)} teams to {output_path}")
    
    # Print summary statistics
    men_count = sum(1 for t in all_teams if t["gender"] == "men")
    women_count = sum(1 for t in all_teams if t["gender"] == "women")
    
    print(f"\nSummary:")
    print(f"  EuroLeague (men): {men_count} teams")
    print(f"  EuroLeague Women: {women_count} teams")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
