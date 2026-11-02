# Tick 279 final

## State
- Nothing computed. No data fetched. Bibliography still unverified.
- hr_out had one entry: hoops_summary (Foteinakis) returned error `'path'`. No summary text came back.
- The two hoops_bib queries ("Decade of Evolution", "changes in basketball shooting pattern") returned no output this tick. Treat them as unanswered.
- Foteinakis (E7QXTIF7): the summary says nine seasons, but its stated range and 12,150 games imply ten. Still unresolved. No methods quote in hand.
- Wang (NCQ6GJND): 163-177 is probably attempts, not makes. Unconfirmed. No quote on the metric or on one team vs both.

## Next
1. Retry hoops_record on the Foteinakis key E7QXTIF7 instead of hoops_summary, since the summary path errored. If that also fails, mark the season count as unverifiable from the library.
2. Retry hoops_bib with a single short fragment, e.g. "Foteinakis" and "Wang 2022".
3. Record the Wang metric definition only if quoted.
4. Run analysis/br_league_fetch.py. Log the URL and access date. Build rows.csv from fetched values only.
5. Keep Table A and Table B separate. Keep mean_of_means separate from games_weighted.

## Sources
- hoops/data sources/Unknown - n.d. - Basketball-Reference -- WNKIH56T (https://www.basketball-reference.com/)
