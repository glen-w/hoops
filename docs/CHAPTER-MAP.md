# Chapter-to-Data Map

This document maps Scrivener binder paths to derived data artifacts, Zotero keys, and dataset status.

## Purpose

Track which data products support which sections of the manuscript, ensuring every table/figure reference has a clear pipeline back to sources documented in `data/raw/LICENSES.md` and cited in Zotero `hoops`.

## Map

| Binder Path | Derived Artifact | Zotero Key | Status |
|-------------|------------------|------------|--------|
| GAME TIME / average game | `data/derived/avg_game_by_decade.csv` | TBD | ready |
| STADIUM / home court advantage | `data/derived/home_court_2024_playoffs.md` | TBD | wanted |
| ANALYTICS / state of the data | `docs/SLOAN-ARCHIVE.md` + `docs/DATA-REPOS.md` + `docs/BASKETBALL-SOFTWARE.md` + `data/sloan/papers.jsonl` | TBD | ready |
| EXAMPLE: PLAYERS / height evolution | `data/derived/nba_height_series.csv` | TBD | EXAMPLE |
| EXAMPLE: TEAM / front office / efficiency | `data/derived/franchise_efficiency_2015_16.md` | TBD | EXAMPLE |

## Column Definitions

- **Binder Path**: Location in the Scrivener `.scriv` project
- **Derived Artifact**: File path under `data/derived/` that provides the table, figure, or dataset
- **Zotero Key**: Zotero item key(s) for primary citations; use comma-separated list if multiple
- **Status**: One of:
  - `wanted` — needed for the draft; not yet produced
  - `missing` — data source unknown or unavailable
  - `hold` — deferred until later phase or decision
  - `ready` — artifact exists and is current
  - `EXAMPLE` — placeholder row for demonstration

## Maintenance

Update this map whenever:
- A new derived artifact is committed
- A Scrivener section is restructured
- A data dependency changes or is resolved
