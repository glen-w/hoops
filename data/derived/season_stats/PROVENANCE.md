# NBA Season Statistics: Provenance

## Files

- `team_season_stats_2026_09_25.csv` — Team per-game season statistics

## Source

**Basketball-Reference.com**  
https://www.basketball-reference.com/

**Owner:** Sports Reference LLC

## Description

Team per-game statistics for NBA regular seasons: 2023-24, 2022-23, 2021-22.

Each row represents one team's regular season performance aggregated as per-game averages.

## Coverage

- **Seasons:** 2023-24, 2022-23, 2021-22 (3 seasons)
- **Teams:** 30 NBA teams per season
- **Statistics:** Points, field goals, three-pointers, free throws, rebounds, assists, steals, blocks, turnovers, fouls, plus/minus, and advanced metrics

## Fetch Details

- **Fetch date (UTC):** 2026-09-25
- **Script:** `scripts/fetch_season_stats.py`
- **Method:** HTML table scraping from Basketball-Reference season pages
- **Table:** Per Game Team Stats
- **Season type:** Regular Season

## Rate Limiting

This script enforces strict rate limiting to comply with Sports Reference bot policy:

- Minimum 5 seconds between page requests (well under 12 requests/minute)
- Random jitter up to 7 seconds
- Exponential backoff on 429 responses (10s, 20s, 40s)
- Never parallelizes requests
- Stops immediately on 429 and backs off

**Sports Reference bot policy:** Fewer than 20 requests/minute on Basketball-Reference. 
This script targets ~10 requests/minute maximum to maintain a safety margin.

## License and Redistribution Constraints

**IMPORTANT:** There is NO official Basketball-Reference / Sports Reference public API.

**Usage constraints:**
- Basketball-Reference data is scraped from public HTML pages
- Sports Reference LLC owns the data compilation
- This is cite-scrape only: cite the source, do NOT create wholesale mirrors
- Use for research, citation, and analysis only
- NOT for redistribution as a data product

**From repository policy (DATA-REPOS.md):**
- "Derive a table, cite the source, commit only what we may redistribute"
- "Package MIT ≠ data license"
- "No SportVU dumps, no full BRef archives"

This small 3-season team summary is a derived research table for the Hoops book project, 
not a redistributable archive.

## Method

1. Scrape Basketball-Reference HTML season page for each season
2. Parse per-game team stats table using pandas `read_html`
3. Extract regular season team averages only
4. Enforce rate limiting (≥5s per page, with jitter)
5. Combine seasons into single CSV with `season` column
6. Write with ISO fetch date in filename

## Validation

Cross-reference spot checks against:
- Basketball-Reference team pages
- Official NBA team stat leaders
- League-wide averages should match known published values

## Regenerate

```bash
cd /workspace
uv run python scripts/fetch_season_stats.py --seasons 3
```

Change `--seasons N` to fetch a different window of recent completed seasons.

## Related Files

- `data/derived/avg_game_by_decade/nba_league_averages_by_season.csv` — League-wide per-game averages by season (1946-2024)
- `data/derived/avg_game_by_decade/methodology.md` — Methodology for league average aggregates

---

**Repository:** glen-w/hoops  
**Purpose:** Research sidecar for *Hoops: An Uncommon Field Guide to Basketball*
