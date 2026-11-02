# HR Batch Triage — 2026-10-23

**Run:** 2026-10-22 pm → 2026-10-23 am  
**Status:** 8 requests; 1 ready, 2 failed (low yield expected), 3 failed (retriable), 2 pending validation

---

## Results Summary

### ✓ Done (Ready to Cite)
- **FT pressure cascade** (`analysis/game_time/ft_pressure_cascade.md`): −2.5pp late-close, −5.3pp trailing (p<.01, n=519,640). Use in GAME TIME § pressure context.

### ✗ Low Yield (Retriable—Gaps Confirmed)
1. **Paperful_ask #1** (NBA media rights 2025-26 Amazon Apple): 0 library matches  
   - Expected; library cut-off 2026-09-19, gap is real
   - Retry if external research time permits; else defer to future edition
   
2. **Paperful_ask #2** (NBA naming rights 2024-25): 0 specific 2024-25 data in library  
   - Library has 2017-18 jersey patch ($150M), historical Quicken Loans example only
   - Gap is real; requires vendor survey or external source

### ✗ Failed (Retriable—Technique Issues)
3. **Zotero_search #1 & #2** (Sinclair, Diamond Sports RSN): 0 results  
   - Generic terms may not match mirror index
   - Retry with vendor-specific keywords: "Sinclair Broadcasting", "Diamond Sports bankruptcy", "Bally Sports NBA"
   - If still 0, flag as mirror gap

4. **Hoops_record ×4** (Vegas, SoFi, Crypto.com, Intuit): 'path' parameter errors  
   - Schema fixed in codebase; retry with corrected param structure
   - Expect arena financing detail (public %, subsidy total, structure)

### ⏳ Pending (Validation)
5. **Zotero_get** (FIN/STADIUM key validation): 9 keys empty  
   - Check Crossref/OpenAlex existence for each key
   - If missing, flag as research gap (no invented sources)

---

## Critical Blocker

**Salary-cap CSV 2024-25 mislabeled**  
- File: `league-income-ingredients.csv` lines 18-20
- Current values: WRONG
- Official (pr.nba.com): cap $140.588M, tax $170.814M, aprons $156.228M / $176.228M
- **Action:** Researcher must correct before FIN chapter; researcher data gate
- **Deadline: TODAY (2026-10-23)**

---

## Next HR Batch (Revised Priority)

| Priority | Task | Rationale |
|----------|------|-----------|
| 1 | Zotero_get (validate 9 keys) | Unblocks Zotero retry for FIN/STADIUM |
| 2 | Zotero_search (vendor keywords) | Attempt RSN literature recovery |
| 3 | Hoops_record (retry 4 cases) | Fixed schema; expect financing detail |
| 4 | Paperful_ask (media rights/sponsors) | Low yield expected; defer if tight |

---

## Researcher Handoff

1. **Today (2026-10-23):** Fix salary-cap CSV; FIN chapter gated until done
2. **After Zotero validation:** Review 9 keys; update nightshift if sources truly missing
3. **After hoops_record retry:** Integrate post-2010 arena financing into FIN + STADIUM
4. **Manuscript:** Use FT pressure cascade in GAME TIME; reconcile endnotes (38k w) vs bibliography (464 w)
