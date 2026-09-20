#!/usr/bin/env python3
"""Join each team to the desks that already exist. Paths only; no copied stats."""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEAMS = ROOT / "data" / "derived" / "teams" / "teams.csv"
ORGS = ROOT / "data" / "derived" / "nba_orgs"
OUT = ROOT / "data" / "derived" / "franchise_bundle.csv"

NBA_CBA = "data/cba/2023/derived/structure.json (cba:2023:art-VII); data/cba/2023/derived/headings_index.json"
INCOME = "data/derived/league_income_ingredients.csv"

COLUMNS = [
    "team_id",
    "league_id",
    "name",
    "org_chart",
    "cba_articles",
    "income_ingredients",
    "bundle_status",
    "notes",
]


def org_path(row: dict) -> str:
    if row["league_id"] != "nba":
        return ""
    slug = (row.get("wikipedia_en") or row["name"]).lower().replace(" ", "-")
    path = ORGS / f"{slug}.csv"
    if not path.exists():
        raise SystemExit(f"No org chart for {row['team_id']} (looked for {path.name})")
    return str(path.relative_to(ROOT))


def main() -> int:
    rows = list(csv.DictReader(TEAMS.open(encoding="utf-8")))
    out_rows = []
    for row in rows:
        chart = org_path(row)
        nba = row["league_id"] == "nba"
        out_rows.append({
            "team_id": row["team_id"],
            "league_id": row["league_id"],
            "name": row["name"],
            "org_chart": chart,
            "cba_articles": NBA_CBA if nba else "",
            "income_ingredients": INCOME if nba else "",
            "bundle_status": "ready" if chart else "partial",
            "notes": "" if chart else "No org chart. Do not invent staff, colors, or owners.",
        })
    with OUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(out_rows)
    ready = sum(1 for row in out_rows if row["bundle_status"] == "ready")
    print(f"Wrote {OUT} ({len(out_rows)} teams, {ready} with org charts)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
