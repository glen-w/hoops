# Tick 261 final

## Status
- Foteinakis (E7QXTIF7): the hoops_bib q=Foteinakis result did not come back this tick. Pooled NBA and EuroLeague figures are still from a truncated summary excerpt, not the PDF. Unverified.
- Season-count conflict (nine vs ten, 2012-13 to 2022-23 excluding 2019-20) is still open.
- Wang (NCQ6GJND): hoops_summary returned. It is a model summary (qwen3.8:latest), and the excerpt is cut off at Limitations. The figures below are not checked against the PDF.
- Tables A and B: blank.

## Wang and Zheng 2022, from the summary excerpt
- Window: ten regular seasons, 2011-12 to 2020-21. Source: NBA shot chart API, via Python.
- Games per season: 1,059 to 1,230, because of shortened schedules.
- Distance bins: restricted area; <8 ft outside the restricted area; 8-16 ft; 16-24 ft; 24 ft and above.
- Method: Mann-Kendall trend test, p < 0.05, run in Matlab 2020a. Data are league-wide aggregates.
- Field goals per game: about 163 (2011-12) to 177 (2020-21), p < 0.001. The excerpt does not say whether this means attempts or makes. Check the PDF.
- 3-point share (24 ft and above): 22% to 39%, about +1.85 percentage points per year, p < 0.001.
- 16-24 ft share: 21% to about 7.2%, p < 0.001.
- Accuracy: rising at every distance except 3-pointers (flat, p = 0.150). Restricted-area accuracy is above 60% every season. Long-range accuracy is 35-36%.
- Within-game pattern: Q1 has the highest accuracy, and the last 3-minute segment of each quarter has the lowest.

## Use rules
- Wang gives ten seasons from 2011-12. Foteinakis uses a different window, so do not merge the two.
- Quote Wang figures only with a note that they are summary-sourced until the PDF is checked.
- Do not use pooled Foteinakis values as per-season data.
- Do not invent numbers.

## Next
1. Retry hoops_bib q=Foteinakis. If it is empty again, find the attachment path.
2. Check the Wang figures above, and what the field-goals-per-game number counts, against the PDF.
3. Settle the Foteinakis season count and get per-season 3PA/FGA.
4. Run br_league_fetch.py, then decade_means.py. Cite the Basketball-Reference URL (WNKIH56T) and the access date.
5. Keep mean_of_means and games_weighted as separate columns.
6. Fill Table A and Table B separately.