"""The desk lookup and the franchise bundle stay aligned with files on disk."""

import csv
from pathlib import Path

from hoops_data.ask import search

ROOT = Path(__file__).resolve().parents[1]


def test_ask_finds_celtics_org_chart():
    hits = search("Boston Celtics", ROOT)
    artifacts = [hit.artifact for hit in hits]
    assert any(path.endswith("boston-celtics.csv") for path in artifacts)


def test_ask_says_missing_when_nothing_matches():
    assert search("zzzz-not-a-desk", ROOT) == []


def test_ask_keeps_the_blazers_ticket_gap():
    hits = search("Blazers season tickets", ROOT)
    claim = next(hit for hit in hits if hit.kind == "claim")
    assert claim.confidence == "GAP"
    assert "$47M" in claim.sentence
    assert "Cite OregonLive" not in claim.sentence


def test_ask_reports_team_confidence():
    hits = search("Boston Celtics", ROOT)
    team = next(hit for hit in hits if hit.kind == "team")
    assert team.confidence == "HIGH"


def test_franchise_bundle_joins_every_nba_org_chart():
    bundle = ROOT / "data" / "derived" / "franchise_bundle.csv"
    rows = list(csv.DictReader(bundle.open(encoding="utf-8")))
    nba = [row for row in rows if row["league_id"] == "nba"]
    assert len(nba) == 30
    for row in nba:
        assert (ROOT / row["org_chart"]).exists()
        assert "cba:2023:art-VII" in row["cba_articles"]
        assert row["income_ingredients"].endswith("league_income_ingredients.csv")
    others = [row for row in rows if row["league_id"] != "nba"]
    assert others
    assert all(row["org_chart"] == "" for row in others)


def test_liga_acb_is_a_league_row_without_invented_clubs():
    leagues = list(csv.DictReader((ROOT / "data/derived/teams/leagues.csv").open()))
    acb = [row for row in leagues if row["league_id"] == "liga_acb"]
    assert len(acb) == 1
    assert acb[0]["wikidata_qid"] == "Q324867"
    teams = list(csv.DictReader((ROOT / "data/derived/teams/teams.csv").open()))
    assert not any(row["league_id"] == "liga_acb" for row in teams)
