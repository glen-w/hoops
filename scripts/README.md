# Hoops Data Scripts

Data fetching and transformation scripts for the Hoops manuscript. This project uses [uv](https://github.com/astral-sh/uv).

```bash
uv sync
```

## Running Scripts

### Smoke Test

```bash
uv run python scripts/smoke_derived.py
```

Creates `data/derived/smoke_placeholder.csv` and confirms the pipeline layout.

### Build Average Game by Decade

Regenerate decade averages from the committed Basketball-Reference season file. No Kaggle credentials and no API calls.

```bash
uv run python scripts/build_avg_game_by_decade.py
```

- **Input:** `data/reference/nba_league_averages_by_season.csv` (1979-80 through 2023-24)
- **Output:** `data/derived/avg_game_by_decade.csv`
- **Methodology:** `data/derived/avg_game_by_decade_methodology.md`

The script loads season-level league averages, groups them by decade, and writes the mean of each stat.

### Validate NBA org charts

```bash
python3 scripts/validate_nba_orgs.py
```

Checks locked column order and the role vocabulary for every CSV in `data/derived/nba_orgs/`.

## Data Layout

- **`data/reference/`** — Small, redistributable source CSVs that derived tables are built from (committed).
- **`data/raw/`** — Bulky downloads (gitignored). Document license and fetch date in `data/raw/LICENSES.md` before fetching.
- **`data/derived/`** — Processed tables (committed). Each artifact should point back to its source.

Current decade table does not need a Kaggle download. `fetch_basketball_data.py` is only for later box-score or per-position work.

## Optional: wyattowalsh/basketball

```bash
# Shell wrapper → data/raw/wyattowalsh-basketball/
bash scripts/fetch_wyattowalsh.sh

# Python fetcher → data/raw/basketball/
uv run python scripts/fetch_basketball_data.py
```

Prerequisites: a Kaggle API token at `~/.kaggle/kaggle.json` (`chmod 600`). See `data/raw/LICENSES.md`.

## Adding a derived table

1. Prefer a small cited CSV in `data/reference/`. Use gitignored `data/raw/` only for bulky datasets.
2. Name the script `build_<artifact>.py` and write `data/derived/<artifact>.csv` plus a methodology note.
3. Update this README, `docs/CHAPTER-MAP.md`, and `data/mentions.csv` if the manuscript cites it.
4. Add any new dependency to `pyproject.toml` and run `uv lock`.
