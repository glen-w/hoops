# Coder Triage — 2026-10-23

## Grokbot 2026-10-22-pm: All 14 Items Processed

**Status:** Triage complete. INDEX verified. All items grounded, no junk.

### Ready Handoffs (Do NOT wait)
1. **FT Pressure → GAME TIME** (−2.5pp late, −5.3pp trailing, n=519,640, p<.01)
   - Cite: analysis/game_time/ft_pressure_cascade.md (1-liner verified)
   - Supporting: 3 CSVs + 4 Python scripts in _grokbot/2026-10-22-pm/
   - Zotero: 48 items tagged (nightshift-2026-10-22); all verified Crossref/OpenAlex
   - Action: Researcher integrate ASAP; workload×pressure interaction null (cascade NOT supported)

2. **Salary-Cap CSV Corrected** (deadline 2026-10-23 EOD)
   - File: analysis/fin/league_income_ingredients_corrected_2024-25.csv
   - Values: 2024-25 cap $140.588M, tax $170.814M (was mislabeled)
   - Action: Researcher merge into main CSV; source: pr.nba.com official

### Literature Briefs Queued (Future Chapters)
- 2026-10-22_researcher-01_kinematic-variance-x-reinvestment.md → PLAYERS/reinvestment
- 2026-10-22_researcher-03_automaticity-baseline-proxies.md → PLAYERS/skills  
- 2026-10-22_researcher-04_fatigue-executive-control.md → GAME TIME/fatigue
- 2026-10-22_researcher-05_release-variability-under-pressure.md → GAME TIME/kinematics

### Confirmed Research Gaps (No Backfill)
**MEDIA:** Library pre-2023 cutoff. 5 paperful_ask queries all returned 0 results:
- 2024-25 streaming cycle (Amazon Prime, Apple TV+, ESPN+ TNT) → NOT in library
- Naming rights + jersey patch inventory 2024-25 → pre-2020 only in library
- RSN vendor landscape (Sinclair/Diamond/Bally) → post-2023 outside academic scope

**FIN/STADIUM:** Zotero key validation needed before proceeding.
- Vegas Allegiant 2020, SoFi 2020, Crypto.com 2019, Intuit 2024: confirm exist + have detail
- hoops_record path format debug: test Vegas case first (all 4 returned errors)

## Coder Next Actions (Priority)
1. **2026-10-24 AM:** Debug hoops_record venue-name-year format; test Vegas case
2. **2026-10-24 PM:** Once Zotero validated (researcher), retry zotero_get arena batch
3. **2026-10-24+:** Assess MEDIA split query retry (pending researcher scope decision on 2025-26)

## Chapter Holes (Biggest First)
1. **MEDIA** 7% — confirmed library gap; manual sourcing or out-of-scope
2. **FIN** 10% — blocked on Zotero key validation + hoops_record fix
3. **STADIUM** 20% — blocked on arena subsidy detail
4. **SOCIETY** (non-race) — capitalism/sustainability missing (not blocked, lower priority)
5. **ANALYTICS** — core argument sections weak (existing library coverage)

## Tracking
- Analysis requests logged: analysis/nightshift_requests.json (7 items, status updated)
- Open threads: 1 (hoops_status.md clobbered — full review needed post-integration)