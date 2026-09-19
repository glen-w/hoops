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


# Locked desk schema. Same header as data/derived/teams/teams.csv.
EXPECTED_NBA = 30
EXPECTED_WNBA = 12
EXPECTED_EUROLEAGUE_MEN = 20
EXPECTED_EUROLEAGUE_WOMEN_WITH_QIDS = 22  # 24 in the seed, 2 gaps
EXPECTED_LIGA_ACB = 18  # P0e: Spanish men
EXPECTED_LNB_ELITE = 16  # P0e: French men
EXPECTED_BBL = 18  # P0e: German men
EXPECTED_SERIE_A = 16  # P0e: Italian men
EXPECTED_GREEK_BASKET_LEAGUE = 14  # P0e: Greek men
EXPECTED_LF_ENDESA = 9  # P0e: Spanish women (16 in seed, 7 gaps)
EXPECTED_LFB = 10  # P0e: French women (12 in seed, 2 gaps)
EXPECTED_WNBL = 9  # P0e: Australian women
# P0f: Asia/Oceania/Africa/Turkey domestics
EXPECTED_CBA = 20  # P0f: Chinese men
EXPECTED_B_LEAGUE = 26  # P0f: Japanese men
EXPECTED_KBL = 10  # P0f: Korean men
EXPECTED_NBL = 10  # P0f: Australian men
EXPECTED_BSL = 16  # P0f: Turkish men
EXPECTED_BAL = 12  # P0f: African men (continental)
EXPECTED_WCBA = 14  # P0f: Chinese women (21 in seed, 7 gaps)
EXPECTED_WJBL = 8  # P0f: Japanese women
# P0g: Americas domestics
EXPECTED_NBB = 17  # P0g: Brazilian men (18 in seed, 1 gap)
EXPECTED_LNB_ARGENTINA = 18  # P0g: Argentine men
EXPECTED_LNBP = 14  # P0g: Mexican men
EXPECTED_LBF = 1  # P0g: Brazilian women (10 in seed, 9 gaps)
EXPECTED_LFB_ARGENTINA = 4  # P0g: Argentine women (20 in seed, 16 gaps)
EXPECTED_TOTAL = (
    EXPECTED_NBA
    + EXPECTED_WNBA
    + EXPECTED_EUROLEAGUE_MEN
    + EXPECTED_EUROLEAGUE_WOMEN_WITH_QIDS
    + EXPECTED_LIGA_ACB
    + EXPECTED_LNB_ELITE
    + EXPECTED_BBL
    + EXPECTED_SERIE_A
    + EXPECTED_GREEK_BASKET_LEAGUE
    + EXPECTED_LF_ENDESA
    + EXPECTED_LFB
    + EXPECTED_WNBL
    + EXPECTED_CBA
    + EXPECTED_B_LEAGUE
    + EXPECTED_KBL
    + EXPECTED_NBL
    + EXPECTED_BSL
    + EXPECTED_BAL
    + EXPECTED_WCBA
    + EXPECTED_WJBL
    + EXPECTED_NBB
    + EXPECTED_LNB_ARGENTINA
    + EXPECTED_LNBP
    + EXPECTED_LBF
    + EXPECTED_LFB_ARGENTINA
)

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
    "confidence",
]

# Valid confidence levels
VALID_CONFIDENCE = {"high", "medium", "low", "gap"}

# ISO 3166-1 alpha-2 country codes (partial list for validation)
VALID_COUNTRY_CODES = {
    "BE", "FR", "DE", "IT", "ES", "GR", "TR", "PL", "CZ", "HU", 
    "RO", "LT", "RS", "IL", "AE", "AU", "CA", "US",
    "CN", "JP", "KR",  # P0f: Asia
    "NZ",  # P0f: New Zealand (NBL)
    "ML", "NG", "MA", "TN", "EG", "KE", "TZ", "ZA", "AO", "BW", "RW", "SN", "CI", "CM", "LY", "UG", "MZ",  # P0f: Africa (BAL)
    "BR", "AR", "MX",  # P0g: Americas domestics
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


def euroleague_rows() -> list[dict[str, str]]:
    """Rows this seed owns. NBA and WNBA stay in the same file."""
    seed_leagues = {
        "euroleague", "euroleague_women",
        "liga_acb", "lnb_elite", "bbl", "serie_a", "greek_basket_league",
        "lf_endesa", "lfb", "wnbl",
        "cba", "b_league", "kbl", "nbl", "bsl", "bal", "wcba", "wjbl",
        "nbb", "lnb_argentina", "lnbp", "lbf", "lfb_argentina"
    }
    return [
        team for team in load_teams_csv()
        if team.get("league_id") in seed_leagues
    ]


def test_schema_locked():
    """Test that the shared desk columns are present."""
    teams = load_teams_csv()

    if not teams:
        raise TestFailure("teams.csv is empty")

    actual_columns = list(teams[0].keys())
    if actual_columns != EXPECTED_COLUMNS:
        raise TestFailure(
            f"Schema mismatch.\nExpected: {EXPECTED_COLUMNS}\nGot: {actual_columns}"
        )

    print(f"✓ Schema locked ({len(EXPECTED_COLUMNS)} columns)")


def test_row_counts():
    """Test that the shared desk still has every league."""
    teams = load_teams_csv()
    counts = {}
    for team in teams:
        counts[team["league_id"]] = counts.get(team["league_id"], 0) + 1

    expected = {
        "nba": EXPECTED_NBA,
        "wnba": EXPECTED_WNBA,
        "euroleague": EXPECTED_EUROLEAGUE_MEN,
        "euroleague_women": EXPECTED_EUROLEAGUE_WOMEN_WITH_QIDS,
        "liga_acb": EXPECTED_LIGA_ACB,
        "lnb_elite": EXPECTED_LNB_ELITE,
        "bbl": EXPECTED_BBL,
        "serie_a": EXPECTED_SERIE_A,
        "greek_basket_league": EXPECTED_GREEK_BASKET_LEAGUE,
        "lf_endesa": EXPECTED_LF_ENDESA,
        "lfb": EXPECTED_LFB,
        "wnbl": EXPECTED_WNBL,
        "cba": EXPECTED_CBA,
        "b_league": EXPECTED_B_LEAGUE,
        "kbl": EXPECTED_KBL,
        "nbl": EXPECTED_NBL,
        "bsl": EXPECTED_BSL,
        "bal": EXPECTED_BAL,
        "wcba": EXPECTED_WCBA,
        "wjbl": EXPECTED_WJBL,
        "nbb": EXPECTED_NBB,
        "lnb_argentina": EXPECTED_LNB_ARGENTINA,
        "lnbp": EXPECTED_LNBP,
        "lbf": EXPECTED_LBF,
        "lfb_argentina": EXPECTED_LFB_ARGENTINA,
    }
    if len(teams) != EXPECTED_TOTAL:
        raise TestFailure(f"Total row count mismatch. Expected {EXPECTED_TOTAL}, got {len(teams)}")
    for league_id, count in expected.items():
        if counts.get(league_id) != count:
            raise TestFailure(f"{league_id} count mismatch. Expected {count}, got {counts.get(league_id)}")

    print(f"✓ Row counts match ({EXPECTED_TOTAL} teams)")


def test_gaps_documented():
    """Test that gap teams are documented (not in CSV)."""
    seed = load_seed()
    
    gap_teams = []
    for league in seed.get("leagues", []):
        for team in league.get("teams", []):
            if team.get("status") == "gap":
                gap_teams.append(team.get("team_id"))
    
    if len(gap_teams) != 44:
        raise TestFailure(
            f"Expected 44 gap teams in seed (2 EuroLeague Women + 7 LF Endesa + 2 LFB + 7 WCBA + 1 NBB + 9 LBF + 16 LFB Argentina), found {len(gap_teams)}"
        )
    
    # Verify gap teams are NOT in CSV
    teams = load_teams_csv()
    csv_team_ids = {t["team_id"] for t in teams}
    
    for gap_team_id in gap_teams:
        if gap_team_id in csv_team_ids:
            raise TestFailure(f"Gap team {gap_team_id} should not be in CSV")
    
    print(f"✓ Gap teams documented: {', '.join(gap_teams)}")


def test_required_fields():
    """Test that required fields are populated on EuroLeague rows."""
    teams = euroleague_rows()

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


def test_data_integrity():
    """Test data integrity (valid values) for EuroLeague rows."""
    teams = euroleague_rows()

    for team in teams:
        team_id = team["team_id"]

        confidence = team["confidence"].lower()
        if confidence not in VALID_CONFIDENCE:
            raise TestFailure(f"Invalid confidence for {team_id}: {team['confidence']}")
        
        # Country code must be valid (or empty)
        if team["country"] and team["country"] not in VALID_COUNTRY_CODES:
            raise TestFailure(f"Invalid country code for {team_id}: {team['country']}")
        
        # QID must start with Q
        qid = team["wikidata_qid"]
        if not qid.startswith("Q"):
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
    
    expected_leagues = {
        "nba": EXPECTED_NBA,
        "wnba": EXPECTED_WNBA,
        "euroleague": EXPECTED_EUROLEAGUE_MEN,
        "euroleague_women": EXPECTED_EUROLEAGUE_WOMEN_WITH_QIDS,
        "liga_acb": EXPECTED_LIGA_ACB,
        "lnb_elite": EXPECTED_LNB_ELITE,
        "bbl": EXPECTED_BBL,
        "serie_a": EXPECTED_SERIE_A,
        "greek_basket_league": EXPECTED_GREEK_BASKET_LEAGUE,
        "lf_endesa": EXPECTED_LF_ENDESA,
        "lfb": EXPECTED_LFB,
        "wnbl": EXPECTED_WNBL,
        "cba": EXPECTED_CBA,
        "b_league": EXPECTED_B_LEAGUE,
        "kbl": EXPECTED_KBL,
        "nbl": EXPECTED_NBL,
        "bsl": EXPECTED_BSL,
        "bal": EXPECTED_BAL,
        "wcba": EXPECTED_WCBA,
        "wjbl": EXPECTED_WJBL,
        "nbb": EXPECTED_NBB,
        "lnb_argentina": EXPECTED_LNB_ARGENTINA,
        "lnbp": EXPECTED_LNBP,
        "lbf": EXPECTED_LBF,
        "lfb_argentina": EXPECTED_LFB_ARGENTINA,
    }
    
    for league_id, expected_count in expected_leagues.items():
        if league_id not in league_counts:
            raise TestFailure(f"No teams found for league_id '{league_id}'")
        
        if league_counts[league_id] != expected_count:
            raise TestFailure(
                f"Expected {expected_count} {league_id} teams, "
                f"got {league_counts[league_id]}"
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
