# Tick 293 final

Source for every number below: hr_out summaries (qwen3.8 mirrored notes). They are summaries, not full text, so check against the PDFs before quoting in the manuscript. The Basketball-Reference record was read for its URL only (https://www.basketball-reference.com/). No fetch was run, so no BR numbers exist yet.

## Table A: Karamousalidis 2025, Euroleague vs NCAA DI (2020-21)
Path: hoops/⭐game 🏀/offense 💥/Karamousalidis ... 8VEP8FE8

| Metric | Euroleague | NCAA DI | All |
|---|---|---|---|
| Games | 35 | 35 | 70 |
| 3PT sequences | 1,774 | 1,475 | 3,249 |
| 3P% | 38.4 | 35.1 | 36.9 |
| Transition share of attempts (%) | 8.0 | 9.4 | |
| Transition 3P% | 39.0 | 32.8 | |
| Set-play 3P% | 38.4 | 35.5 | |
| Set-play share of all attempts (%) | | | 75.3 |
| End-of-possession share (%) | 19.4 | 6.1 | |
| Middle-of-possession 3P% | 41.2 | 36.1 | |
| Forward 3P% | 39.3 | 33.4 | |

Guards took 59.7% of all attempts (both leagues pooled). Chi-square results: offense type 20.84, timing 206.52, position 30.79, each df=2, p<.001.

Arithmetic check: (1774*0.384 + 1475*0.351) / 3249 = 36.9%. This matches the reported overall figure. The sequence counts also sum to 3,249.

The excerpt was cut off at the CHAID results. Re-read the full note before using them.

## Table B: Foteinakis and Pavlidou 2025, NBA vs EuroLeague
Path: hoops/⭐game 🏀/offense 💥/Foteinakis ... E7QXTIF7

| Metric | EuroLeague | NBA |
|---|---|---|
| Games | 2,538 | 12,150 |
| 3PA/FGA % | 37.59 | 32.44 |
| 3PA per 100 poss | 32.79 | 27.94 |
| 2PA per 100 poss | 54.50 | 58.29 |
| 2P% | 52.90 | 51.11 |
| 3P% | 36.38 | 35.62 |
| eFG% | 53.95 | 52.14 |

Table A and Table B stay separate. They differ in design (video-coded sequences vs league box scores), in season (2020-21 only vs a decade) and in league pairing.

### Foteinakis discrepancies to resolve in the full text
1. Season count: the objective gives 2012-13 to 2022-23 and excludes 2019-20. That is 10 seasons. The methods say nine. Check which is correct and which seasons are included.
2. Game count: 12,150 NBA games over 9 seasons is 1,350 a season. A full regular season is 1,230 games, and the 2020-21 and 2021-22 seasons were not played in a standard format. The count only works if the NBA total includes something else, or if the season count is 10 (1,215 a season). Check the paper's own game table.
3. Per-team vs combined: confirm whether the figures are per team or per game combined, and whether league means are mean-of-games or pooled.

## Wang and Zheng 2022, NBA shot distribution (2011-12 to 2020-21)
Path: hoops/_inbox/Wang ... NCQ6GJND

Reported in the summary:
- 3PT share of FGA ('24 ft and above'): 22% to 39%, about +1.85 points a year.
- 16-24 ft share: 21% to about 7.2%.
- 3P% flat (p=0.150).
- Restricted-area accuracy above 60% every season.
- 'Field goals per game' rose from about 163 to 177.

Open question: the 163 to 177 figure is labelled 'field goals' in the summary. The paper likely means attempts, since it counts shots from a shot-chart API, and it may be both teams combined. Check the full text for attempts vs makes and for per-team vs per-game. Do not cite it as makes until then.

## Basketball-Reference
hr_out gave only the catalog record. Its note says it is scrape-friendly with etiquette and not a bulk open-dump license.

Next step: run analysis/br_league_fetch.py where network access is allowed. Log the URL and access date for each page. Build rows.csv from fetched values only.
