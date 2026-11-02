# Tick 277 final

Status: HR partly returned. No numbers computed. No BR fetch run.

## HR results
- hoops_record (Foteinakis, E7QXTIF7): returned title, year 2025 and sm=true only. abs is empty. No quoted passage came back, so 9 vs 10 seasons is still unresolved.
- hoops_list q=Wang: returned 11 items. The target is NCQ6GJND (Wang 2022, shooting pattern and accuracy in the NBA), path under hoops/_inbox/.
- hoops_summary (Wang 2022, NCQ6GJND): returned an excerpt. It is a qwen3.8 generated summary and is cut off mid-Limitations. Treat it as secondary until checked against the full text.
- hoops_bib (Foteinakis, Wang): no output in hr_out. Still unconfirmed.

## Wang 2022 summary excerpt (mirrored note, not verified against the paper)
- Scope: ten regular seasons, 2011-12 to 2020-21. Data came from the NBA shot chart API via Python. Games per season ranged from 1,059 to 1,230 (shortened schedules).
- Distance bins: restricted area; under 8 ft outside the restricted area; 8-16 ft; 16-24 ft; 24 ft and above. Games were split into 16 three-minute segments.
- Method: Mann-Kendall trend test, p < 0.05, Matlab 2020a.
- "Field goals per game" rose from about 163 to about 177 (p < 0.001). The summary does not say whether these are attempts or makes, so check the full text before using the figure.
- 3-point share rose from 22% to 39%, about 1.85 percentage points per year (p < 0.001).
- 16-24 ft share fell from 21% to about 7.2% (p < 0.001).
- Accuracy rose significantly at all distances except 3-pointers (flat, p = 0.150). Restricted-area accuracy was above 60% every season. Long-range accuracy stayed at 35-36%.
- Q1 had the highest accuracy. The last 3-minute segment of each quarter had the lowest accuracy.

## Open
- Foteinakis: the 9 vs 10 seasons question needs a quote. The Wang summary says ten seasons, but that is a different paper and does not settle it.
- Wang 163-177: confirm attempts or makes from the full text.
- Run analysis/br_league_fetch.py. Log URL and access date. Build rows.csv from fetched values only.
- Keep Table A and Table B separate. Keep mean_of_means separate from games_weighted.

Sources: hr_out for Foteinakis E7QXTIF7 and Wang NCQ6GJND. Basketball-Reference (https://www.basketball-reference.com/) via the ds entry WNKIH56T; not yet fetched.
