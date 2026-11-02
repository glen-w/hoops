# Barttorvik ToS Confirmation Checklist

Purpose: clear the gate before `fetch_torvik_csv.py` runs. Fill every line from what the site itself states — do not infer permission.

## Checks
- [ ] `robots.txt` on barttorvik.com read; confirm CSV paths are not Disallowed.
- [ ] Site terms / copyright / about page read; note exact wording on scraping and reuse.
- [ ] Confirm `{year}_team_results.csv` files are published as direct downloads, not session-gated.
- [ ] Rate-limit plan written: sequential requests only, delay between hits, single-season files (no crawl of all years in one burst).
- [ ] Redistribution stance recorded: raw CSVs cached locally for analysis; raw dumps not republished; derived tables only, credited to barttorvik.com.
- [ ] Attribution line ready for manuscript tables: source note crediting Bart Torvik T-Rank.
- [ ] Paywall separation confirmed: nothing from KenPom or other subscription feeds mixed into fetched files.
- [ ] If any check fails: stop, keep cite-only path (published tables), note fallback in `analysis/torvik_gate_update.md`.

## Sign-off
- ToS confirmed on: ____ (date)
- Checked by: coder citizen, tick 2026-10-19
- Result: PASS / FAIL → next step:

Until PASS date is filled, gate stays closed and no CSV numbers enter analysis.
