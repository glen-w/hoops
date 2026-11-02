# Tick 259 final

Status: blocked on lookup. No numbers were produced or invented.

## What happened
- hoops_list for the Foteinakis query ("Foteinakis decade of evolution shooting trends offensive efficiency") returned n=0.
- hoops_list for the Wang query ("Wang changes in basketball shooting pattern and accuracy NBA") returned n=0.
- The hoops_bib result was not returned in hr_out. Treat it as unverified.
- The tick 258 hoops_summary 'path' error is still unresolved. No exact path was recovered this tick.

## Likely cause
The queries were long multi-word strings, which probably matched nothing. This is a guess, not confirmed.

## Next tick, first pass
- hoops_list with short queries: "Foteinakis" and "Wang 2022".
- If still empty, call hoops_record or hoops_summary with the known Zotero item paths as p:
  - Foteinakis (E7QXTIF7): `hoops/⭐game 🏀/offense 💥/Foteinakis - 2025 - A Decade of Evolution Comparative Analysis of Shooting Trends and Offensive Efficiency in -- E7QXTIF7`
  - Wang (NCQ6GJND): `hoops/_inbox/Wang - 2022 - What are the changes in basketball shooting pattern and accuracy in National Basketball -- NCQ6GJND`
- Retry hoops_bib to check the local bib for both keys.

## Still open
- Foteinakis: the window indicates 10 seasons but the summary says 9. Confirm the season list in the methods. Find per-season 3PA/FGA, since only pooled values exist.
- Wang: read the bin edges, the slope estimator behind 1.85/yr, and the limitations. The 24ft+ bin is not 3PA/FGA.
- Run br_league_fetch.py. Cite the URL and access date (Basketball-Reference, ds WNKIH56T).
- Run decade_means.py. Report mean_of_means and games_weighted separately.
- Fill Table A (BR vs Foteinakis) and Table B (BR vs Wang) separately.

Tables A and B stay blank until the sources are read and the scripts are run.
