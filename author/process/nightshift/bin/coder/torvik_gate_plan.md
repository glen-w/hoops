# Torvik Gate Plan — tick 2026-10-19 (r335)

Status: tools disabled this pass. No CSVs fetched, no stats emitted, no numbers invented.

## Steps (when tools on)
1. **Re-query hoopR**: `hoops_list(torvik_*)` returned 0 last tick. Consult hoopR docs (ds: `hoops/data sources/Saiem Gilani - n.d. - hoopR (sportsdataverse) -- NEGCDXKA`) for actual torvik export names; retry with corrected prefixes; log what returns.
2. **Fetch CSVs**: Barttorvik season-end pattern `{year}_team_results.csv` per citeable `hoops/_ repo citeables/open datasets _ catalog/Bart Torvik - n.d. - Barttorvik T-Rank — NCAA team ratings CSVs -- NVTWTCHG`. Drive via `analysis/fetch_torvik_csv.py` for 2024 and 2025 seasons. Cache raw bytes locally; polite rate; no redistribution.
3. **Gate**: run `analysis/check_torvik_csv.py` — must confirm parse OK, expected columns, season markers, row counts match source. Fail → halt with reason, emit nothing.
4. **Re-verify exports**: cross-check hoopR torvik_* rows against fetched CSV (sample team rows) before `analysis/torvik_loader.py` loads anything.
5. **Emit stats**: only after gate pass, run `analysis/torvik_analysis.py`.

## Non-goals
- No CSV requests to Glen.
- No invented numbers anywhere.
- KenPom cite-only unless subscribed.

Paths: `analysis/README.md`, `analysis/data_sources.md`, `analysis/fetch_torvik_csv.py`, `analysis/check_torvik_csv.py`, `analysis/torvik_loader.py`, `analysis/torvik_analysis.py`.