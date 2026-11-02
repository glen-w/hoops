# decade_means status

Tick 2026-10-19 (final_tick).

## Result
No values computed. `mean_of_means` and `games_weighted` are still pending.

## What happened
- `hoops_list` q=`avg_game_by_decade` returned 0 items.
- `hoops_list` q=`decade season rows JIVPJ22E` returned 0 items.
- The `hoops_bib` lookup for WNKIH56T returned no output in this pass.

## Next
1. Fetch the season tables from Basketball-Reference (WNKIH56T, https://www.basketball-reference.com/). Use a polite rate and respect its ToS. Do not redistribute raw dumps.
2. Aggregate by decade, then run `analysis/decade_means.py` on the result.
3. Cite the exact URL and fetch date next to every number.
4. If scraping is blocked, use nba_api (9FJZPDKM) for league-level season game stats and note the ToS.

## Sources
- hoops/data sources/Unknown - n.d. - Basketball-Reference -- WNKIH56T
- hoops/data sources/Swar Patel - n.d. - nba_api -- 9FJZPDKM
