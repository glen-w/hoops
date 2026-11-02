# Hoops data sources by ecosystem

Derived only from ds abstracts. No stats here. Verify ToS before bulk use.

## Python
- nba_api (9FJZPDKM): NBA.com Stats client. Box, PBP, shot charts, tracking. Rate-limit and ToS sensitive. Do not redistribute raw dumps without checking the license.
- pbpstats (ASRNZRRW): PBP parsing, lineups, on/off from NBA Stats feeds.
- Basketball_reference_scraper (ZJQF9C6X): B-Ref historical tables back to BAA. Rate-limit politely. Check commercial ToS before redistributing.

## R
- nbastatR (PXFIX2G8): NBA Stats API plus B-Ref, HoopsHype, RealGM, draft sources.
- hoopR (NEGCDXKA): ESPN NBA/NCAAM loads, NBA Stats wrappers, B-Ref scrapers. KenPom needs a subscription. load_nba_pbp covers ESPN PBP from about 2002.
- wehoop (4J27S9CP): WNBA and women's college via ESPN.
- BasketballAnalyzeR (ZV8R54SA): CRAN analysis and visualization helpers. Already cited in Glen's Zotero (BB4SV25F).

## Web / manual
- Basketball-Reference (WNKIH56T): canonical historical tables, including salaries pages. Scrape with etiquette. Not a bulk open license. Primary source for avg_game_by_decade season rows.
- NBA Stats (6HB5G2B3): official API behind nba_api. Endpoints change. Tracking and advanced splits are uneven by era.

## College
- Barttorvik (7FHGENDV, NVTWTCHG): free D-I ratings and four factors from about 2008. Season-end CSVs. Verify bulk ToS.
- KenPom (RTJ8Q7E6): paywalled. Cite-only for the manuscript unless subscribed.

## Bulk / index
- wyattowalsh/basketball (VVBZ3IXN): large SQLite NBA DB including salaries. Needs Kaggle auth. Parked as optional.
- awesome-nba-data (CTJJ3N4H): source matrix and ToS notes. Not a license grant.

## Gaps
- No CBA, income, or team dataset in the ds list. Ask Glen or run hoops_list.
- Salary coverage by year is unconfirmed. Check B-Ref before use.
