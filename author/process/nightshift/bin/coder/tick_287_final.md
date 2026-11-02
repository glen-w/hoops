# Tick 287 final

Source: hr_out summaries only. No fetched data. br_league_fetch.py not run.

## Foteinakis and Pavlidou 2025 (E7QXTIF7)
Path: hoops/⭐game 🏀/offense 💥/Foteinakis - 2025 - A Decade of Evolution ... -- E7QXTIF7
- Comparison: NBA vs EuroLeague.
- Span stated: 2012-2013 to 2022-2023. 2019-2020 excluded (pandemic).
- Games: 14,688 total. 12,150 NBA regular season. 2,538 EuroLeague (regular season plus top-16).
- Metrics: 2PA, 3PA, 2PM, 3PM per 100 possessions. 3PA/FGA%, 3PM/FGM%, 2P%, 3P%, eFG%.
- Stats: Shapiro-Wilk, then Mann-Whitney U, p < 0.05, JASP 0.19.
- Pooled values (summary): 3PA/FGA% 37.59 EL vs 32.44 NBA. 3PA/100 32.79 vs 27.94. 2PA/100 NBA 58.29 vs EL 54.50. 2P% 52.90 EL vs 51.11 NBA. 3P% 36.38 vs 35.62. eFG% 53.95 vs 52.14.
- Flag: the summary says nine seasons, but 2012-13 to 2022-23 minus 2019-20 is ten. The season list is not confirmed. Read the full text before listing seasons.
- Flag: these are pooled whole-period values, not per-season. Do not mix them with Table A or Table B rows.

## Wang and Zheng 2022 (NCQ6GJND)
Path: hoops/_inbox/Wang - 2022 - What are the changes ... -- NCQ6GJND
- Seasons: 2011-2012 to 2020-2021 regular seasons. Source: NBA shot chart API via Python.
- Games per season 1,059 to 1,230. Trend test: Mann-Kendall. Matlab 2020a.
- Summary says league-wide aggregate. It says 'field goals per game' rose from about 163 to 177 (p < 0.001).
- STILL UNCONFIRMED: whether 163 and 177 are per-team or combined, and whether they are attempts or makes. The summary excerpt does not settle either. Do not use 163 or 177 until the full text methods and results are read.
- Usable as stated: 3-pointer share (24 ft and above) rose 22% to 39%. 16-24 ft share fell 21% to about 7.2%. 3P accuracy flat (p = 0.150), 35-36% range. Restricted area accuracy above 60% every season.

## Library searches
- q=Karamousalidis: 1 hit. hoops/⭐game 🏀/offense 💥/Karamousalidis - 2025 - A comparison of three-point shooting effectiveness in the Euroleague and NCAA DI -- 8VEP8FE8. Summary exists. Next: hoops_summary on that path.
- q=CHAID: 1 hit, Noivo 2022 ball screen paper (VLIEQWMV). The title is unrelated to CHAID. Record: CHAID not in library, unless Noivo's full text uses it. That is unverified.

## Still blocked
- br_league_fetch.py: run only where fetching is permitted. Log URL and access date. Build rows.csv from fetched values only.
- Keep Table A (mean_of_means) and Table B (games_weighted) separate.
