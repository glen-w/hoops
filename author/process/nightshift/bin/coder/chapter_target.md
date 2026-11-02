# Chapter target: decade averages, CBA/income/teams

## Status (2026-10-20, final_tick)
- hoops_list `avg_game_by_decade`: 0 items.
- hoops_list `CBA income teams`: 0 items.
- hoops_summary on Basketball-Reference (WNKIH56T): no paperful summary (`sm: false`); only the Zotero abstract came back.
- No season-rows file has been located. No stat values are stated here, and none should be added until a real file is read.

## What the sources say (from ds abstracts only)
- Basketball-Reference (WNKIH56T): canonical historical NBA/ABA/WNBA tables (season, advanced, salaries pages). Scrape-friendly with etiquette, but not a bulk open-dump license. The abstract names it as the primary source for the glen-w/hoops `avg_game_by_decade` season rows.
- nba_api (9FJZPDKM): Python client for NBA.com Stats API. Rate-limit and ToS sensitive; do not redistribute raw dumps without checking the license.
- pbpstats (ASRNZRRW): Python play-by-play parsing, lineups, on/off from NBA Stats feeds.
- hoopR (NEGCDXKA): R package with ESPN loads and Basketball-Reference scrapers. `load_nba_pbp` covers multi-season ESPN PBP (~2002 on). KenPom needs a subscription.
- Barttorvik T-Rank CSVs (NVTWTCHG): free Division I team ratings and four factors (~2008 on), season-end CSVs. Open college path without KenPom.
- awesome-nba-data (CTJJ3N4H): curation index and terms matrix, not a license grant.

## Pipeline
1. `check_ds.py ROOT <paths>` on the six ds paths (not yet run; no disk access this pass).
2. Locate the `avg_game_by_decade` rows file under `paperful-out/hoops`.
3. `decade_table.py ROWS.csv SEASON_COL STAT_COL...` on that file only.
4. Cite the rows file path and the Basketball-Reference path in the chapter.

## Open
- CBA/income/teams: no hr path found yet. Try other keys (`salary`, `collective bargaining`, `franchise`) or list the folder directly.
- Chapter prose may cite source existence and scope only until rows are read.