# Data source glance (coder)

No numbers here. Every row comes from the Zotero `ds` entries (abstract text only). Item key is the last token of the path.

## Fit for decade averages (avg_game_by_decade)

The abstract names Basketball-Reference as the primary source for the glen-w/hoops season rows. That makes it the intended input for `decade_compare.py`. Glen still needs to supply the season CSV.

| Source | Key | Lang | Access / ToS note (from abstract) | Use for Hoops |
|---|---|---|---|---|
| Basketball-Reference | WNKIH56T | web | Season, advanced and salaries pages. Scrape with etiquette. Not a bulk open dump license. | Primary: season rows, decade averages, salaries |
| Basketball_reference_scraper | ZJQF9C6X | Python | Scrapes B-Ref history back to BAA. Rate-limit; check commercial ToS before redistributing. | Optional fetch path for the CSV |
| nba_api | 9FJZPDKM | Python | NBA.com Stats client: box scores, PBP, shot charts, tracking. Rate-limit and ToS sensitive; do not redistribute raw dumps without checking the license. | Modern-era detail |
| NBA Stats | 6HB5G2B3 | web/API | Official site behind nba_api. Endpoints change; tracking and advanced splits uneven by era. | Era caveat for any tracking stat |
| pbpstats | ASRNZRRW | Python | PBP parsing, lineups, on/off from NBA Stats feeds. | Lineup / on-off chapters |
| hoopR | NEGCDXKA | R | ESPN loads, NBA Stats wrappers, B-Ref scrapers. KenPom needs a subscription. load_nba_pbp covers multi-season ESPN PBP (~2002 on). | R path, PBP |
| nbastatR | PXFIX2G8 | R | NBA Stats, B-Ref, HoopsHype, RealGM and draft wrappers. Front-office oriented. | Salary / front-office angle |
| BasketballAnalyzeR | ZV8R54SA | R (CRAN) | Companion to Basketball Data Science (CRC). Analysis and visualization helpers. | Method reference |
| wyattowalsh nbadb (Kaggle) | VVBZ3IXN | SQLite | Box, PBP, salaries. Needs Kaggle auth. Parked for later in glen-w/hoops policy. | Optional bulk land, not first |
| wehoop | 4J27S9CP | R | WNBA and women's college via ESPN. | Only if the book covers WNBA |
| Barttorvik T-Rank | 7FHGENDV / NVTWTCHG | web/CSV | Free D-I ratings and four factors (~2008 on). Verify ToS for bulk scraping. | College side |
| KenPom | RTJ8Q7E6 | web | Premium. Cite-only unless subscribed. | Cite only |
| awesome-nba-data | CTJJ3N4H | index | Source matrix and ToS notes. Not a license grant. | ToS cross-check |

## Gaps

- No source in `ds` is confirmed for CBA, income or team items. The abstracts only cover tooling.
- Salary data: B-Ref salaries pages and nbadb list salaries. Coverage by year is unchecked.
- No CSV is in hand, so no columns have been validated against decade_csv_spec.md.

## Next

1. Glen supplies the B-Ref season CSV.
2. Check its columns against decade_csv_spec.md.
3. Run `decade_compare.py --help`.
4. The researcher picks mean_of_means or games_weighted, then runs the script.
