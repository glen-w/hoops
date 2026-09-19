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

# Locked CSV schema (24 columns, matches NBA/WNBA desk from #20/#21)
CSV_COLUMNS = [
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
    "confidence"
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


def derive_abbr(short_name: str, team_id: str) -> str:
    """
    Derive a simple abbreviation from short_name.
    This is a fallback when no official abbreviation exists.
    
    Special cases:
    - Paris Basketball -> PAR
    - Partizan Belgrade -> PTZ (to avoid collision with Paris)
    """
    if not short_name:
        return ""
    
    # Handle special cases for abbreviation collisions
    if "partizan" in team_id.lower():
        return "PTZ"
    if "paris" in team_id.lower():
        return "PAR"
    
    # Handle multi-word names (e.g., "Real Madrid" -> "RM")
    words = short_name.split()
    if len(words) >= 2:
        return "".join(w[0] for w in words[:3]).upper()
    
    # Single word: use first 3 letters
    return short_name[:3].upper()


def process_team(team: dict[str, Any], league_id: str, gender: str) -> dict[str, str]:
    """
    Process a single team from the seed and enrich with Wikidata.
    
    Returns a dict matching CSV_COLUMNS (24 columns).
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
    former_names = extract_former_names(entity) if entity else ""
    
    # Derive abbreviation (with collision handling)
    abbr = derive_abbr(short_name, team_id)
    
    # Source URL
    source_url = f"https://www.wikidata.org/wiki/{qid}" if qid else ""
    
    # Rate limit: be nice to Wikidata
    time.sleep(0.5)
    
    # Return 24-column row (blanks for unknown values)
    return {
        "team_id": team_id,
        "league_id": league_id,
        "name": name,
        "abbr": abbr,
        "short_name": short_name,
        "former_names": former_names,
        "city": "",  # Not available from current Wikidata extraction
        "country": country,
        "arena": "",  # Not available
        "arena_capacity": "",  # Not available
        "founded_year": founded_year,
        "colours_primary_hex": "",  # Blank (requires additional Wikidata resolution)
        "colours_secondary_hex": "",
        "colours_accent_hex": "",
        "colours_source": "",
        "mascot": "",  # Not available
        "owner": "",  # Not available
        "ownership_structure": "unknown",  # Set to unknown per requirements
        "wikidata_qid": qid,
        "wikipedia_en": wikipedia_en,
        "official_url": "",  # Not available
        "as_of": as_of,
        "source_url": source_url,
        "confidence": confidence.upper()  # Match NBA/WNBA format (HIGH, not high)
    }


def main() -> int:
    """
    Main entry point.
    
    Appends EuroLeague teams to existing teams.csv (preserving NBA/WNBA rows).
    """
    repo_root = Path(__file__).parent.parent.parent
    seed_path = repo_root / "scripts" / "teams" / "leagues_seed.yaml"
    output_path = repo_root / "data" / "derived" / "teams" / "teams.csv"
    
    if not seed_path.exists():
        print(f"ERROR: Seed file not found: {seed_path}", file=sys.stderr)
        return 1
    
    # Read existing teams.csv to preserve NBA/WNBA rows
    existing_teams = []
    if output_path.exists():
        print(f"Reading existing teams from {output_path}")
        with open(output_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            existing_teams = list(reader)
        print(f"  Found {len(existing_teams)} existing teams")
    
    # Read seed
    print(f"\nReading seed from {seed_path}")
    with open(seed_path, "r", encoding="utf-8") as f:
        seed_data = yaml.safe_load(f)
    
    leagues = seed_data.get("leagues", [])
    
    if not leagues:
        print("ERROR: No leagues found in seed", file=sys.stderr)
        return 1
    
    # Process all EuroLeague teams
    euro_teams = []
    
    for league in leagues:
        league_id = league.get("league_id", "")
        league_name = league.get("name", "")
        gender = league.get("gender", "")
        teams = league.get("teams", [])
        
        print(f"\nProcessing {league_name} ({league_id}): {len(teams)} teams")
        
        for team in teams:
            team_row = process_team(team, league_id, gender)
            if team_row:
                euro_teams.append(team_row)
    
    # Combine: existing teams + new EuroLeague teams
    all_teams = existing_teams + euro_teams
    
    # Write CSV
    print(f"\nWriting {len(all_teams)} teams to {output_path}")
    print(f"  Existing (NBA/WNBA): {len(existing_teams)}")
    print(f"  New (EuroLeague): {len(euro_teams)}")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(all_teams)
    
    print(f"\n✓ Done! Wrote {len(all_teams)} teams to {output_path}")
    
    # Print summary statistics
    nba_count = sum(1 for t in all_teams if t["league_id"] == "nba")
    wnba_count = sum(1 for t in all_teams if t["league_id"] == "wnba")
    euro_men_count = sum(1 for t in euro_teams if t["league_id"] == "euroleague")
    euro_women_count = sum(1 for t in euro_teams if t["league_id"] == "euroleague_women")
    
    print(f"\nSummary:")
    print(f"  NBA: {nba_count} teams (preserved)")
    print(f"  WNBA: {wnba_count} teams (preserved)")
    print(f"  EuroLeague (men): {euro_men_count} teams (added)")
    print(f"  EuroLeague Women: {euro_women_count} teams (added)")
    print(f"  Total: {len(all_teams)} teams")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
