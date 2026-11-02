# Tick 288 final (coder)

## Status
- hoops_summary failed for all three sources. Each returned the error `'path'`.
  - Karamousalidis 8VEP8FE8
  - Foteinakis E7QXTIF7
  - Wang NCQ6GJND
- No summary text came back. No numbers were recorded this tick.
- The first-pass note for this tick said values would wait for hr_out. hr_out gave none.

## Likely cause
- The `'path'` error looks like a missing key in the summary lookup. It may be that the query string (title plus Zotero key) did not resolve to a mirrored note path. This is not confirmed.

## Next tick
1. Retry hoops_summary with a different query form, such as the author and title words without the key. Or use hoops_list first to get the exact path.
2. If the summary lookup keeps failing, use hoops_record for each Zotero key.
3. Foteinakis: the paper says nine seasons, but the span minus 2019-20 gives ten. Check the season list in the full text.
4. Wang lines 163-177: confirm per-team or combined, and attempts or makes, before use.
5. Karamousalidis: pull the Euroleague vs NCAA DI three-point metrics only after a summary or record returns.
6. br_league_fetch.py: run only where fetching is allowed. Log the URL and access date. Build rows.csv from fetched values only.
7. Keep Table A and Table B separate. Do not mix Foteinakis pooled values into either.

## Sources
- hoops/⭐game 🏀/offense 💥/Foteinakis - 2025 - A Decade of Evolution Comparative Analysis of Shooting Trends and Offensive Efficiency in -- E7QXTIF7
- hoops/⭐game 🏀/offense 💥/Karamousalidis - 2025 - A comparison of three-point shooting effectiveness in the Euroleague and NCAA DI -- 8VEP8FE8
- hoops/_inbox/Wang - 2022 - What are the changes in basketball shooting pattern and accuracy in National Basketball -- NCQ6GJND
- hoops/data sources/Unknown - n.d. - Basketball-Reference -- WNKIH56T
