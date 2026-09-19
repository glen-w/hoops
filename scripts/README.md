# Hoops Data Scripts

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for Python package management.

Initialize the environment:

```bash
uv sync
```

## Running Scripts

### Smoke Test

Generate a placeholder derived table to verify the pipeline:

```bash
uv run python scripts/smoke_derived.py
```

This creates `data/derived/smoke_placeholder.csv` with sample data and confirms the data pipeline structure is working.

### Build Average Game by Decade

Generate per-decade NBA game statistics from published historical records:

```bash
uv run python scripts/build_avg_game_by_decade.py
```

This creates:
- `data/derived/avg_game_by_decade.csv` — per-decade averages for points, FG%, rebounds, assists, 3PT stats
- `data/derived/avg_game_by_decade.md` — full methodology note with sources and caveats

**Data source**: Compiled from Basketball-Reference.com and NBA.com official league averages (public records)

**Time to run**: < 1 second (uses compiled historical data)

**Output**: 9 decades (1940s-2020s) with per-team-per-game averages

### Validate NBA org charts

```bash
python3 scripts/validate_nba_orgs.py
```

Checks locked column order and the role vocabulary for every CSV in `data/derived/nba_orgs/`.

## Data Layout

- **`data/raw/`** — Raw downloaded datasets (gitignored). Add source, license, and redistribution notes to `data/raw/LICENSES.md` before fetching new datasets.
- **`data/derived/`** — Processed tables and analysis outputs (committed to git). Each derived artifact should have clear provenance to its raw source(s).

## Adding New Datasets

### Fetching wyattowalsh/basketball (optional)

The full NBA Database is optional and blocked until Kaggle API credentials are available. It is not required for the current derived tables.

```bash
# Shell wrapper → data/raw/wyattowalsh-basketball/
bash scripts/fetch_wyattowalsh.sh

# Python fetcher → data/raw/basketball/
uv run python scripts/fetch_basketball_data.py
```

**Prerequisites**:
1. Kaggle account: https://www.kaggle.com
2. API token: https://www.kaggle.com/settings → "Create New Token"
3. Place `kaggle.json` in `~/.kaggle/` with permissions `chmod 600 ~/.kaggle/kaggle.json`

See `data/raw/LICENSES.md` for license terms and attribution requirements.

### Adding Other Datasets

1. Document the source, license, and fetch date in `data/raw/LICENSES.md`
2. Download raw data to `data/raw/<dataset-name>/`
3. Write a processing script under `scripts/` that reads from `data/raw/` and writes to `data/derived/`
4. Document the command to regenerate the derived output in this README

Raw data is never committed. Derived tables must credit their sources.
