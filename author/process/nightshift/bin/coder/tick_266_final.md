# Tick 266 final (2026-10-20)

## Done
- Status note written. No code run, no new numbers.

## HR result
- Both hoops_record calls (Foteinakis, Wang) returned error `'path'`. No record content came back.
- Cause is unknown. It may be a missing `path` field on the record lookup. Nothing was verified about the PDFs.

## Still open
1. **Foteinakis season count.** The summary says nine seasons. The span minus 2019-20 gives ten. Not resolved. Do not state a count in the chapter until the PDF's own season list or a table caption settles it.
2. **Foteinakis per-season 3PA and FGA.** Not extracted. Record the page and table numbers when pulled.
3. **Wang pp. 163-177.** Probably FGA, but inferred and unconfirmed. Check the table header (FGA vs FGM) before use.
4. **Fetch.** Run br_league_fetch.py, then decade_means.py. Cite the Basketball-Reference URL and the access date.

## Next tick
- Retry hoops_record with a `p` path taken from the pc list below, not only a `q` query. If it errors again, try hoops_summary instead.

## Invariants
- Keep mean_of_means and games_weighted as separate columns.
- Keep Table B apart from Table A.
- No invented values.

## Sources (pc)
- hoops/⭐game 🏀/offense 💥/Foteinakis - 2025 - A Decade of Evolution Comparative Analysis of Shooting Trends and Offensive Efficiency in -- E7QXTIF7
- hoops/_inbox/Wang - 2022 - What are the changes in basketball shooting pattern and accuracy in National Basketball -- NCQ6GJND
- hoops/data sources/Unknown - n.d. - Basketball-Reference -- WNKIH56T
