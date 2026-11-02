# Tick 269 final

## Status
- `hoops_record` for Foteinakis (E7QXTIF7) returned title, year 2025, `sm:true`, and an empty abstract.
- `hoops_record` for Wang (NCQ6GJND) returned title, year 2022, `sm:true`, and an empty abstract.
- The records contain no season count, no per-season 3PA or FGA values, and no definition of 163-177.
- Nothing was verified this tick. No figures were added. Nothing was run.

## Still open
1. Foteinakis: season count (ten vs. nine) and per-season 3PA/FGA with page and table. Both records have `sm:true`, so the next pass should be `hoops_summary` (mirrored summary note) for E7QXTIF7. A PDF read is needed for page and table references.
2. Wang: what 163-177 measures, and whether it is per-team or league-total. Use `hoops_summary` for NCQ6GJND, then the PDF.
3. Run `analysis/br_league_fetch.py`. Cite the URL and access date. Then write `decade_means.py` against its actual output columns.

## Rules kept
- `mean_of_means` and `games_weighted` stay separate.
- Table A (papers) and Table B (Basketball-Reference) stay separate.
- See `analysis/definitions_3pa_share.md` before comparing Wang's 3PA share with Foteinakis's 3PA/FGA.
