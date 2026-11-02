# Tick 271 final (coder)

Status: hoops_summary worked for both records. No per-season numbers in either, so no stats written and none invented.

## Foteinakis & Pavlidou 2025 (E7QXTIF7)
- Summary text says "nine seasons", but it also gives the span 2012-13 to 2022-23 with 2019-20 excluded. That span is 11 seasons minus 1, so 10.
- Arithmetic check on the summary's NBA game count of 12,150. With 10 seasons, 9 x 1230 + 1080 (the shortened 2020-21 season) = 12,150. That matches exactly. With 9 seasons it does not match.
- Working conclusion: 10 seasons. The "nine" in the summary is probably a summary error. The 1230 and 1080 schedule lengths come from my own knowledge, not from the record. Confirm in the paper text via hoops_record before use.
- Summary reports only pooled league means: 3PA/FGA% 37.59 (EuroLeague) vs 32.44 (NBA); 3PA/100 poss 32.79 vs 27.94. These are per-100-possession rates, not raw per-season 3PA and FGA.
- Per-season 3PA and FGA, with page and table refs: not in the summary. Needs hoops_record.

## Wang & Zheng 2022 (NCQ6GJND)
- Seasons: 2011-12 to 2020-21, 10 regular seasons. Games per season 1,059 to 1,230.
- "Field goals per game" went from about 163 to 177 (p < 0.001). The summary does not say per-team or league-total.
- Context only, not a confirmation: a single NBA team usually attempts well under 100 FGA per game, so 163-177 is more likely both teams combined. Also unclear whether it is attempts or makes. Treat as unconfirmed until hoops_record gives the table or sentence.
- Distance bins: restricted area; <8 ft; 8-16; 16-24; 24+ ft. 3-pointer share 22% to 39%. 16-24 ft share 21% to about 7.2%. 3P accuracy flat (p = 0.150), 35-36%.

## Next
1. hoops_record for both papers. Get the season count, per-season 3PA and FGA with page and table, and the Wang 163-177 definition.
2. Run analysis/br_league_fetch.py. Cite the URL and access date.
3. Write analysis/decade_means.py.
4. Keep Table A and Table B separate. Keep mean_of_means and games_weighted separate.
