# Torvik Gate Update

**Status**: scripts staged, bulk fetch held on one blocker — Barttorvik Terms of Service confirmation.

## Blocker
`fetch_torvik_csv.py` must not run until ToS sign-off is recorded. Everything downstream (`check_torvik_csv.py` gate → `torvik_loader.py` → `torvik_analysis.py`) waits behind it.

## Run order after sign-off
1. Record sign-off date in `analysis/torvik_tos_checklist.md`.
2. `python analysis/fetch_torvik_csv.py` — pulls `2024_team_results.csv`, `2025_team_results.csv` (season-end files, small number of requests, polite delay between hits).
3. `python analysis/check_torvik_csv.py` — schema/completeness gate. No numbers read or reported before this passes.
4. `python analysis/torvik_loader.py` — load gated CSVs.
5. `python analysis/torvik_analysis.py` — stats and tables.

## Data sourcing rule
Glen supplies no CSVs. Sources are Zotero notes/attachments (ds entries) and real public endpoints cited in-file. No invented numbers.

## Citations
- `hoops/_ repo citeables/open datasets _ catalog/Bart Torvik - n.d. - Barttorvik T-Rank — NCAA team ratings CSVs -- NVTWTCHG`
- `hoops/data sources/Unknown - n.d. - Barttorvik (T-Rank) college basketball -- 7FHGENDV`
- `hoops/data sources/Saiem Gilani - n.d. - hoopR (sportsdataverse) -- NEGCDXKA` (reference client for torvik loaders)
