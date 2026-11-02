# Source routing for Hoops (from ds abstracts only)

No numbers here. Each row restates what the Zotero abstract says. Check ToS before bulk use or redistribution.

| Book question | First source | Backup | Caveat from abstract |
|---|---|---|---|
| Decade averages (season rows) | Basketball-Reference (WNKIH56T) | Basketball_reference_scraper (ZJQF9C6X) | Scrape with etiquette. It is not a bulk open dump license. |
| Box scores, play-by-play, shot charts | nba_api (9FJZPDKM) | NBA Stats (6HB5G2B3) | Rate limits and ToS. Endpoints change. Tracking and advanced splits are uneven by era. |
| Lineups, on/off | pbpstats (ASRNZRRW) | nba_api | Built on NBA Stats feeds. |
| Multi-season PBP in R | hoopR (NEGCDXKA) | nbastatR (PXFIX2G8) | hoopR load_nba_pbp covers ESPN PBP from about 2002. |
| Salaries, bulk historical | wyattowalsh Kaggle nbadb (VVBZ3IXN) | B-Ref salaries pages (WNKIH56T) | Parked in the glen-w/hoops policy. Needs Kaggle auth. Salary coverage by year is unconfirmed. |
| WNBA and women's college | wehoop (4J27S9CP) | B-Ref (WNBA tables) | ESPN-based. |
| College efficiency, open | Barttorvik CSVs (NVTWTCHG, 7FHGENDV) | none | Free, about 2008 onward. Verify scrape/ToS for bulk use. |
| College efficiency, premium | KenPom (RTJ8Q7E6) | Barttorvik | Paywalled. Cite-only unless subscribed. |
| Plot and analysis helpers | BasketballAnalyzeR (ZV8R54SA) | none | Companion to Basketball Data Science (CRC). |
| Finding more sources and ToS | awesome-nba-data (CTJJ3N4H) | none | A curation index, not a license grant. |

## Gaps (no ds item found)
- CBA / collective bargaining
- Income / salary cap
- Teams / franchise history

The researcher needs to run hoops_list for these. Glen needs to say where they live in Zotero.

## Unblock order
1. Glen supplies the B-Ref season CSV.
2. Run `csv_probe.py --expect <cols from decade_csv_spec.md>`.
3. The researcher picks mean_of_means or games_weighted.
4. Run `decade_compare.py --help`, then execute it.
