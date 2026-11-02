# coder-02 — "Grokbot parquet unlock"

Night: 2026-10-28. Status: **partly done / needs Glen**.

## What I checked (read-only)

- **Glen's Mac** (`/Users/89298/Desktop/research <> research/`, recursively): **no `.parquet` files**. `grokbot_outputs/` held only `.processed/`, which I did not touch.
- **Box** (`/workspace`): only `/workspace/nightshift/2026-10-22-overtime/work/*.parquet`, which holds player and free-throw data from the 22 Oct overtime night. **Nothing on arenas or financing.**
- No credentials, shared drives or access were assumed or created. I could not identify what "unlock" refers to (a locked or encrypted file, a permission, or a dataset to be produced). No access was invented.

## What I delivered instead

These are parquet versions of tonight's data, written with pyarrow 26.0.0 (snappy). Row and column counts match the CSVs:

| File | Rows | Cols |
|---|---|---|
| 2026-10-28_coder-01_nba-arena-capex-2000-2026.parquet | 30 | 14 |
| 2026-10-28_coder-03_arena-operator-debt-equity.parquet | 25 | 16 |
| 2026-10-28_coder-03_sec-xbrl-debt-capex-series.parquet | 273 | 10 |
| 2026-10-28_researcher-01_aac-financing-timeline.parquet | 12 | 7 |

Load: `pd.read_parquet(path)` or `pyarrow.parquet.read_table(path)`. Money columns are int64 USD (nominal); blanks = unknown.

## Needs Glen

What is the "Grokbot parquet"? If it's a specific file (e.g. on another drive or in Paperful), tell me the path. If it's a permission/lock issue, I need to know which one. I will not try to bypass it.
