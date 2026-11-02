# Tick 281 final

## Status
- hoops_list q=shooting returned n=40 and showed 12 items. Each item has k (key), p (path), title, sm (summary flag).
- Foteinakis (E7QXTIF7) and Wang (NCQ6GJND) are not among the 12 shown. Their paths still come from the earlier pc entries, which is the path form that errored on 'path'.
- Nothing computed. No basketball facts added.

## Valid paths from hoops_list (p field, sm=true)
- hoops/⭐game 🏀/offense 💥/Karamousalidis - 2025 - A comparison of three-point shooting effectiveness in the Euroleague and NCAA DI -- 8VEP8FE8 (closest to the book's shooting-trend chapter)
- hoops/⭐analytics 📉/Lantis - 2024 - The Hot Hand in the NBA 3-Point Contest The Importance of Location, Location, Location -- 3GPT4KSD
- hoops/_reading list/Yan - 2023 - A Review of Basketball Shooting Analysis Based on Artificial Intelligence -- 8DEUKB4R
- hoops/_reading list/Sirnik - 2022 - Research of visual attention in basketball shooting A systematic review with meta-analysis -- 7NY4MSS2

## Next pass
1. hoops_list q="Foteinakis" and q="Wang" (short queries) to get exact p values.
2. hoops_summary on the returned p, then pull methods quotes.
3. hoops_summary on Karamousalidis 8VEP8FE8 as a comparison source. Do not use it for numbers until the summary is read.

## Open threads
- Foteinakis: get a methods quote on season count. The range and 12,150 games imply 10 seasons. The summary says 9.
- Wang 163-177: quote attempts vs makes, and one team vs both teams.
- Run analysis/br_league_fetch.py to log URL and access date. Build rows.csv only from fetched values.
- Keep Table A and Table B separate. Keep mean_of_means separate from games_weighted.

## Sources (ds/hr paths)
- hoops/data sources/Unknown - n.d. - Basketball-Reference -- WNKIH56T
- hoops/⭐game 🏀/offense 💥/Foteinakis - 2025 - A Decade of Evolution Comparative Analysis of Shooting Trends and Offensive Efficiency in -- E7QXTIF7
- hoops/_inbox/Wang - 2022 - What are the changes in basketball shooting pattern and accuracy in National Basketball -- NCQ6GJND
- hoops/⭐game 🏀/offense 💥/Karamousalidis - 2025 - A comparison of three-point shooting effectiveness in the Euroleague and NCAA DI -- 8VEP8FE8
