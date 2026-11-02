# Hoops data source matrix

Built only from the ds abstracts. It has no stat values. Every row is a Zotero item under `hoops/`.

| Source | Language | Scope | Caveat from abstract |
|---|---|---|---|
| Basketball-Reference | web tables | NBA/ABA/WNBA season, advanced and salary pages | Scrape with etiquette. Not a bulk open license. Primary source for the glen-w/hoops avg_game_by_decade season rows. |
| nba_api | Python | NBA.com Stats: box scores, PBP, shot charts, tracking | Rate-limit and ToS sensitive. Do not redistribute raw dumps without checking the license. |
| NBA Stats (stats.nba.com) | API | Official stats backing nba_api and R wrappers | Endpoints change. Tracking and advanced splits are uneven by era. |
| pbpstats | Python | PBP parsing, lineups, on/off | Built on NBA Stats feeds. |
| nbastatR | R | NBA Stats API, Basketball-Reference, HoopsHype, RealGM, draft sources | Front-office oriented wrappers. |
| hoopR | R | ESPN NBA/NCAAM loads, NBA Stats wrappers, Basketball-Reference scrapers, KenPom | KenPom needs a subscription. load_nba_pbp covers multi-season ESPN PBP (~2002 onward). |
| wehoop | R | WNBA and women's college via ESPN | PBP, box, standings. |
| Basketball_reference_scraper | Python | Basketball-Reference historical tables back to BAA | Rate-limit politely. Check commercial ToS before redistributing. |
| BasketballAnalyzeR | R (CRAN) | Analysis and visualization helpers | Companion to Basketball Data Science (CRC). |
| Barttorvik T-Rank | CSV / web | Free Division I team ratings and four factors (~2008 onward) | Verify scrape/ToS for bulk use. Season-end CSVs named {year}_team_results.csv. |
| KenPom | web | Premium college efficiency | Paywalled. Cite-only for the manuscript unless subscribed. |
| wyattowalsh/basketball (Kaggle) | SQLite | Large NBA historical DB (box, PBP, salaries) | Parked per glen-w/hoops policy. Needs Kaggle auth. Optional bulk land. |
| awesome-nba-data | index | Source matrix and ToS notes | A curation index, not a license grant. |

## Open items
- The avg_game_by_decade rows file is still not located. Do not write decade numbers until it has been read.
- CBA, income and team datasets are still unlisted. Researcher should retry hoops_list with salary, collective bargaining and franchise.
