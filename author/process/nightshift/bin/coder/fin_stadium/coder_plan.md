# Hoops Analysis Plan – 2026-10-22

## 1. Triage Grokbot Files
- Parse `analysis/_grokbot/2026-10-22-pm/INDEX.md` to list 14 pending files.
- Flag the four FT‑pipeline files (`build_ft.py`, `enrich.py`, `analyze.py`, `robustness.py`) as recoverable.
- Verify that the CSV `ft_attempts_2015-2024.csv.gz` is complete and can be re‑imported.

## 2. Use Existing Answers
- **MEDIA**: Use the `paperful_ask` answer for NBA media rights, local RSN revenue, and national TV money. Cite the sources listed in the answer.
- **FRANCHISE**: Use the `paperful_ask` answer for franchise valuation and operating income. Include Forbes and audited references as provided.
- **STADIUM**: Use the `paperful_ask` answer for arena construction financing, public subsidy, and stadium revenue. Cite the sources from the answer.

## 3. Reference Management
- Add the three answers to the Zotero library via `hoops_bib` (40 items). Ensure each citation key matches the keys in the answers.
- Update `analysis/nightshift_requests.json` to flag any remaining gaps in FIN, MEDIA, STADIUM that cannot be filled with the current answers.

## 4. Next Steps
1. Run a quick sanity check on the FT pipeline outputs (verify row counts, missing values).
2. Draft the FIN, MEDIA, STADIUM sections using the answers, inserting inline citations.
3. Consolidate endnotes and bibliography; reconcile 38k endnotes vs 464 bib entries in Zotero.
4. Submit the updated sections to the manuscript for review.

## 5. Paths to Update
- `analysis/_grokbot/2026-10-22-pm/INDEX.md`
- `analysis/fin_stadium/coder_plan.md`
- `analysis/nightshift_requests.json`
- `analysis/hoops_status.md`
- `hoops_bib` (40 items)

---
*This plan is a snapshot for the current tick; further refinement will follow after FT pipeline verification.*