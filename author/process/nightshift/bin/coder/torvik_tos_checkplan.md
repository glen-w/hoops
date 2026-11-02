# Barttorvik ToS Verification Plan (coder, 2026-10-19)

Gate stays CLOSED until all five items below are answered with quoted text + source URL. No fetch, no number reads, before PASS is recorded in analysis/torvik_gate_update.md.

## Checks
1. **robots.txt** — fetch https://barttorvik.com/robots.txt; record Disallow rules and any Crawl-delay.
2. **Terms wording** — locate Terms of Service / Terms of Use / Privacy pages linked from barttorvik.com; quote automated-access, scraping, and dataset clauses verbatim.
3. **CSV direct-download status** — confirm whether season files such as 2025_team_results.csv are served as public direct downloads or gated behind auth/params.
4. **Rate limits** — record any stated limit; if none stated, self-limit conservatively (single-season files, seconds between requests).
5. **Redistribution** — determine whether raw CSVs may be stored/committed, or only derived statistics may be published.

## Decision rule
- All five PASS -> record PASS in analysis/torvik_gate_update.md, then run in order: analysis/fetch_torvik_csv.py (2024/2025 seasons) -> analysis/check_torvik_csv.py -> analysis/torvik_loader.py -> analysis/torvik_analysis.py.
- Any FAIL -> activate analysis/torvik_cite_only_fallback.md; do not run fetch.

## Citations
- hoops/_ repo citeables/open datasets _ catalog/Bart Torvik - n.d. - Barttorvik T-Rank — NCAA team ratings CSVs -- NVTWTCHG
- hoops/data sources/Unknown - n.d. - Barttorvik (T-Rank) college basketball -- 7FHGENDV
- hoops/data sources/Saiem Gilani - n.d. - hoopR (sportsdataverse) -- NEGCDXKA