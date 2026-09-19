#!/usr/bin/env python3
"""
Test suite for teams data validation.

Validates:
- Row counts match seed expectations
- CSV schema locks
- Required fields are populated
- Data integrity (QIDs, country codes, etc.)

Exit codes:
- 0: All tests pass
- 1: One or more tests fail
"""

import csv
import sys
from pathlib import Path
from typing import Any

import yaml


# Expected row counts
EXPECTED_NBA = 30
EXPECTED_WNBA = 12
EXPECTED_EUROLEAGUE_MEN = 20
EXPECTED_EUROLEAGUE_WOMEN_WITH_QIDS = 22  # 24 total - 2 gaps
EXPECTED_TOTAL = EXPECTED_NBA + EXPECTED_WNBA + EXPECTED_EUROLEAGUE_MEN + EXPECTED_EUROLEAGUE_WOMEN_WITH_QIDS

# Locked CSV schema (24 columns, matches NBA/WNBA desk from #20/#21)
EXPECTED_COLUMNS = [
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

# Valid ownership structure vocabulary
VALID_OWNERSHIP_STRUCTURE = {"sole", "majority", "group", "public", "municipal", "unknown", ""}

# Valid confidence levels
VALID_CONFIDENCE = {"HIGH", "MEDIUM", "LOW", "GAP", ""}  # Match NBA/WNBA format

# ISO 3166-1 alpha-2 country codes (partial list for validation)
VALID_COUNTRY_CODES = {
    "US", "CA",  # NBA/WNBA
    "BE", "FR", "DE", "IT", "ES", "GR", "TR", "PL", "CZ", "HU", 
    "RO", "LT", "RS", "IL", "AE",  # EuroLeague
    ""  # Empty string allowed for unknown
}


class TestFailure(Exception):
    """Raised when a test fails."""
    pass


def load_seed() -> dict[str, Any]:
    """Load the seed YAML file."""
    repo_root = Path(__file__).parent.parent.parent
    seed_path = repo_root / "scripts" / "teams" / "leagues_seed.yaml"
    
    with open(seed_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_teams_csv() -> list[dict[str, str]]:
    """Load the teams CSV file."""
    repo_root = Path(__file__).parent.parent.parent
    csv_path = repo_root / "data" / "derived" / "teams" / "teams.csv"
    
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def test_csv_exists():
    """Test that teams.csv exists."""
    repo_root = Path(__file__).parent.parent.parent
    csv_path = repo_root / "data" / "derived" / "teams" / "teams.csv"
    
    if not csv_path.exists():
        raise TestFailure(f"teams.csv not found at {csv_path}")
    
    print("✓ teams.csv exists")


def test_schema_locked():
    """Test that CSV columns match the locked schema."""
    teams = load_teams_csv()
    
    if not teams:
        raise TestFailure("teams.csv is empty")
    
    actual_columns = list(teams[0].keys())
    
    if actual_columns != EXPECTED_COLUMNS:
        raise TestFailure(
            f"Schema mismatch.\n"
            f"Expected: {EXPECTED_COLUMNS}\n"
            f"Got: {actual_columns}"
        )
    
    print(f"✓ Schema locked ({len(EXPECTED_COLUMNS)} columns)")


def test_row_counts():
    """Test that row counts match expected values."""
    teams = load_teams_csv()
    
    total_count = len(teams)
    nba_count = sum(1 for t in teams if t["league_id"] == "nba")
    wnba_count = sum(1 for t in teams if t["league_id"] == "wnba")
    euro_men_count = sum(1 for t in teams if t["league_id"] == "euroleague")
    euro_women_count = sum(1 for t in teams if t["league_id"] == "euroleague_women")
    
    if total_count != EXPECTED_TOTAL:
        raise TestFailure(
            f"Total row count mismatch. Expected {EXPECTED_TOTAL}, got {total_count}"
        )
    
    if nba_count != EXPECTED_NBA:
        raise TestFailure(
            f"NBA count mismatch. Expected {EXPECTED_NBA}, got {nba_count}"
        )
    
    if wnba_count != EXPECTED_WNBA:
        raise TestFailure(
            f"WNBA count mismatch. Expected {EXPECTED_WNBA}, got {wnba_count}"
        )
    
    if euro_men_count != EXPECTED_EUROLEAGUE_MEN:
        raise TestFailure(
            f"EuroLeague (men) count mismatch. Expected {EXPECTED_EUROLEAGUE_MEN}, got {euro_men_count}"
        )
    
    if euro_women_count != EXPECTED_EUROLEAGUE_WOMEN_WITH_QIDS:
        raise TestFailure(
            f"EuroLeague Women count mismatch. Expected {EXPECTED_EUROLEAGUE_WOMEN_WITH_QIDS}, got {euro_women_count}"
        )
    
    print(f"✓ Row counts match expected:")
    print(f"  - NBA: {nba_count} teams")
    print(f"  - WNBA: {wnba_count} teams")
    print(f"  - EuroLeague (men): {euro_men_count} teams")
    print(f"  - EuroLeague Women: {euro_women_count} teams")
    print(f"  - Total: {total_count} teams")


def test_gaps_documented():
    """Test that gap teams are documented (not in CSV)."""
    seed = load_seed()
    
    gap_teams = []
    for league in seed.get("leagues", []):
        for team in league.get("teams", []):
            if team.get("status") == "gap":
                gap_teams.append(team.get("team_id"))
    
    if len(gap_teams) != 2:
        raise TestFailure(
            f"Expected 2 gap teams in seed, found {len(gap_teams)}: {gap_teams}"
        )
    
    # Verify gap teams are NOT in CSV
    teams = load_teams_csv()
    csv_team_ids = {t["team_id"] for t in teams}
    
    for gap_team_id in gap_teams:
        if gap_team_id in csv_team_ids:
            raise TestFailure(f"Gap team {gap_team_id} should not be in CSV")
    
    print(f"✓ Gap teams documented: {', '.join(gap_teams)}")


def test_required_fields():
    """Test that required fields are populated."""
    teams = load_teams_csv()
    
    required_fields = [
        "team_id", "league_id", "name", "short_name", "abbr",
        "wikidata_qid", "as_of", "confidence"
    ]
    
    for team in teams:
        for field in required_fields:
            if not team.get(field):
                raise TestFailure(
                    f"Required field '{field}' is empty for team {team.get('team_id')}"
                )
    
    print(f"✓ Required fields populated for all teams")


def test_abbr_unique_within_league():
    """Test that abbreviations are unique within each league."""
    teams = load_teams_csv()
    
    # Group teams by league_id
    by_league = {}
    for team in teams:
        league_id = team["league_id"]
        if league_id not in by_league:
            by_league[league_id] = []
        by_league[league_id].append(team)
    
    # Check uniqueness within each league
    for league_id, league_teams in by_league.items():
        abbrs = [t["abbr"] for t in league_teams]
        duplicates = [a for a in set(abbrs) if abbrs.count(a) > 1]
        
        if duplicates:
            collision_details = []
            for dup_abbr in duplicates:
                colliding_teams = [t["team_id"] for t in league_teams if t["abbr"] == dup_abbr]
                collision_details.append(f"{dup_abbr}: {', '.join(colliding_teams)}")
            
            raise TestFailure(
                f"Duplicate abbreviations in league {league_id}:\n  " +
                "\n  ".join(collision_details)
            )
    
    print("✓ Abbreviations are unique within each league")


def test_data_integrity():
    """Test data integrity (valid values)."""
    teams = load_teams_csv()
    
    for team in teams:
        team_id = team["team_id"]
        
        # Confidence must be valid
        if team["confidence"] and team["confidence"] not in VALID_CONFIDENCE:
            raise TestFailure(f"Invalid confidence for {team_id}: {team['confidence']}")
        
        # Ownership structure must be valid
        if team["ownership_structure"] and team["ownership_structure"] not in VALID_OWNERSHIP_STRUCTURE:
            raise TestFailure(f"Invalid ownership_structure for {team_id}: {team['ownership_structure']}")
        
        # Country code must be valid (or empty)
        if team["country"] and team["country"] not in VALID_COUNTRY_CODES:
            raise TestFailure(f"Invalid country code for {team_id}: {team['country']}")
        
        # QID must start with Q
        qid = team["wikidata_qid"]
        if qid and not qid.startswith("Q"):
            raise TestFailure(f"Invalid QID for {team_id}: {qid}")
        
        # League ID must match team_id prefix
        league_id = team["league_id"]
        if not team_id.startswith(league_id):
            raise TestFailure(
                f"Team ID {team_id} does not start with league_id {league_id}"
            )
    
    print("✓ Data integrity checks passed")


def test_league_ids():
    """Test that league IDs are correct."""
    teams = load_teams_csv()
    
    league_counts = {}
    for team in teams:
        league_id = team["league_id"]
        league_counts[league_id] = league_counts.get(league_id, 0) + 1
    
    # Check NBA
    if "nba" not in league_counts:
        raise TestFailure("No teams found for league_id 'nba'")
    if league_counts["nba"] != EXPECTED_NBA:
        raise TestFailure(
            f"Expected {EXPECTED_NBA} nba teams, "
            f"got {league_counts['nba']}"
        )
    
    # Check WNBA
    if "wnba" not in league_counts:
        raise TestFailure("No teams found for league_id 'wnba'")
    if league_counts["wnba"] != EXPECTED_WNBA:
        raise TestFailure(
            f"Expected {EXPECTED_WNBA} wnba teams, "
            f"got {league_counts['wnba']}"
        )
    
    # Check EuroLeague
    if "euroleague" not in league_counts:
        raise TestFailure("No teams found for league_id 'euroleague'")
    if league_counts["euroleague"] != EXPECTED_EUROLEAGUE_MEN:
        raise TestFailure(
            f"Expected {EXPECTED_EUROLEAGUE_MEN} euroleague teams, "
            f"got {league_counts['euroleague']}"
        )
    
    # Check EuroLeague Women
    if "euroleague_women" not in league_counts:
        raise TestFailure("No teams found for league_id 'euroleague_women'")
    if league_counts["euroleague_women"] != EXPECTED_EUROLEAGUE_WOMEN_WITH_QIDS:
        raise TestFailure(
            f"Expected {EXPECTED_EUROLEAGUE_WOMEN_WITH_QIDS} euroleague_women teams, "
            f"got {league_counts['euroleague_women']}"
        )
    
    print("✓ League IDs correct")


def main() -> int:
    """Run all tests."""
    tests = [
        test_csv_exists,
        test_schema_locked,
        test_row_counts,
        test_gaps_documented,
        test_required_fields,
        test_abbr_unique_within_league,
        test_data_integrity,
        test_league_ids,
    ]
    
    print("Running teams data validation tests...\n")
    
    failed = []
    
    for test in tests:
        try:
            test()
        except TestFailure as e:
            print(f"✗ {test.__name__}: {e}", file=sys.stderr)
            failed.append(test.__name__)
        except Exception as e:
            print(f"✗ {test.__name__}: Unexpected error: {e}", file=sys.stderr)
            failed.append(test.__name__)
    
    print()
    
    if failed:
        print(f"✗ {len(failed)} test(s) failed:", file=sys.stderr)
        for test_name in failed:
            print(f"  - {test_name}", file=sys.stderr)
        return 1
    else:
        print(f"✓ All {len(tests)} tests passed!")
        return 0


if __name__ == "__main__":
    sys.exit(main())
