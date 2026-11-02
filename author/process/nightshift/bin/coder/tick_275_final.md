# Tick 275 final

## Status
- HR retry by key failed. hoops_summary E7QXTIF7 and hoops_summary NCQ6GJND both returned error 'path'.
- The hoops_bib call for Foteinakis got no result in hr_out.
- Same failure as tick 274. Retrying hoops_summary by key does not work.
- No numbers computed. None invented.
- decade_means.py is input-driven and still unrun.
- br_league_fetch.py is not yet run, so no URL or access date is logged.

## Open conflicts
- Foteinakis (E7QXTIF7): summary says 9 seasons, derived window says 10. Unresolved. Check the paper text before using either.
- Wang (NCQ6GJND), pp. 163-177: unresolved. Do not use until full text or notes are read.

## Next
1. Do not retry hoops_summary with a bare key. It has failed twice.
2. Try hoops_record with the exact item title, or hoops_list with a title query, to get a path.
3. Try hoops_bib with a short query such as 'Foteinakis' or 'Wang 2022 NBA shooting'.
4. Read the Foteinakis season count and resolve 9 vs 10.
5. Read what Wang 163-177 refers to.
6. Run br_league_fetch.py. Log URL and access date. Build rows.csv from fetched values only.
7. Keep Table A and Table B separate.
8. Keep mean_of_means separate from games_weighted.

## Sources (unread)
- hoops/⭐game 🏀/offense 💥/Foteinakis - 2025 - A Decade of Evolution Comparative Analysis of Shooting Trends and Offensive Efficiency in -- E7QXTIF7
- hoops/_inbox/Wang - 2022 - What are the changes in basketball shooting pattern and accuracy in National Basketball -- NCQ6GJND
- hoops/data sources/Unknown - n.d. - Basketball-Reference -- WNKIH56T
