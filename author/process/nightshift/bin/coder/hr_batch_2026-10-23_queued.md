# HR Batch Queue — 2026-10-23

**Status:** Ready to execute. Coder triage complete; 14 Grokbot items mapped. Next: HR queries to fill MEDIA/FIN/STADIUM holes.

---

## Queue Order (High to Low Impact)

### 1. Paperful_ask ×3 (Media Rights + Sponsors)
**Reason:** Avoid 180s timeout; split narrow queries.

- Query (a): "NBA media rights deals 2025-26 Amazon Apple streaming"
- Query (b): "NBA streaming landscape 2025-26 TNT ESPN+ cable decline"
- Query (c): "NBA naming rights arena sponsors jersey apparel 2024-25"

### 2. Zotero_search ×2 (RSN Consolidation)
**Reason:** Vendor keywords; prior search returned 0 items.

- Query (a): "Sinclair Broadcasting NBA regional sports 2023-26"
- Query (b): "Regional sports network bankruptcy 2023-24 Diamond Sports Bally"

### 3. Hoops_record ×4 (Post-2010 Arena Cases)
**Reason:** Schema fixed; test 1 case first, then batch remaining 3.
**Keys needed:** public_pct, total_subsidy, financing_structure

- Vegas: Allegiant Stadium Raiders 2020
- SoFi: Los Angeles Rams/Chargers 2020
- Crypto.com: Los Angeles Lakers/Kings 2019
- Intuit: San Francisco Warriors 2024

### 4. Zotero_get (FIN/STADIUM Key Validation)
**Status:** Pending. Need 9 empty key list from researcher.
**Action:** Validate Crossref/OpenAlex entry exists; if missing, flag research gap (no invented sources).

---

## Blocker (Researcher Action, Deadline 2026-10-23)
**Salary-cap CSV 2024-25 correction required before FIN integration.**
- File: league-income-ingredients.csv lines 18-20
- Official pr.nba.com values: cap $140.588M, tax $170.814M, aprons $156.228M/$176.228M
- Sources: pr.nba.com PRs 2024-10-08, 2024-06-27

---

## Integration Timeline (After HR Returns)
| Chapter | Status | Blocker |
|---------|--------|---------|
| GAME TIME | 40% → Ready | none (FT pressure cascade ready) |
| FIN | 10% → Pending | CSV correction + hoops_record + Zotero key validation |
| STADIUM | 20% → Pending | hoops_record + architectural context (paperful_ask post-2010) |
| MEDIA | 7% → Pending | paperful_ask (3 queries) + zotero_search (RSN) |
