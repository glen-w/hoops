# Hoops Data Scripts

Data fetching and transformation scripts for the *Hoops* manuscript.

## Setup

Install dependencies using `uv`:

```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install project dependencies
uv sync
```

## Available Scripts

### `build_avg_game_by_decade.py` ✅ Ready

Generate average game statistics by decade from NBA season data.

**No Kaggle required** - uses committed Basketball-Reference data.

```bash
uv run python scripts/build_avg_game_by_decade.py
```

**Input:** `data/reference/nba_league_averages_by_season.csv` (committed)  
**Output:** `data/derived/avg_game_by_decade.csv`  
**Methodology:** `data/derived/avg_game_by_decade_methodology.md`

**What it does:**
1. Loads season-level league averages (1979-80 through 2023-24)
2. Groups seasons by decade
3. Calculates mean statistics per decade
4. Writes CSV with decade-level averages

**Status:** ✅ Ready - no API calls, no credentials needed

---

### `fetch_basketball_data.py` ⏸ Optional

Download the wyattowalsh/basketball dataset from Kaggle for future detailed analysis.

**Currently optional** - not required for any committed derived tables.

#### Prerequisites

1. Create a Kaggle account at https://www.kaggle.com
2. Generate API credentials:
   - Go to Account → Settings → API
   - Click "Create New Token"
   - Save `kaggle.json` to `~/.kaggle/kaggle.json`
   - Run `chmod 600 ~/.kaggle/kaggle.json`

#### Usage

```bash
# When needed: download wyattowalsh/basketball to data/raw/basketball/
uv run python scripts/fetch_basketball_data.py
```

**Status:** ⏸ Documented for later use. See `data/raw/LICENSES.md` for license terms.

---

## Data Flow

```
Reference (committed)         Scripts                 Derived (committed)
─────────────────────         ───────                 ───────────────────
data/reference/           →   build_*.py          →   data/derived/*.csv
  season_data.csv                                      data/derived/*.md

Optional Raw (gitignored)     Scripts                 (Future use)
─────────────────────────     ───────                 ────────────
data/raw/basketball/      →   fetch_*.py          →   (box-score analysis)
```

## No Kaggle Required for Current Artifacts

The `avg_game_by_decade` table is built from committed source data (`data/reference/`), **not** from Kaggle downloads. The `fetch_basketball_data.py` script is documented for potential future use (e.g., per-position analysis, detailed box scores), but is not needed for any current derived table.

## Adding New Transform Scripts

When adding a new derived table:

1. **Source data:**
   - Prefer small, redistributable CSVs in `data/reference/` (with citation)
   - Use `data/raw/` (gitignored) only for bulky datasets
   
2. **Script naming:** `build_<artifact_name>.py`

3. **Output:**
   - Write to `data/derived/<artifact_name>.csv`
   - Include `data/derived/<artifact_name>_methodology.md`

4. **Documentation:**
   - Update this README
   - Add entry to `CHAPTER-MAP.md`
   - Update `data/mentions.csv` if manuscript-referenced

5. **Dependencies:**
   - Add to `pyproject.toml` dependencies
   - Run `uv sync` to update lockfile
   - Keep scripts simple (pandas + documented CLI)

## Design Principles

- **Reproducibility:** Any derived table can be regenerated from source
- **Transparency:** Methodology documented alongside output
- **Simplicity:** Scripts are intentionally simple (pandas + CLI)
- **Attribution:** All sources credited in LICENSES.md or SOURCE_CITATION.md
- **No secrets in CI:** Prefer public APIs or committed source data

## Notes

- **Raw data** (`data/raw/`) is **never committed** - see `data/raw/LICENSES.md` for provenance
- **Reference data** (`data/reference/`) contains small, redistributable source CSVs
- **Derived tables** (`data/derived/`) must credit source datasets
- **No web app, no tracking warehouse** - this is a manuscript sidecar, not a platform

---

**Last Updated:** 2024-09-19  
**See Also:** `CHAPTER-MAP.md`, `data/raw/LICENSES.md`, `ROADMAP.md`
