# Raw Dataset Licenses

This file documents the source, license, and redistribution terms for datasets that may be downloaded into `data/raw/`. Raw data files are not committed to this repository due to size and licensing constraints.

Currently, derived tables are generated from public records (Basketball-Reference, NBA.com) and public APIs (`nba_api`) without requiring a local raw dump. The bulky dataset below is documented for later use.

---

## Datasets

### wyattowalsh/basketball (NBA Database)

- **Source**: https://www.kaggle.com/datasets/wyattowalsh/basketball
- **Primary Source**: NBA stats API (`stats.nba.com`) accessed via `nba_api`
- **Repository**: https://github.com/wyattowalsh/nbadb
- **Documentation**: https://nbadb.w4w.dev
- **Author**: Wyatt Walsh
- **License**: [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- **Status**: Optional — not required for current derived tables. Phase later: blocked on Kaggle credentials.
- **Date documented**: 2026-09-19
- **Format**: SQLite database (`nba.sqlite`) — 235 tables covering 1946-47 to present
- **Redistributable Derived Products**: YES, with attribution under CC-BY-SA-4.0 terms. The raw database itself is not redistributed.
- **Content**: Comprehensive NBA warehouse including:
  - 65,000+ games (every game since 1946-47)
  - 4,800+ players
  - Box scores (traditional, advanced, hustle, tracking)
  - Play-by-play (13M+ events)
  - Shot charts with court coordinates
  - Team/player season aggregates
  - Draft history and combine measurements
  - Standings, awards, and matchup history

- **Notes**:
  - Raw database is ~2GB+ and kept in gitignored `data/raw/`
  - Only derived CSV extracts and analysis outputs are committed to git
  - Attribution requirement: Must cite "Wyatt Walsh. NBA Basketball Database. Kaggle: wyattowalsh/basketball"
  - Data is updated daily during NBA season; a snapshot represents data as of the fetch date
  - NBA API data is public but subject to NBA.com terms; not an official NBA records system

### Fetch Instructions

The database requires Kaggle API credentials. Two fetch paths are available:

```bash
# Shell wrapper (writes to data/raw/wyattowalsh-basketball/)
bash scripts/fetch_wyattowalsh.sh

# Python fetcher (writes to data/raw/basketball/)
uv run python scripts/fetch_basketball_data.py
```

1. Create a Kaggle account and generate an API token at https://www.kaggle.com/settings
2. Place `kaggle.json` in `~/.kaggle/` (or set `KAGGLE_USERNAME` and `KAGGLE_KEY` env vars)
3. `chmod 600 ~/.kaggle/kaggle.json`

If Kaggle credentials are unavailable, regenerate derived tables from documented NBA statistics. See `scripts/build_avg_game_by_decade.py`.

---

## Active Data Sources (API/Web-Based)

### nba_api

- **Source**: https://github.com/swar/nba_api
- **License**: MIT License
- **Status**: Available dependency; current decade table is compiled from published league averages rather than a live API pull
- **Description**: Python API client for NBA.com endpoints. Provides league-wide statistics, team data, and historical season averages.
- **Redistribution**: API data from NBA.com is public statistics. Derived aggregations may be committed with attribution to NBA.com and nba_api.

### Basketball-Reference.com

- **Source**: https://www.basketball-reference.com/
- **License**: Public statistics (cite, don't scrape aggressively)
- **Status**: Active — used for historical league averages
- **Description**: Comprehensive basketball statistics archive maintained by Sports Reference LLC.
- **Redistribution**: Season-level aggregates may be redistributed with attribution to Basketball-Reference.com.

---

## Additional Future Sources (Not Yet Downloaded)

### DeepSportRadar v1

- **Source**: https://paperswithcode.com/dataset/deepsportradar-v1
- **Status**: Under consideration for tracking-style analysis
- **Notes**: Only download if the manuscript needs tracking-data samples

### Data.world Basketball Catalog

- **Source**: https://data.world/datasets/basketball
- **Status**: Exploratory — alternative box score sources
- **Notes**: License terms vary by dataset

---

## License Compliance Notes

1. **Storage:** Raw data files stay in `data/raw/` (gitignored, except this file and `.gitkeep`)
2. **Commits:** Only derived/aggregated tables go into `data/derived/`
3. **Attribution:** All derived tables must credit source datasets
4. **Proprietary Data:** No NBA tracking feeds (SportVU, Second Spectrum, Hawk-Eye) — narrative citations only
5. **Studies:** Paper notes live under `data/studies/`; do not rehost copyrighted papers

---

**Last Updated:** 2026-09-19
