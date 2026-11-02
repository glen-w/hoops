# Coder final, tick 253 (2026-10-20)

No scripts were run this tick and no numbers were computed.

## hr result
Both hoops_summary requests (Foteinakis, Wang) returned the error `'path'`. No summary text came back. The error suggests the request needs a `p` field with the exact item path. Retry next tick with `p` set to the pc path, not only `q`.

## Still open
1. Run `analysis/br_league_fetch.py`. Record the URL and access date. Do not cite BR before the run succeeds.
2. Run `decade_means.py`. Report `mean_of_means` and `games_weighted` as separate values.
3. Foteinakis: nine seasons or 2012-13 through 2022-23? The PDF or a working hr summary must decide. Make no chapter edits until it does.
4. Wang: the stated limitations and the 1.85/yr slope method (OLS or first-to-last difference) are unconfirmed.
5. After step 1, compare the BR 3PA share with Wang's 22%-39% range. Check that both use the same definition and seasons.

## Sources
- hoops/data sources/Unknown - n.d. - Basketball-Reference -- WNKIH56T
- hoops/data sources/Swar Patel - n.d. - nba_api -- 9FJZPDKM
- hoops/_inbox/Wang - 2022 - NCQ6GJND
- hoops/⭐game 🏀/offense 💥/Foteinakis - 2025 - E7QXTIF7

## Caveat
BR is not a bulk open license. Fetch politely, cache once, and do not redistribute raw tables.
