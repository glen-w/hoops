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
| TEAM / Atlanta Hawks / front office | `data/derived/nba_orgs/atlanta-hawks.csv` | TBD | ready |
| TEAM / Boston Celtics / front office | `data/derived/nba_orgs/boston-celtics.csv` | TBD | ready |
| TEAM / Brooklyn Nets / front office | `data/derived/nba_orgs/brooklyn-nets.csv` | TBD | ready |
| TEAM / Charlotte Hornets / front office | `data/derived/nba_orgs/charlotte-hornets.csv` | TBD | ready |
| TEAM / Chicago Bulls / front office | `data/derived/nba_orgs/chicago-bulls.csv` | TBD | ready |
| TEAM / Cleveland Cavaliers / front office | `data/derived/nba_orgs/cleveland-cavaliers.csv` | TBD | ready |
| TEAM / Dallas Mavericks / front office | `data/derived/nba_orgs/dallas-mavericks.csv` | TBD | ready |
| TEAM / Denver Nuggets / front office | `data/derived/nba_orgs/denver-nuggets.csv` | TBD | ready |
| TEAM / Detroit Pistons / front office | `data/derived/nba_orgs/detroit-pistons.csv` | TBD | ready |
| TEAM / Golden State Warriors / front office | `data/derived/nba_orgs/golden-state-warriors.csv` | TBD | ready |
| TEAM / Houston Rockets / front office | `data/derived/nba_orgs/houston-rockets.csv` | TBD | ready |
| TEAM / Indiana Pacers / front office | `data/derived/nba_orgs/indiana-pacers.csv` | TBD | ready |
| TEAM / LA Clippers / front office | `data/derived/nba_orgs/la-clippers.csv` | TBD | ready |
| TEAM / Los Angeles Lakers / front office | `data/derived/nba_orgs/los-angeles-lakers.csv` | TBD | ready |
| TEAM / Memphis Grizzlies / front office | `data/derived/nba_orgs/memphis-grizzlies.csv` | TBD | ready |
| TEAM / Miami Heat / front office | `data/derived/nba_orgs/miami-heat.csv` | TBD | ready |
| TEAM / Milwaukee Bucks / front office | `data/derived/nba_orgs/milwaukee-bucks.csv` | TBD | ready |
| TEAM / Minnesota Timberwolves / front office | `data/derived/nba_orgs/minnesota-timberwolves.csv` | TBD | ready |
| TEAM / New Orleans Pelicans / front office | `data/derived/nba_orgs/new-orleans-pelicans.csv` | TBD | ready |
| TEAM / New York Knicks / front office | `data/derived/nba_orgs/new-york-knicks.csv` | TBD | ready |
| TEAM / Oklahoma City Thunder / front office | `data/derived/nba_orgs/oklahoma-city-thunder.csv` | TBD | ready |
| TEAM / Orlando Magic / front office | `data/derived/nba_orgs/orlando-magic.csv` | TBD | ready |
| TEAM / Philadelphia 76ers / front office | `data/derived/nba_orgs/philadelphia-76ers.csv` | TBD | ready |
| TEAM / Phoenix Suns / front office | `data/derived/nba_orgs/phoenix-suns.csv` | TBD | ready |
| TEAM / Portland Trail Blazers / front office | `data/derived/nba_orgs/portland-trail-blazers.csv` | TBD | ready |
| TEAM / Sacramento Kings / front office | `data/derived/nba_orgs/sacramento-kings.csv` | TBD | ready |
| TEAM / San Antonio Spurs / front office | `data/derived/nba_orgs/san-antonio-spurs.csv` | TBD | ready |
| TEAM / Toronto Raptors / front office | `data/derived/nba_orgs/toronto-raptors.csv` | TBD | ready |
| TEAM / Utah Jazz / front office | `data/derived/nba_orgs/utah-jazz.csv` | TBD | ready |
| TEAM / Washington Wizards / front office | `data/derived/nba_orgs/washington-wizards.csv` | TBD | ready |

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

## Notes

**NBA org-charts sparse sources:** TOR, CLE, MIL relied more on press releases + NBAstuffer vs. official staff directories; check row-level `confidence` + `as_of` when citing.

## CBA Reference (2023 NBA Collective Bargaining Agreement)

| Binder Path | Derived Artifact | Zotero Key | Status |
|-------------|------------------|------------|--------|
| CBA / Article I / Definitions | `data/cba/2023/derived/structure.json` + `data/cba/2023/derived/defined_terms.json` | TBD | ready |
| CBA / Article II / Uniform Player Contract | `data/cba/2023/derived/structure.json` (cba:2023:art-II, 15 sections) | TBD | ready |
| CBA / Article VII / Team Salary | `data/cba/2023/derived/structure.json` (cba:2023:art-VII, 12 sections) | TBD | ready |
| CBA / Article VII / Section 6 / Exceptions (MLE) | `data/cba/2023/derived/headings_index.json` (Mid-Level Exception subsections) | TBD | ready |
| CBA / Article X / Veteran Free Agents | `data/cba/2023/derived/structure.json` (cba:2023:art-X, 10 sections) | TBD | ready |
| CBA / Article XI / Rookie Scale | `data/cba/2023/derived/structure.json` (cba:2023:art-XI, 5 sections) | TBD | ready |
| CBA / Exhibits A-H, I-1 to I-7, J-1, J-2 | `data/cba/2023/derived/structure.json` (17 exhibits) | TBD | ready |
| CBA / Full spike documentation | `docs/cba/SPIKE-REPORT.md` (42 articles, 279 sections parsed) | TBD | ready |

**CBA provenance:**
- PDF SHA-256: `sha256:cf59d43fe46f63d7ba07364563046d766c487c26032fcc88432310d47effd9d9`
- Source: NBA Official 2023 Final (686 pages)
- Parser spike: `scripts/parse_cba_spike.py`
- **Copyright note:** PDF & full text remain gitignored (`data/raw/cba/.gitignore`); only structure metadata and ≤500-char previews committed
- **Engineer P0:** Productize parser under `src/hoops_data/cba/` (see SPIKE-REPORT §5)

## Maintenance

Update this map whenever:
- A new derived artifact is committed
- A Scrivener section is restructured
- A data dependency changes or is resolved
