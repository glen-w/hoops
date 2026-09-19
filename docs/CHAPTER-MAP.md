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
| TEAM / San Antonio Spurs / front office | `data/derived/nba_orgs/san-antonio-spurs.csv` | TBD | partial |
| TEAM / Denver Nuggets / front office | `data/derived/nba_orgs/denver-nuggets.csv` | TBD | partial |
| TEAM / Philadelphia 76ers / front office | `data/derived/nba_orgs/philadelphia-76ers.csv` | TBD | partial |
| TEAM / Atlanta Hawks / front office | `data/derived/nba_orgs/atlanta-hawks.csv` | TBD | partial |
| TEAM / Boston Celtics / front office | `data/derived/nba_orgs/boston-celtics.csv` | TBD | partial |
| TEAM / Brooklyn Nets / front office | `data/derived/nba_orgs/brooklyn-nets.csv` | TBD | partial |
| TEAM / Chicago Bulls / front office | `data/derived/nba_orgs/chicago-bulls.csv` | TBD | partial |
| TEAM / Cleveland Cavaliers / front office | `data/derived/nba_orgs/cleveland-cavaliers.csv` | TBD | partial |
| TEAM / Golden State Warriors / front office | `data/derived/nba_orgs/golden-state-warriors.csv` | TBD | partial |
| TEAM / Indiana Pacers / front office | `data/derived/nba_orgs/indiana-pacers.csv` | TBD | partial |
| TEAM / Miami Heat / front office | `data/derived/nba_orgs/miami-heat.csv` | TBD | partial |
| TEAM / Milwaukee Bucks / front office | `data/derived/nba_orgs/milwaukee-bucks.csv` | TBD | partial |
| TEAM / New Orleans Pelicans / front office | `data/derived/nba_orgs/new-orleans-pelicans.csv` | TBD | partial |
| TEAM / New York Knicks / front office | `data/derived/nba_orgs/new-york-knicks.csv` | TBD | partial |
| TEAM / Oklahoma City Thunder / front office | `data/derived/nba_orgs/oklahoma-city-thunder.csv` | TBD | partial |
| TEAM / Orlando Magic / front office | `data/derived/nba_orgs/orlando-magic.csv` | TBD | partial |
| TEAM / Portland Trail Blazers / front office | `data/derived/nba_orgs/portland-trail-blazers.csv` | TBD | partial |
| TEAM / Toronto Raptors / front office | `data/derived/nba_orgs/toronto-raptors.csv` | TBD | partial |
| TEAM / Washington Wizards / front office | `data/derived/nba_orgs/washington-wizards.csv` | TBD | partial |

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
