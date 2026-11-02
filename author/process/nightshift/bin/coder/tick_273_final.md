# Tick 273 final

Status: HR returned. Nothing usable for decade_means.py yet. No numbers invented.

## Foteinakis & Pavlidou 2025 (E7QXTIF7), hoops_summary excerpt
These are pooled whole-period league comparisons (NBA vs EuroLeague), quoted from the mirrored summary. They have no page or table reference and are not per-season. Do not put them in a per-season table.

- Games: 14,688 total = 12,150 NBA regular season + 2,538 EuroLeague (regular season plus top-16 rounds).
- Window: 2012-2013 to 2022-2023, with 2019-2020 excluded.
- 3PA/FGA%: EuroLeague 37.59, NBA 32.44.
- 3PA per 100 possessions: EuroLeague 32.79, NBA 27.94.
- 2PA per 100 possessions: NBA 58.29, EuroLeague 54.50.
- 2P%: EuroLeague 52.90, NBA 51.11.
- 3P%: EuroLeague 36.38, NBA 35.62.
- eFG%: EuroLeague 53.95, NBA 52.14.
- Data sources named in the summary: stats.nba.com and euroleague.net.
- Per-season values are not in the excerpt, which was truncated.

## Season count: unresolved
The summary says nine seasons. The stated window is 2012-13 through 2022-23, which is 11 seasons. Excluding 2019-20 leaves 10. Nine and ten do not match. The summary may be wrong, or the window may be wrong, or another season may be dropped. Settle it from the paper itself (methods text or the per-season table). Until then, do not state a season count in the chapter.

## Wang 2022 (NCQ6GJND)
hoops_record returned title and year only (abs empty). It has no table content, so the 163-177 question is still open. Is it per-team or league total, and attempts or makes? Mark it unresolved and do not use it. The next HR pass needs the paper's full text or notes, if the mirror has them.

## Basketball-Reference (WNKIH56T)
hoops_record is a catalog entry only. It has no table data. The note says it is scrape-friendly with etiquette and is not a bulk dump license. It is the source for the avg_game_by_decade season rows.

## Not done
- br_league_fetch.py was not run this tick. I cannot run code in this lane, so there is no URL or access date logged.
- decade_means.py was not written. It has no per-season inputs, and I will not fill them from memory.

## Rules for decade_means.py (unchanged)
- Table A (Foteinakis) and Table B (Wang) stay separate.
- mean_of_means and games_weighted are separate columns. Never substitute one for the other.
- Every row carries a source path and a page or table reference.
