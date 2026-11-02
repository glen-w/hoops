# MEDIA / FIN / STADIUM Priority Roadmap — 2026-10-23

## Status: Critical Path Issues + Ready Handoffs

### IMMEDIATE (Today 2026-10-23)

**DONE — Salary-cap CSV fix [critical blocker]**
- Corrected file: `analysis/fin/league_income_ingredients_corrected_2024-25.csv`
- Values: 2024-25 cap $140.588M, tax $170.814M, first apron $178.132M, second apron $188.931M
- Action: merge into main `league_income_ingredients.csv` (or replace with corrected version)
- Methodology: `analysis/fin/league_income_ingredients_sourced.md` (pr.nba.com official)

**READY TO HANDOFF — FT Pressure Integration**
- Free-throw outcome pressure real and small (−2.5pp late-close, −5.3pp trailing, p<.01)
- Workload × pressure interaction NULL (p>.05; cascade hypothesis NOT supported)
- Summary: `analysis/game_time/ft_pressure_integration_coder_note.md`
- Supporting data: 3 CSV files + 4 reproducible Python scripts in `_grokbot/2026-10-22-pm/`
- Zotero keys verified (48 items, tag: nightshift-2026-10-22)
- **Do NOT wait for other batches—integrate to GAME TIME immediately**

---

### HIGH PRIORITY (This Week)

**MEDIA: 2025-26 Cycle [retry split queries, library gap confirmed]**
- Issue: paperful_ask broad query returned pre-2024 refs only; 2025-26 not in hoops library
- Retry strategy:
  1. `paperful_ask "Amazon Prime Video NBA 2024-2025 media rights deal"`
  2. `paperful_ask "Apple TV+ NBA basketball streaming 2024 rights"`
  3. `paperful_ask "ESPN+ TNT streaming carriage 2024-25 fees"`
- Expect: low yield (library lag ~2 years)
- Scope decision: if found, add as forward footnote per manuscript cutoff 2026-09-19; do NOT backfill pre-2024 narrative
- Impact: MEDIA chapter ~7% written; needs 2025-26 context + 2024 final FCC approval timeline

**MEDIA: Naming Rights + Jersey Sponsors [retry split, timeout risk]**
- Issue: previous paperful_ask (180s timeout); found only pre-2020 values
- Retry strategy:
  1. `paperful_ask "NBA arena naming rights sponsors 2024-25 inventory by team"`
  2. `paperful_ask "NBA jersey patch apparel sponsor 2024-25 deals"`
- Expect: timeout risk + low yield if library lacks post-2020 inventory
- Impact: MEDIA chapter needs current sponsor counts and values (2024-25 snapshot)

**FIN/STADIUM: Zotero Key Validation [researcher action, blocks coder retry]**
- Issue: 9 post-2010 arena subsidy refs returned empty from zotero_get batch
- Keys: Vegas Allegiant 2020, SoFi 2020, Crypto.com 2019, Intuit 2024 (missing detail: public %, total subsidy, financing)
- Researcher action:
  1. Confirm each key exists in hoops Zotero library AND has data
  2. Check Crossref/OpenAlex for missing entries
  3. If entry missing entirely, flag as research gap (no invented sources)
  4. Once validated, coder runs zotero_get retry with confirmed keys
- Impact: FIN/STADIUM chapters blocked pending validation

**FIN/STADIUM: hoops_record Arena Cases [debug then retry]**
- Issue: all 4 cases returned 'path' error in 2026-10-22 batch (Vegas, SoFi, Crypto.com, Intuit)
- Coder action:
  1. Debug hoops_record path parameter format (likely venue-name-year mismatch)
  2. Test single Vegas case with corrected params
  3. If fixed, retry full batch; if error persists, escalate + use paperful_ask fallback
- Fallback: paperful_ask for architectural/financing context per venue
- Impact: STADIUM chapter financing detail + FIN subsidy breakdown blocked

---

### MEDIUM PRIORITY (Week 2)

**RSN / Regional Sports Networks [confirmed research gap]**
- Issue: zotero_search 'Sinclair', 'Diamond Sports', 'Bally' all returned 0 items
- Finding: hoops library lacks vendor/bankruptcy literature (post-2023 collapse outside academic scope)
- Action: if researcher has access to gray sources (SEC filings, Bloomberg, industry reports), pull vendor landscape; otherwise mark as out-of-scope
- Impact: MEDIA chapter section on local broadcast erosion incomplete (academic coverage sparse)

**Zotero Reconciliation [endnotes 38k vs bibliography 464 w]**
- Issue: endnotes far exceed bibliography word count; likely duplicates/incomplete entries
- Researcher action: audit hoops Zotero for duplicates, missing URLs, incomplete citations
- Consolidate oversized blocks first: PRE-GAME/history (9.5k), GAME TIME/skills (7.6k), SOCIETY/race (4.8k), PLAYERS/paths+characteristics (~8k)
- Re-measure word counts before citing manuscript
- Impact: bibliography cleanup needed before final submission

---

## Chapter Completion Snapshot (2026-10-22)

| Chapter | % Complete | Status | Gap |
|---|---|---|---|
| MEDIA | 7% | Essentially unwritten | 2025-26 cycle, current sponsors, RSN landscape |
| FIN | 10% | Essentially unwritten | Post-2010 arena subsidy cases, sponsorship values |
| STADIUM | 20% | Underdeveloped | Financing breakdown (public/private/PSLs), team impact |
| SOCIETY (non-race) | 0% | Missing | Capitalism, sustainability frameworks |
| TEAM / draft | 30% | Weak | Draft mechanics, selection processes |
| ANALYTICS | 30% | Weak | Core argument sections |
| Transitions | 0% | Missing | "an attempt..." bridge, "TO – ballhaus" section |

---

## Research Boundary (Scope Respected)

- **Library cutoff:** pre-2024 (confirmed 2026-10-22)
- **Manuscript cutoff:** 2026-09-19 (Europe/Paris)
- **Rule:** No invented sources; new sources → nightshift_requests first
- **2025-26 decision:** If found, add as footnote; do NOT backfill pre-2024 backbone
- **Gray literature:** OK for RSN/vendor landscape if researcher sourced; otherwise out-of-scope

---

## Blockers Summary

| Blocker | Status | Owner | ETA |
|---|---|---|---|
| Salary-cap CSV mislabeling | ✓ READY | Researcher merge | 2026-10-23 EOD |
| FT pressure integration | ✓ READY | Researcher integrate | 2026-10-23 (do not wait) |
| paperful_ask split (MEDIA 2025-26) | Pending | Coder retry | 2026-10-24 |
| paperful_ask split (sponsors) | Pending | Coder retry | 2026-10-24 |
| Zotero key validation (9 arena refs) | Blocked | Researcher validate | 2026-10-24 |
| hoops_record path error (4 arenas) | Blocked | Coder debug + retry | 2026-10-24 |
| RSN gray literature | Medium | Researcher source | 2026-10-25 (optional) |

---

## Next Handoff to Researcher

1. **Merge salary-cap CSV today**
2. **Integrate FT pressure to GAME TIME immediately** (do not wait for other batches)
3. **Validate 9 Zotero keys** (arena subsidy refs)—confirm in Zotero + Crossref
4. Once Zotero validated, coder will retry hoops_record arena batch
