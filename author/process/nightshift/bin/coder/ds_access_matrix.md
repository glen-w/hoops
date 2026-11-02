# Hoops data sources: access matrix (from ds abs only)

Every cell below is copied or paraphrased from the Zotero `abs` text. Nothing is verified against live terms of service. Blank means the abs does not say.

| Source | Kind | Lang | Coverage per abs | Access / ToS flag per abs | Zotero key |
|---|---|---|---|---|---|
| Basketball-Reference | site | - | historical NBA/ABA/WNBA season, advanced, salaries pages | scrape-friendly with etiquette; not a bulk open dump license | WNKIH56T |
| NBA Stats (stats.nba.com) | API | - | box, advanced, tracking; uneven by era | endpoints change | 6HB5G2B3 |
| nba_api | client for NBA Stats | Python | box scores, PBP, shot charts, tracking | rate-limit and ToS sensitive; check license before redistributing raw dumps | 9FJZPDKM |
| Basketball_reference_scraper | scraper | Python | B-Ref historical tables, advanced metrics, back to BAA | rate-limit politely; commercial ToS check before redistribute | ZJQF9C6X |
| nbastatR | client | R | NBA Stats, B-Ref, HoopsHype, RealGM, draft | | PXFIX2G8 |
| pbpstats | parser | Python | PBP, lineups, on/off from NBA Stats feeds | | ASRNZRRW |
| hoopR | client | R | ESPN NBA/NCAAM, NBA Stats, B-Ref, KenPom; load_nba_pbp multi-season ESPN PBP (~2002 on) | KenPom needs a subscription | NEGCDXKA |
| wehoop | client | R | WNBA and women's college via ESPN | | 4J27S9CP |
| BasketballAnalyzeR | analysis pkg | R | analysis and visualization helpers | | ZV8R54SA |
| Kaggle nbadb (wyattowalsh) | SQLite dump | - | box, PBP, salaries | needs Kaggle auth; parked in glen-w/hoops policy; optional bulk | VVBZ3IXN |
| Barttorvik T-Rank | site and CSVs | - | D1 team ratings and four factors (~2008 on); {year}_team_results.csv | open-ish; verify scrape/ToS for bulk use | 7FHGENDV, NVTWTCHG |
| KenPom | site | - | college efficiency | paywall; cite-only unless subscribed | RTJ8Q7E6 |
| awesome-nba-data | index | - | source matrix and ToS notes | not a license grant | CTJJ3N4H |

## Reading
- avg_game_by_decade season rows: abs names Basketball-Reference as the primary source. A CSV is needed before `decade_table.py` can run.
- Open college path without KenPom: Barttorvik CSVs (abs says free; ToS still to verify).
- Python vs R is a toolchain choice. Read the awesome-nba-data matrix before picking nba_api or basketball_reference_scraper.

## Open
- Verify live ToS for B-Ref, NBA Stats, Barttorvik and Kaggle. Update `tos_checklist.md`.
- Compare against `list_sources.py` and `source_matrix.py` output. Merge if redundant.
