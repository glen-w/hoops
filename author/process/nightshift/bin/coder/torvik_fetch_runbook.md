# Torvik Fetch Runbook

Runs only after `analysis/torvik_tos_checklist.md` shows PASS.

## Sequence
```
python analysis/fetch_torvik_csv.py     # writes 2024/2025 team_results CSVs
python analysis/check_torvik_csv.py     # gate: schema, row counts, null checks
python analysis/torvik_loader.py        # load only CSVs that passed gate
python analysis/torvik_analysis.py      # stats/tables from loaded data
```

## Rules
- Gate (`check_torvik_csv.py`) must exit clean before loader or analysis is invoked.
- If fetch returns partial or redirected files, rerun check; do not hand-edit CSVs.
- All numbers in downstream prose trace to these files; cite the CSV path plus the Barttorvik Zotero record.
- If ToS check fails, abandon fetch; analysis falls back to published/cited tables only.

## Open threads
1. Confirm Barttorvik ToS (checklist).
2. Run fetch for 2024/2025.
3. Run check gate.
4. Run loader then analysis.
5. HR first pass — pending, hoops tools unavailable this tick.
