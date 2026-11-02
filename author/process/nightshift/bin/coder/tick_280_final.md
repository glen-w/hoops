# Tick 280 final

- hoops_record on E7QXTIF7 returned error `'path'`. No record text was retrieved.
- The hoops_bib lookups for "Foteinakis" and "Wang 2022" returned nothing in hr_out.
- No computation was done and no new facts were recorded.

## Open
- Foteinakis: still need a full-text methods quote on season count. The range and 12,150 games imply 10 seasons, but the summary says 9.
- Wang 163-177: still need a quote on attempts vs makes and one team vs both teams.
- The hoops_summary and hoops_record calls both fail on 'path'. Try hoops_list with a short query to get a valid path, or read the mirrored note under hoops/ directly.
- Run analysis/br_league_fetch.py, log the URL and access date, and build rows.csv from fetched values only.
- Keep Table A and Table B separate. Keep mean_of_means separate from games_weighted.

## Sources
- hoops/⭐game 🏀/offense 💥/Foteinakis - 2025 - A Decade of Evolution Comparative Analysis of Shooting Trends and Offensive Efficiency in -- E7QXTIF7
- hoops/_inbox/Wang - 2022 - What are the changes in basketball shooting pattern and accuracy in National Basketball -- NCQ6GJND
- hoops/data sources/Unknown - n.d. - Basketball-Reference -- WNKIH56T
