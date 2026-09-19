#!/usr/bin/env python3
"""
Add P0h teams (ABA, PBA, G League, Israeli Premier) to teams.csv.

This script:
1. Reads the P0h seed fragment (77 teams with QIDs)
2. Appends to the existing teams.csv (preserving all existing rows)
3. Ensures abbr codes are unique within each league_id
4. Follows the locked 24-column schema

Hard requirements:
- APPEND-ONLY: Do not modify existing rows
- Uniquify abbrs within league_id
- No invented QIDs or colors
- Preserve all 24 columns
"""

import csv
import sys
from pathlib import Path
from typing import Any
import yaml


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


def derive_abbr(short_name: str, team_id: str) -> str:
    """
    Derive abbreviation from short_name.
    Uses team_id suffix as fallback.
    """
    if not short_name:
        # Use team_id suffix as fallback
        suffix = team_id.split("_")[-1]
        return suffix.upper()[:3]
    
    # Handle multi-word names (e.g., "Rain or Shine" -> "ROS")
    words = short_name.split()
    if len(words) >= 2:
        return "".join(w[0] for w in words[:3]).upper()
    
    # Single word: use first 3 letters
    return short_name[:3].upper()


def uniquify_abbrs(teams: list[dict[str, str]], league_id: str, existing_abbrs: set[str]) -> list[dict[str, str]]:
    """
    Ensure abbr codes are unique within a league.
    If collision, append numeric suffix.
    """
    seen_abbrs = existing_abbrs.copy()
    result = []
    
    for team in teams:
        abbr = team["abbr"]
        original_abbr = abbr
        counter = 2
        
        while abbr in seen_abbrs:
            # Try numeric suffix
            if len(original_abbr) <= 2:
                abbr = f"{original_abbr}{counter}"
            else:
                abbr = f"{original_abbr[:2]}{counter}"
            counter += 1
        
        seen_abbrs.add(abbr)
        team["abbr"] = abbr
        result.append(team)
    
    return result


def load_existing_teams(csv_path: Path) -> tuple[list[dict[str, str]], dict[str, set[str]]]:
    """
    Load existing teams from CSV.
    Returns (rows, {league_id: {abbr_set}})
    """
    if not csv_path.exists():
        return [], {}
    
    rows = []
    abbrs_by_league = {}
    
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append({col: row.get(col, "") for col in DESK_COLUMNS})
            league_id = row.get("league_id", "")
            abbr = row.get("abbr", "")
            if league_id and abbr:
                if league_id not in abbrs_by_league:
                    abbrs_by_league[league_id] = set()
                abbrs_by_league[league_id].add(abbr)
    
    return rows, abbrs_by_league


def process_team(team: dict[str, Any], league_id: str, existing_abbrs: set[str]) -> dict[str, str]:
    """
    Convert team from seed YAML to CSV row format.
    """
    qid = team.get("wikidata_qid", "")
    team_id = team.get("team_id", "")
    name = team.get("name", "")
    short_name = team.get("short_name", "")
    
    # Derive abbr from short_name
    abbr = derive_abbr(short_name, team_id)
    
    row = {col: "" for col in DESK_COLUMNS}
    row.update({
        "team_id": team_id,
        "league_id": league_id,
        "name": name,
        "abbr": abbr,
        "short_name": short_name,
        "former_names": "",
        "city": "",
        "country": "",
        "arena": "",
        "arena_capacity": "",
        "founded_year": "",
        "colours_primary_hex": "",
        "colours_secondary_hex": "",
        "colours_accent_hex": "",
        "colours_source": "",
        "mascot": "",
        "owner": "",
        "ownership_structure": "",
        "wikidata_qid": qid,
        "wikipedia_en": team.get("wikipedia_en", ""),
        "official_url": "",
        "as_of": team.get("as_of", ""),
        "source_url": f"https://www.wikidata.org/wiki/{qid}" if qid else "",
        "confidence": team.get("confidence", "").upper(),
    })
    
    return row


def main() -> int:
    repo_root = Path(__file__).parent.parent.parent
    seed_path = Path("/home/ubuntu/.cursor/projects/workspace/uploads/leagues_seed_fragment_608e.yaml")
    output_path = repo_root / "data" / "derived" / "teams" / "teams.csv"
    
    if not seed_path.exists():
        print(f"ERROR: Seed fragment not found: {seed_path}", file=sys.stderr)
        return 1
    
    # Load P0h seed fragment
    print(f"Reading P0h seed from {seed_path}")
    with open(seed_path, "r", encoding="utf-8") as f:
        seed_data = yaml.safe_load(f)
    
    leagues = seed_data.get("leagues", [])
    if not leagues:
        print("ERROR: No leagues found in seed fragment", file=sys.stderr)
        return 1
    
    # Load existing teams
    print(f"Loading existing teams from {output_path}")
    existing_rows, existing_abbrs = load_existing_teams(output_path)
    print(f"  Found {len(existing_rows)} existing teams")
    
    # Process P0h teams
    new_teams_by_league = {}
    
    for league in leagues:
        league_id = league.get("league_id", "")
        league_name = league.get("name", "")
        teams = league.get("teams", [])
        
        if league.get("status") == "gap":
            print(f"  Skipping {league_name} (status=gap)")
            continue
        
        print(f"\nProcessing {league_name} ({league_id}): {len(teams)} teams")
        
        league_teams = []
        for team in teams:
            if team.get("status") == "gap":
                print(f"  Skipping {team.get('team_id')} (status=gap)")
                continue
            
            league_abbrs = existing_abbrs.get(league_id, set())
            row = process_team(team, league_id, league_abbrs)
            league_teams.append(row)
            print(f"  ✓ {row['team_id']}: {row['name']} ({row['abbr']})")
        
        new_teams_by_league[league_id] = league_teams
    
    # Uniquify abbrs within each league
    print("\nUniquifying abbreviations within leagues...")
    all_new_teams = []
    for league_id, teams in new_teams_by_league.items():
        league_abbrs = existing_abbrs.get(league_id, set())
        unique_teams = uniquify_abbrs(teams, league_id, league_abbrs)
        all_new_teams.extend(unique_teams)
        
        # Print final abbrs
        print(f"  {league_id}: {', '.join(t['abbr'] for t in unique_teams)}")
    
    # Combine existing + new
    combined = existing_rows + all_new_teams
    
    print(f"\nWriting {len(combined)} teams to {output_path}")
    print(f"  Existing: {len(existing_rows)}")
    print(f"  New (P0h): {len(all_new_teams)}")
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DESK_COLUMNS)
        writer.writeheader()
        writer.writerows(combined)
    
    print(f"\n✓ Done! {len(all_new_teams)} P0h teams appended.")
    
    # Summary by league
    print("\nSummary:")
    for league_id, teams in new_teams_by_league.items():
        print(f"  {league_id}: {len(teams)} teams")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
