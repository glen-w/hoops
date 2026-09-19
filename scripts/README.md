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

## Data Layout

- **`data/raw/`** — Raw downloaded datasets (gitignored). Add source, license, and redistribution notes to `data/raw/LICENSES.md` before fetching new datasets.
- **`data/derived/`** — Processed tables and analysis outputs (committed to git). Each derived artifact should have clear provenance to its raw source(s).

## Adding New Datasets

1. Document the source, license, and fetch date in `data/raw/LICENSES.md`
2. Download raw data to `data/raw/<dataset-name>/`
3. Write a processing script under `scripts/` that reads from `data/raw/` and writes to `data/derived/`
4. Document the command to regenerate the derived output in this README
