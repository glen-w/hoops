# Coder-01: League-Income Path A — Researcher Decision (2026-10-22)

## Decision

**APPROVED with conditions.** Path A scope (national media rights, salary cap/tax history, attendance, BRI definition; local media and licensing deferred to Path B) is coherent and appropriate for FIN chapter outline. Proceed to full dataset build conditioned on fixes below.

## Issues to Fix Before 2026-10-23 Deadline

**1. Salary-cap row off-by-one error (CRITICAL)**
- CSV currently shows: 2024-25 cap $154.647M, tax $188.103M
- **Official pr.nba.com figures:**
  - 2024-25: cap $140.588M, tax $170.814M
  - 2025-26: cap $154.647M, tax $187.895M (estimated)
- Action: Correct CSV rows. Coder's own `league_income_ingredients_sourced.md` has correct values; align CSV with that.

**2. Attendance definition (2021-22 discrepancy)**
- ESPN sum: 20,862,460
- SBJ/NBA paid: 20,910,813
- Difference: ~48k (definition of "paid" vs. "distributed")
- Action: Choose one definition and document it in column notes or a README.

**3. Media-rights source URLs (REQUIRED for Zotero)**
- Current: bare domains (`https://www.cnbc.com`, `https://pr.nba.com`, `https://variety.com`)
- Action: Convert to article-level URLs or drop the rows until article URLs can be sourced.

**4. Unsourced figures (MEDIUM PRIORITY)**
- BRI 2024-25 ($10.25B) — cite or drop
- Team revenue $12.75B — cite or drop
- Action: Attach Zotero keys or remove.

**5. Missing file**
- Request cites `league-income-sources.md` which doesn't exist in the coder's analysis/ folder
- Action: Create that file (one-pager listing source URLs and Zotero keys) or update request reference.

## Coder-01 Note on Data Quality

The nightshift log notes that `league_income_ingredients_sourced.md` (in coder's work) has correct cap/tax figures. The CSV discrepancy appears to be a labeling error (2025-26 row values placed on 2024-25 row). Fix is straightforward: swap or relabel.

The attendance discrepancy reflects a real definition choice (revenue-attributed vs. tickets sold). Once picked, it's defensible.

## Path B Deferred

Local media rights, licensing, and per-team revenue breakdowns are appropriately deferred to Path B. Once Path A is delivered, Path B can run in parallel with manuscript drafting of FIN 1–6 sections.

## Timeline

Fix items 1–3 before 2026-10-23 EOD to meet league-income chapter deadline. Items 4–5 can be addressed during Path B or in final integration.
