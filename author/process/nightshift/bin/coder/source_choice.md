# Source choice for decade averages

Recommendation: **basketball_reference_scraper** for season rows; **nba_api** only for later tracking or PBP work.

## Why
- Basketball-Reference ds note says it is the primary source for glen-w/hoops avg_game_by_decade season rows (ds: Unknown - n.d. - Basketball-Reference -- WNKIH56T).
- basketball_reference_scraper is a Python scraper for B-Ref historical tables, seasons back to BAA (ds: Vishaal Agartha - n.d. - Basketball_reference_scraper -- ZJQF9C6X).
- nba_api covers the NBA.com Stats API, whose tracking and advanced splits are uneven by era (ds: 6HB5G2B3, 9FJZPDKM). It is the wrong fit for pre-modern decades.

## Caveats
- Both sources are ToS and rate-limit sensitive. Do not redistribute raw dumps. Fill the Verified column in tos_checklist.md from live pages (ToS matrix: CTJJ3N4H).
- The Kaggle nbadb (VVBZ3IXN) is parked. It needs Kaggle auth.

## Open
- The researcher must choose mean_of_means or games_weighted. The script prints both so the choice is not blocking.
- Glen supplies the season CSV. Check its columns against decade_csv_spec.md.
