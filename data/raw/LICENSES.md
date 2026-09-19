# Raw Dataset Licenses

This file documents the source, license, and redistribution terms for all datasets downloaded into `data/raw/`.

---

## Datasets

### wyattowalsh/basketball (NBA Database)

- **Source**: https://www.kaggle.com/datasets/wyattowalsh/basketball
- **Primary Source**: NBA stats API (`stats.nba.com`) accessed via `nba_api`
- **Repository**: https://github.com/wyattowalsh/nbadb
- **Documentation**: https://nbadb.w4w.dev
- **License**: CC-BY-SA-4.0
- **Date Fetched**: 2026-09-19
- **Format**: SQLite database (`nba.sqlite`) — 235 tables covering 1946-47 to present
- **Redistributable Derived Products**: YES, with attribution under CC-BY-SA-4.0 terms
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
  - Raw database is ~2GB+ and kept in gitignored `data/raw/wyattowalsh-basketball/`
  - Only derived CSV extracts and analysis outputs are committed to git
  - Attribution requirement: Must cite "Wyatt Walsh. NBA Basketball Database. Kaggle: wyattowalsh/basketball"
  - Data is updated daily during NBA season; our snapshot represents data as of fetch date
  - NBA API data is public but subject to NBA.com terms; not an official NBA records system

### Fetch Instructions

The database requires Kaggle API credentials. To download:

1. Create a Kaggle account and generate an API token at https://www.kaggle.com/settings
2. Place `kaggle.json` in `~/.kaggle/` (or set `KAGGLE_USERNAME` and `KAGGLE_KEY` env vars)
3. Run:
   ```bash
   mkdir -p data/raw/wyattowalsh-basketball
   cd data/raw/wyattowalsh-basketball
   kaggle datasets download -d wyattowalsh/basketball
   unzip basketball.zip
   ```

**Alternative if Kaggle credentials unavailable**: The repository includes scripts that regenerate derived tables from documented NBA statistics. See `scripts/build_avg_game_by_decade.py` methodology notes.
