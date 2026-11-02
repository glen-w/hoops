# Tick 272 (final)

## State
- All three hr calls failed with error `'path'`: Foteinakis hoops_record, Foteinakis hoops_summary, Wang hoops_record. No record or summary content came back.
- Foteinakis season count is still unconfirmed (9 or 10). Game-count arithmetic from tick 271 suggests 10, but that is not settled.
- Wang's 163-177 is still undefined. Unknown whether it is per-team or league-total, or attempts or makes.
- No per-season 3PA/FGA seen. No numbers written. None invented.
- `analysis/br_league_fetch.py` has not been run. No URL or access date recorded.

## Next tick
- Retry hr with a `p` field set to the exact item path instead of a free-text `q`. The `'path'` error suggests the call needs `p`.
  - Foteinakis: `hoops/⭐game 🏀/offense 💥/Foteinakis - 2025 - A Decade of Evolution Comparative Analysis of Shooting Trends and Offensive Efficiency in -- E7QXTIF7`
  - Wang: `hoops/_inbox/Wang - 2022 - What are the changes in basketball shooting pattern and accuracy in National Basketball -- NCQ6GJND`
- Settle the season count and the Wang range from the records, with page and table refs.
- Then run br_league_fetch.py, record the URL and access date, and write decade_means.py.

## Rules for decade_means.py
- Keep Table A and Table B separate.
- Keep mean_of_means separate from games_weighted.
- Cite the Basketball-Reference URL and access date for every fetched row.
- Do not write the script until the season count and the Wang range are confirmed.

## Sources
- hoops/⭐game 🏀/offense 💥/Foteinakis - 2025 - A Decade of Evolution Comparative Analysis of Shooting Trends and Offensive Efficiency in -- E7QXTIF7
- hoops/_inbox/Wang - 2022 - What are the changes in basketball shooting pattern and accuracy in National Basketball -- NCQ6GJND
- hoops/data sources/Unknown - n.d. - Basketball-Reference -- WNKIH56T
