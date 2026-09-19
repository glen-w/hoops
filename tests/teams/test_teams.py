"""
Tests for teams data pipeline.

Validates schema compliance and data quality for NBA/WNBA teams.
"""

import pandas as pd
import pytest
from pathlib import Path


REPO_ROOT = Path(__file__).parent.parent.parent


def test_teams_csv_exists():
    """Verify teams.csv exists in expected location."""
    teams_csv = REPO_ROOT / "data" / "derived" / "teams" / "teams.csv"
    assert teams_csv.exists(), f"Expected teams.csv at {teams_csv}"


def test_teams_schema():
    """Verify teams.csv has required columns."""
    teams_csv = REPO_ROOT / "data" / "derived" / "teams" / "teams.csv"
    
    if not teams_csv.exists():
        pytest.skip("teams.csv not yet generated")
    
    df = pd.read_csv(teams_csv)
    
    required_columns = [
        "team_id",
        "league_id",
        "name",
        "short_name",
        "city",
        "country",
        "arena",
        "arena_capacity",
        "founded_year",
        "colours_primary_hex",
        "colours_secondary_hex",
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
    
    for col in required_columns:
        assert col in df.columns, f"Missing required column: {col}"


def test_lakers_row_shape():
    """
    Golden test: Validate Lakers row exists with expected structure.
    
    This test verifies a stable NBA franchise (Los Angeles Lakers)
    has a well-formed row with expected data shape.
    """
    teams_csv = REPO_ROOT / "data" / "derived" / "teams" / "teams.csv"
    
    if not teams_csv.exists():
        pytest.skip("teams.csv not yet generated")
    
    df = pd.read_csv(teams_csv)
    
    # Find Lakers row (multiple possible matches; check any)
    lakers = df[df["name"].str.contains("Lakers", case=False, na=False)]
    
    assert len(lakers) > 0, "Lakers not found in teams.csv"
    
    lakers_row = lakers.iloc[0]
    
    # Validate required fields are present
    assert lakers_row["league_id"] == "nba", "Lakers should be in NBA"
    assert pd.notna(lakers_row["name"]), "Lakers name should not be null"
    assert pd.notna(lakers_row["wikidata_qid"]), "Lakers Wikidata QID should be present"
    assert pd.notna(lakers_row["team_id"]), "team_id should be present"
    
    # Validate team_id format (should contain league_id)
    assert lakers_row["team_id"].startswith("nba_"), "team_id should start with league_id"
    
    # Validate confidence is valid enum
    assert lakers_row["confidence"] in ["HIGH", "MEDIUM", "LOW", "GAP"], \
        f"confidence must be HIGH/MEDIUM/LOW/GAP, got {lakers_row['confidence']}"
    
    # Validate as_of is ISO date format
    assert pd.notna(lakers_row["as_of"]), "as_of date should be present"
    pd.to_datetime(lakers_row["as_of"])  # Will raise if not valid date
    
    # Validate source_url is Wikidata
    assert lakers_row["source_url"].startswith("https://www.wikidata.org/wiki/"), \
        "source_url should be Wikidata URL"


def test_logos_csv_schema():
    """Verify logos.csv has required columns."""
    logos_csv = REPO_ROOT / "data" / "derived" / "teams" / "logos.csv"
    
    if not logos_csv.exists():
        pytest.skip("logos.csv not yet generated")
    
    df = pd.read_csv(logos_csv)
    
    required_columns = [
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
    
    for col in required_columns:
        assert col in df.columns, f"Missing required column: {col}"


def test_leagues_csv_schema():
    """Verify leagues.csv has required columns."""
    leagues_csv = REPO_ROOT / "data" / "derived" / "teams" / "leagues.csv"
    
    if not leagues_csv.exists():
        pytest.skip("leagues.csv not yet generated")
    
    df = pd.read_csv(leagues_csv)
    
    required_columns = [
        "league_id",
        "name",
        "gender",
        "tier",
        "country_or_region",
        "governing_body",
        "wikidata_qid",
        "wikipedia_en",
        "season_label",
        "as_of",
        "source_url",
        "confidence",
    ]
    
    for col in required_columns:
        assert col in df.columns, f"Missing required column: {col}"


def test_nba_league_present():
    """Verify NBA league is in leagues.csv."""
    leagues_csv = REPO_ROOT / "data" / "derived" / "teams" / "leagues.csv"
    
    if not leagues_csv.exists():
        pytest.skip("leagues.csv not yet generated")
    
    df = pd.read_csv(leagues_csv)
    
    nba = df[df["league_id"] == "nba"]
    assert len(nba) == 1, "NBA league should be present exactly once"
    
    nba_row = nba.iloc[0]
    assert nba_row["name"] == "National Basketball Association"
    assert nba_row["gender"] == "men"
    assert nba_row["tier"] == 1
    assert nba_row["wikidata_qid"] == "Q155223"


def test_wnba_league_present():
    """Verify WNBA league is in leagues.csv."""
    leagues_csv = REPO_ROOT / "data" / "derived" / "teams" / "leagues.csv"
    
    if not leagues_csv.exists():
        pytest.skip("leagues.csv not yet generated")
    
    df = pd.read_csv(leagues_csv)
    
    wnba = df[df["league_id"] == "wnba"]
    assert len(wnba) == 1, "WNBA league should be present exactly once"
    
    wnba_row = wnba.iloc[0]
    assert wnba_row["name"] == "Women's National Basketball Association"
    assert wnba_row["gender"] == "women"
    assert wnba_row["tier"] == 1
    assert wnba_row["wikidata_qid"] == "Q2593221"
