# Coder Tick 2026-10-23 — Status Report

**Grokbot 2026-10-22-pm:** All 14 items triaged. 6 items archived (code), 5 kept (literature + data tables), 3 skipped (raw data).

## Completed Today

1. **FT Pressure Integration Ready** ✓
   - Free-throw % pressure effect confirmed: −2.5pp late-close, −5.3pp trailing (p<.01, n=519,640 attempts)
   - Workload × pressure interaction NULL across 6 logistic models (p>.05)
   - 48 Zotero keys verified (tag: nightshift-2026-10-22)
   - Files: `ft_pressure_cascade.md` (summary), `ft_pressure_integration_coder_note.md` (full), `_grokbot/2026-10-22-pm/` (code + data)
   - **Handoff:** Researcher integrates to GAME TIME immediately, do not wait for other batches

2. **Salary-Cap CSV Corrected** ✓
   - 2024-25: cap $140.588M, tax $170.814M (was mislabeled with 2025-26)
   - File: `analysis/fin/league_income_ingredients_corrected_2024-25.csv`
   - **Handoff:** Researcher merge to main file by 2026-10-23 EOD (blocks FIN pipeline)

3. **Hoops Status Updated** ✓
   - Reflects Grokbot findings + roadmap
   - MEDIA 7%, FIN 10%, STADIUM 20% complete
   - Library gaps confirmed: 2025-26 cycle, post-2010 arena subsidy detail, sponsorship inventory
   - Ready for researcher review

4. **nightshift_requests.json Current** ✓
   - 7 items tracked: 1 critical (salary-cap, now done), 2 high (MEDIA splits), 2 high (FIN/STADIUM), 1 medium (RSN), 1 medium (Zotero audit)
   - All prioritized, status updated

## Queued for 2026-10-24

### Coder Actions
1. **Paperful_ask MEDIA 2025-26 cycle** (split queries)
   - Query 1: "Amazon Prime Video NBA 2024-2025 media rights deal"
   - Query 2: "Apple TV+ NBA basketball streaming 2024 rights"
   - Query 3: "ESPN+ TNT streaming carriage 2024-25 fees"
   - Expect: low yield (library lag ~2 years); add as footnote if found

2. **Paperful_ask MEDIA sponsorship inventory** (split queries)
   - Query 1: "NBA arena naming rights sponsors 2024-25 inventory by team"
   - Query 2: "NBA jersey patch apparel sponsor 2024-25 deals"
   - Expect: low yield + timeout risk; retry separately if needed

3. **Debug hoops_record arena path format**
   - Issue: all 4 venue cases returned path error in 2026-10-22 batch
   - Action: test Vegas single case first, fix parameter format (likely venue-name-year mismatch)
   - Fallback: paperful_ask if error persists
   - Unblocks: FIN/STADIUM financing detail once Zotero keys validated

### Researcher Actions (2026-10-23–24)
1. Merge salary-cap CSV to main file by EOD today
2. Integrate FT pressure to GAME TIME immediately (citations ready)
3. Validate 9 Zotero keys for post-2010 arena subsidy refs (Vegas, SoFi, Crypto.com, Intuit)
4. Confirm each key exists in hoops library + has detail; check Crossref/OpenAlex if needed

## Open Threads

- **FT pressure integration deadline:** None (proceed immediately)
- **Salary-cap CSV deadline:** 2026-10-23 EOD (researcher)
- **MEDIA/FIN retries:** 2026-10-24 (coder queued)
- **Arena Zotero validation:** 2026-10-24 (researcher, blocks coder hoops_record retry)
- **RSN gray literature:** 2026-10-25 optional (researcher, if accessible)

## Data Paths for Researcher

- **FT pressure full analysis:** `analysis/game_time/ft_pressure_integration_coder_note.md`
- **Citable summary:** `analysis/game_time/ft_pressure_cascade.md` (one-liner)
- **Supporting CSV:** `_grokbot/2026-10-22-pm/2026-10-22_researcher-02_ft_pressure_workload_summary.csv`
- **Reproducible code:** `_grokbot/2026-10-22-pm/2026-10-22_researcher-02_code_*.py` (4 scripts)
- **Raw data:** `_grokbot/2026-10-22-pm/2026-10-22_researcher-02_ft_attempts_2015-2024.csv.gz` (519,640 rows)

## Biggest Holes (Priority)

1. **MEDIA** 7% — 2025-26 cycle + sponsorship inventory; paperful_ask retries start 2026-10-24
2. **FIN** 10% — post-2010 arena subsidy cases; Zotero validation blocks hoops_record retry
3. **STADIUM** 20% — financing breakdown; same blocker as FIN
4. **SOCIETY** (non-race) + **ANALYTICS** core — medium priority, research gap investigation

Next: researcher merge salary-cap, integrate FT pressure; coder retries paperful_ask + debug hoops_record 2026-10-24.
