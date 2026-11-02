# Hoops data gaps (tick 2026-10-19)

Built only from ds abstracts and hr results. No numbers invented.

## Missing
- B-Ref season CSV (the avg_game_by_decade rows). Basketball-Reference, WNKIH56T, is the primary source. Glen must supply the file.
- CBA, income and teams items. hr hoops_list returned 0 items for each of these queries: "CBA collective bargaining agreement", "player income salary", "teams franchises". They are not in the Zotero hoops list under those terms. Glen must say where they live, or add them.

## Next steps once the CSV arrives
1. Read the expected columns from `decade_csv_spec.md`.
2. Run `csv_probe.py --expect <cols>`.
3. Run `decade_compare.py --help` before the first real run.
4. The researcher chooses mean_of_means or games_weighted.

## Source caveats from ds abstracts
- Basketball-Reference (WNKIH56T): scrape with etiquette. It is not a bulk open license.
- nba_api (9FJZPDKM): rate-limit and ToS sensitive. Do not redistribute raw dumps without checking the license.
- Basketball_reference_scraper (ZJQF9C6X): check commercial ToS before redistributing.
- KenPom (RTJ8Q7E6): paywalled. Cite-only unless subscribed.
- Barttorvik (7FHGENDV, NVTWTCHG): verify ToS before bulk scraping.
- wyattowalsh Kaggle nbadb (VVBZ3IXN): needs Kaggle auth. Optional bulk land, parked for later.
- awesome-nba-data (CTJJ3N4H): ToS matrix. It is not a license grant.

## Salary coverage
Unconfirmed by year. Confirm against B-Ref salary pages or the Kaggle nbadb before citing any salary trend.
