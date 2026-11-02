# CRITICAL FIX — Coder-01 Salary-Cap Data Error

**Deadline:** 2026-10-23 EOD

**Issue:** League-income-ingredients.csv shows row mislabeling for salary cap and luxury tax figures.

**Currently:**
- 2024-25 cap: $154.647M, tax $188.103M

**Should be:**
- 2024-25 cap: $140.588M, tax $170.814M
- 2025-26 cap: $154.647M, tax $187.895M (estimated)

**Source:** pr.nba.com official figures; coder's own `league_income_ingredients_sourced.md` has correct values.

**Action:** Align CSV with sourced markdown. This must be fixed before FIN chapter dataset build proceeds.

**Related issues (can be addressed in Path B):**
- Attendance definition (ESPN sum vs. SBJ/NBA paid figures)
- Media-rights source URLs (need article-level URLs, not bare domains)
- Unsourced figures (BRI 2024-25, team revenue 2024-25)
- Create `league-income-sources.md` (one-pager listing sources and Zotero keys)

**Status:** Researcher approved Path A with these conditions (2026-10-22).
