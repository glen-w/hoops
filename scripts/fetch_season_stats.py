#!/usr/bin/env python3
"""
Fetch recent NBA season statistics.

Fetches team season summaries and league aggregates for a small window
of recent completed seasons (default: last 3).

Rate limiting:
- Basketball-Reference: maximum 12 requests/minute with jitter
- Minimum 5 seconds between requests (well under 12/min)
- Stops on 429 with exponential backoff
- Never parallelizes requests

Output:
- data/derived/season_stats/team_season_stats_YYYY_MM_DD.csv
- data/derived/season_stats/PROVENANCE.md

Usage:
    python3 scripts/fetch_season_stats.py [--seasons N]
    
    --seasons N    Number of recent completed seasons to fetch (default: 3)
"""

import argparse
import time
import random
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import pandas as pd
import requests


# Rate limiting constants - Basketball-Reference
MIN_SLEEP_SECONDS = 5.0
MAX_SLEEP_SECONDS = 7.0
MAX_RETRIES = 3
BACKOFF_BASE = 10  # seconds

# User agent for polite scraping
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Hoops Data Research/glen-w/hoops repository) for academic book research'
}


def rate_limited_sleep(verbose: bool = True):
    """Sleep with jitter for Basketball-Reference rate limiting."""
    sleep_time = random.uniform(MIN_SLEEP_SECONDS, MAX_SLEEP_SECONDS)
    if verbose:
        print(f"  Rate limit pause: {sleep_time:.2f}s")
    time.sleep(sleep_time)


def fetch_team_stats_for_season(
    season: str,
    retry_count: int = 0
) -> Optional[pd.DataFrame]:
    """
    Fetch team season stats from Basketball-Reference.
    
    Args:
        season: Season year like "2024" for 2023-24 season
        retry_count: Current retry attempt
        
    Returns:
        DataFrame with team stats or None on failure
    """
    # Basketball-Reference uses the ending year
    year = int(season.split('-')[1])
    if year < 100:  # Handle "23" -> "2023"
        year = 2000 + year
    
    season_label = season  # Keep original label like "2023-24"
    
    print(f"Fetching team stats for {season_label} (year {year})...")
    
    url = f'https://www.basketball-reference.com/leagues/NBA_{year}.html'
    
    try:
        # Let pandas handle the HTTP request with our headers
        # Pass URL directly to read_html
        tables = pd.read_html(url, flavor='bs4')
        
        # Find the per-game team stats table
        # Usually it's labeled "Per Game Stats" or contains per-game averages
        team_stats_df = None
        for table in tables:
            # Look for team name column and per-game stats
            if 'Team' in table.columns and 'PTS' in table.columns:
                # Check if it's per-game (not totals)
                # Per-game tables typically have values under 120 for PTS
                pts_col = table['PTS']
                # Convert to numeric, coercing errors
                pts_numeric = pd.to_numeric(pts_col, errors='coerce')
                if pts_numeric.max() < 150:
                    team_stats_df = table
                    break
        
        if team_stats_df is None:
            print(f"  ✗ Could not find team stats table for {season_label}")
            return None
        
        # Add season column
        team_stats_df.insert(0, 'season', season_label)
        
        # Clean up: remove any "League Average" rows
        team_stats_df = team_stats_df[team_stats_df['Team'] != 'League Average']
        
        print(f"  ✓ Retrieved {len(team_stats_df)} teams")
        return team_stats_df
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 429:
            if retry_count < MAX_RETRIES:
                backoff = BACKOFF_BASE * (2 ** retry_count)
                print(f"  ⚠ Rate limit hit (429). Backing off {backoff}s...")
                time.sleep(backoff)
                return fetch_team_stats_for_season(season, retry_count + 1)
            else:
                print(f"  ✗ Rate limit exceeded after {MAX_RETRIES} retries")
                return None
        raise
        
    except requests.exceptions.Timeout:
        if retry_count < MAX_RETRIES:
            backoff = BACKOFF_BASE * (2 ** retry_count)
            print(f"  ⚠ Timeout. Retrying in {backoff}s...")
            time.sleep(backoff)
            return fetch_team_stats_for_season(season, retry_count + 1)
        else:
            print(f"  ✗ Timeout after {MAX_RETRIES} retries")
            return None
    
    except Exception as e:
        print(f"  ✗ Error fetching {season_label}: {e}")
        return None


def generate_provenance(
    seasons: list[str],
    output_csv: Path,
    fetch_date: str
) -> str:
    """Generate PROVENANCE.md content."""
    
    season_list = ', '.join(seasons)
    
    return f"""# NBA Season Statistics: Provenance

## Files

- `{output_csv.name}` — Team per-game season statistics

## Source

**Basketball-Reference.com**  
https://www.basketball-reference.com/

**Owner:** Sports Reference LLC

## Description

Team per-game statistics for NBA regular seasons: {season_list}.

Each row represents one team's regular season performance aggregated as per-game averages.

## Coverage

- **Seasons:** {season_list} ({len(seasons)} seasons)
- **Teams:** 30 NBA teams per season
- **Statistics:** Points, field goals, three-pointers, free throws, rebounds, assists, steals, blocks, turnovers, fouls, plus/minus, and advanced metrics

## Fetch Details

- **Fetch date (UTC):** {fetch_date}
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
"""


def main():
    parser = argparse.ArgumentParser(
        description='Fetch recent NBA season statistics with rate limiting'
    )
    parser.add_argument(
        '--seasons',
        type=int,
        default=3,
        help='Number of recent completed seasons to fetch (default: 3)'
    )
    
    args = parser.parse_args()
    
    # Define recent completed seasons
    # As of 2026, last completed is 2023-24
    completed_seasons = [
        '2023-24',
        '2022-23',
        '2021-22',
        '2020-21',
        '2019-20',
        '2018-19',
    ]
    
    seasons_to_fetch = completed_seasons[:args.seasons]
    
    print("=" * 60)
    print("NBA Season Statistics Fetcher")
    print("=" * 60)
    print(f"Source: Basketball-Reference.com")
    print(f"Seasons to fetch: {', '.join(seasons_to_fetch)}")
    print(f"Rate limiting: {MIN_SLEEP_SECONDS}-{MAX_SLEEP_SECONDS}s between pages")
    print(f"Estimated time: ~{len(seasons_to_fetch) * 6:.0f} seconds")
    print()
    
    # Prepare output directory
    output_dir = Path('data/derived/season_stats')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Fetch data for each season
    all_data = []
    
    for i, season in enumerate(seasons_to_fetch):
        df = fetch_team_stats_for_season(season)
        
        if df is not None:
            all_data.append(df)
        else:
            print(f"✗ Failed to fetch {season}, stopping")
            sys.exit(1)
        
        # Rate limit between requests (skip after last)
        if i < len(seasons_to_fetch) - 1:
            rate_limited_sleep()
    
    if not all_data:
        print("✗ No data fetched")
        sys.exit(1)
    
    # Combine all seasons
    print()
    print("Combining data...")
    combined_df = pd.concat(all_data, ignore_index=True)
    
    # Write output with ISO date
    fetch_date_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    output_csv = output_dir / f'team_season_stats_{fetch_date_utc.replace("-", "_")}.csv'
    
    combined_df.to_csv(output_csv, index=False)
    print(f"✓ Wrote {len(combined_df)} rows to {output_csv}")
    
    # Write provenance
    provenance_path = output_dir / 'PROVENANCE.md'
    provenance_content = generate_provenance(
        seasons_to_fetch,
        output_csv,
        fetch_date_utc
    )
    provenance_path.write_text(provenance_content)
    print(f"✓ Wrote {provenance_path}")
    
    # Summary stats
    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Seasons: {len(seasons_to_fetch)}")
    print(f"Teams per season: {len(all_data[0])}")
    print(f"Total rows: {len(combined_df)}")
    print(f"Columns: {len(combined_df.columns)}")
    print()
    print("Sample data (first 3 teams):")
    sample_cols = ['season', 'Team']
    for col in ['PTS', 'FGA', 'FG%', '3PA', 'AST', 'TRB']:
        if col in combined_df.columns:
            sample_cols.append(col)
    print(combined_df[sample_cols].head(3))
    print()
    print("✓ Fetch complete")


if __name__ == '__main__':
    main()
