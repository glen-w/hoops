# Tick 278 final

Status: no numbers computed. Summaries are model-generated (qwen3.8) and truncated, so they are unverified leads, not quotes.

## Foteinakis and Pavlidou 2025 (E7QXTIF7): 9 vs 10 seasons, still open
- The summary says "nine seasons" and also gives the range 2012-2013 to 2022-2023 with 2019-2020 excluded.
- That range is 11 seasons minus 1, which makes 10. The summary contradicts itself.
- Games reported: 12,150 NBA and 2,538 EuroLeague, 14,688 total.
- Cross-check, an inference from the usual NBA schedule lengths and not from the paper: 7 x 1230 (2012-13 to 2018-19) + 1080 (2020-21) + 1230 + 1230 = 12,150. That matches ten seasons, not nine.
- Do not state the season count in the chapter until a full-text quote is logged.
- Ask hr for the paper's methods text, or hoops_summary with p, and quote the sentence on the season count.
- Summary figures, unverified, NBA vs EuroLeague: 3PA/FGA% 32.44 vs 37.59; 3PA/100 27.94 vs 32.79; 2PA/100 58.29 vs 54.50; 2P% 51.11 vs 52.90; 3P% 35.62 vs 36.38; eFG% 52.14 vs 53.95.

## Wang and Zheng 2022 (NCQ6GJND): 163 to 177
- The summary says "field goals per game" rose from about 163 (2011-12) to 177 (2020-21), p < 0.001.
- The data come from the NBA shot chart API, 10 seasons, 1,059 to 1,230 games per season.
- The wording is ambiguous between makes and attempts. The method groups attempts by distance, so attempts is more likely. This is unconfirmed.
- Quote the paper's own wording before use, and say whether the count covers both teams.
- Other summary claims, unverified: 3-point share 22% to 39%, 16-24 ft share 21% to 7.2%, 3P% flat (p = 0.150).

## Bib
- hoops_bib returned nothing for both queries in this pass. Retry with a title fragment or key.

## Next
1. Request the Foteinakis methods quote and the Wang wording on 163 to 177.
2. Run analysis/br_league_fetch.py. Log the URL and access date. Build rows.csv from fetched values only.
3. Keep Table A and Table B separate. Keep mean_of_means separate from games_weighted.

## Sources
- hoops/data sources/Unknown - n.d. - Basketball-Reference -- WNKIH56T
