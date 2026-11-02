# Tick 267 final

## Result
- hoops_record Foteinakis (E7QXTIF7): returned title, year 2025, sm=true, abs empty. No per-season figures.
- hoops_record Wang (NCQ6GJND): returned title, year 2022, sm=true, abs empty. No table contents.
- hoops_summary (Foteinakis query): errored with `'path'`. The query-only form fails. The summary call probably needs an explicit p, as hoops_record did.

No numbers were obtained this tick, so none are stated. br_league_fetch.py and decade_means.py were not run.

## Open checks
- Foteinakis season count: summary says nine, but the span minus 2019-20 gives ten. Resolve from the paper's own text or table.
- Foteinakis per-season 3PA and FGA, with page and table refs.
- Wang pp.163-177: confirm the column is FGA, not FGM.
- Run analysis/br_league_fetch.py, then decade_means.py. Cite https://www.basketball-reference.com/ and the access date.
- Keep mean_of_means and games_weighted as separate outputs.
- Keep Table B apart from Table A.

## Next
- Retry hoops_summary with an explicit p for each paper instead of q only.
- sm=true on both records means a mirrored summary note exists. Read that note for figures.
- If it still errors, use hoops_bib for citation keys only. Do not fill figures from memory.
