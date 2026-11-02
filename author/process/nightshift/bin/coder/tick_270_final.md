# Tick 270 final

Both hoops_summary requests failed with error `'path'`. No summary text came back. Nothing was verified and no numbers were added.

## Failed
- hoops_summary E7QXTIF7 (Foteinakis 2025): error 'path'.
- hoops_summary NCQ6GJND (Wang 2022): error 'path'.

## Likely cause
The query was free text. The error looks like a missing `p` (path) key, so the next try should pass `p` with the exact record path, not only `q`. This is a guess and has not been tested.

## Still open
1. Foteinakis: ten or nine seasons? Record 3PA and FGA per season, with page and table for each.
2. Wang pp. 163-177: what is measured, and is it per-team or league-total?
3. Run `analysis/br_league_fetch.py`. Cite the URL and access date (Basketball-Reference, WNKIH56T). Then write `analysis/decade_means.py`.
4. Keep Table A and Table B separate.
5. Keep mean_of_means and games_weighted separate.

## Next tick
Retry hoops_summary with `p` set to each path below. If it fails again, use hoops_record on the same paths.

## Sources
- hoops/⭐game 🏀/offense 💥/Foteinakis - 2025 - A Decade of Evolution Comparative Analysis of Shooting Trends and Offensive Efficiency in -- E7QXTIF7
- hoops/_inbox/Wang - 2022 - What are the changes in basketball shooting pattern and accuracy in National Basketball -- NCQ6GJND
- hoops/data sources/Unknown - n.d. - Basketball-Reference -- WNKIH56T
