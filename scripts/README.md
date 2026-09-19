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

## Optional/Future: Kaggle Basketball Dataset

The `fetch_basketball_data.py` script can download the wyattowalsh/basketball dataset for future detailed analysis. **Currently optional** - not required until box-score level transforms are needed.

### Prerequisites

1. Create a Kaggle account at https://www.kaggle.com
2. Generate API credentials:
   - Go to Account → Settings → API
   - Click "Create New Token"
   - Save `kaggle.json` to `~/.kaggle/kaggle.json`
   - Run `chmod 600 ~/.kaggle/kaggle.json`

### Usage

```bash
# When needed: download wyattowalsh/basketball to data/raw/basketball/
uv run python scripts/fetch_basketball_data.py
```

**Status:** Documented for later use. See `data/raw/LICENSES.md` for license terms.

## Generating Derived Tables

Transform scripts (e.g., `generate_avg_game.py`) will be added by engineer in separate PR.

## Data Flow

```
Optional Raw (gitignored)     Scripts              Derived (committed)
─────────────────────────     ───────              ───────────────────
data/raw/basketball/      →   generate_*.py    →   data/derived/*.csv
                                                    data/derived/*.md
```

Raw data is **never committed** - see `data/raw/LICENSES.md` for all source provenance.

## Available Scripts

- `fetch_basketball_data.py` - Download wyattowalsh/basketball from Kaggle
- `generate_avg_game.py` - Generate per-decade average game statistics (smoke test)

## Data Flow

```
Raw (gitignored)          Scripts              Derived (committed)
─────────────────         ───────              ───────────────────
data/raw/basketball/  →   generate_*.py    →   data/derived/*.csv
                                                data/derived/*.md
```

## Notes

- Raw data is **never committed** - see `data/raw/LICENSES.md` for provenance
- Derived tables must credit source datasets
- Scripts are intentionally simple (pandas + documented CLI)
- No web app, no NBA tracking warehouse
