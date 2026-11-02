# Data source ToS checklist (Hoops book)

Scope: redistribution and scrape flags only. Every "ds says" cell is quoted or paraphrased from the Zotero ds abstract. Nothing here is verified against the live terms. Each "Verified?" cell stays `no` until someone reads the real ToS and records the date.

| Source | ds says | Verified? | Action before redistributing |
|---|---|---|---|
| Basketball-Reference | Scrape-friendly with etiquette; not a bulk open dump license. | no | Read site ToS. Do not republish raw tables. |
| nba_api | Rate-limit / ToS sensitive; do not redistribute raw dumps without checking license. | no | Read the NBA.com terms and the awesome-nba-data matrix. |
| Basketball_reference_scraper | Rate-limit politely; commercial ToS check before redistribute. | no | Same as Basketball-Reference. Also check the scraper repo license. |
| Barttorvik (T-Rank) | Verify scrape/ToS for bulk use. | no | Read site terms before bulk CSV pulls. |
| KenPom | Cite-only / paywall for manuscript unless subscribed. | no | Cite only. Do not embed data. |
| NBA Stats (stats.nba.com) | No ToS statement in ds. Only notes that endpoints change. | no | Find and read the official terms. |
| wyattowalsh/basketball (Kaggle) | Needs Kaggle auth; parked for later. No license stated in ds. | no | Read the dataset license page before use. |
| awesome-nba-data | Terms matrix, not a license grant. | n/a | Use as a finder. Read the linked sources' terms directly. |

## Rules for analysis/ code
- Cite the ds `p` path for every source a script reads.
- Commit scripts only. Do not commit raw scraped dumps.
- Rate-limit all scrapers. Never run bulk pulls without a verified-ToS row.

## Open
- Fill the Verified? column with a date and a link to the terms page.
- avg_game_by_decade season rows still need a Basketball-Reference CSV. Confirm its ToS row first.
