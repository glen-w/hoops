# Grokbot triage — 2026-10-22-pm (researcher lane, 14 items)

**Status:** All items processed. 5 research briefs marked done; incorporation targets noted. 4 code/data files archived. No junk or duplicates.

## Triage Results

| File | Type | Size | Destination | Finding | Action |
|---|---|---|---|---|---|
| `2026-10-22_nightshift-log.md` | metadata | 11.7 KB | reference | 6 requests processed; Zotero keys verified; coder-01 flagged salary-cap CSV error (critical 2026-10-23 deadline) | ✓ read |
| `2026-10-22_researcher-01_kinematic-variance-x-reinvestment.md` | literature brief | 9.7 KB | GAME TIME/PLAYERS (reinvestment future) | **No same-cohort basketball study** measures both Rusdiana kinematics + Kinrade reinvestment. Golf study (Malhotra 2015) found high reinvesters *less* variable. Cascade is untested. | ✓ done |
| `2026-10-22_researcher-02_ft-pressure-workload-nba.md` | analysis summary | 9.4 KB | GAME TIME/PLAYERS (grounded) | **Cascade NOT supported at outcome level.** Pressure effect real (~−2.5 pp late-close, −5.3 pp trailing). **No workload × pressure interaction** (p-values .09–.85). 519,640 FT attempts, 2015-24. | ✓ done |
| `2026-10-22_researcher-02_code_1_build_ft.py` | code | 4.8 KB | archive | Extract FT from stats.nba.com PBP (2015–2024), period/game context. Reproducible pipeline. | archive |
| `2026-10-22_researcher-02_code_2_enrich.py` | code | 3.4 KB | archive | Merge minutes (reconstructed from subs), schedule, B2B flags. Reproducible. | archive |
| `2026-10-22_researcher-02_code_3_analyze.py` | code | 4.2 KB | archive | Empirical Bayes baseline FT%, workload quartiles, context variables. Reproducible. | archive |
| `2026-10-22_researcher-02_code_4_robustness_and_proxies.py` | code | 4.1 KB | archive | Logit models M1–M6, player-clustered SEs, CIs, AME. Reproducible. | archive |
| `2026-10-22_researcher-02_ft_models.csv` | results table | 17.6 KB | supporting data | 6 logit models: terms, coefs, SEs, CIs, p-values, AME (pp), n=519,640. Ready to cite in footnotes or appendix. | cite |
| `2026-10-22_researcher-02_ft_pressure_workload_summary.csv` | results table | 38.7 KB | supporting data | One row per season type × pressure context × workload split; n, makes, FT%, CI, expected, diff. Ready to cite or embed as table. | cite |
| `2026-10-22_researcher-02_ft_attempts_2015-2024.csv.gz` | raw data | 12.2 MB | skip | 519,640 attempt-level rows (gzipped). Summary and models extracted; no need for binary in manuscript. | skip |
| `2026-10-22_researcher-03_automaticity-baseline-proxies.md` | literature brief | 6.7 KB | PLAYERS/ANALYTICS (skills/evaluation) | Individual "choke gap" is **not stable** (r = 0.08 year-to-year). Baseline FT% is stable (r = 0.88). No validated field-level automaticity measure in basketball. | ✓ done |
| `2026-10-22_researcher-03_player_season_automaticity_proxies.csv` | results table | 785.7 KB | supporting data | One row per player-season (2015–24): low-pressure FT%, pressure FT%, gap, consistency, workload. Ready to append as supplementary data. | cite |
| `2026-10-22_researcher-04_fatigue-executive-control.md` | literature brief | 10.9 KB | GAME TIME/PLAYERS (fatigue, psychology) | **Exercise fatigue → executive control:** small effects. **Ego depletion → choking in FT** (Englert & Bertrams) strongest link. **Key:** Fatigue hurts *explicitly learned skills* (Poolton, Masters), not implicit. Full chain untested. | ✓ done |
| `2026-10-22_researcher-05_release-variability-under-pressure.md` | literature brief | 8.9 KB | GAME TIME/PLAYERS (kinematics) | **Pressure → kinematics:** Cruz et al. 2026 is only direct test (youth, n=24). **Quiet-eye shortens under anxiety** (Wilson 2009). **NO fatigue × pressure kinematics interaction found.** Need Cruz full text to settle release-variability direction. | ✓ done |

## Researcher Open Threads

1. **shufinskiy/nba_data GitHub source:** Researcher-02 analysis cites stats.nba.com PBP via GitHub mirror (Apache-2.0). Not yet in Zotero. Needed before 519k FT figures cited in manuscript.
2. **Cruz et al. 2026 full text:** Researcher-05 abstract unclear on whether release *variability* increased or decreased under pressure. Need Sci Rep article (https://doi.org/10.1038/s41598-026-51871-7, tentative key 86WR2S8S) to confirm kinematic direction.

## Integration Points

- **GAME TIME:** ft_pressure_cascade.md (grounded outcome-level analysis, no interaction); fatigue section (exercise → exec control small effects, ego depletion → choking stronger). Kinematics section awaits Cruz full text.
- **PLAYERS:** Reinvestment section (cascade untested); psychology/pressure section (ego depletion effect); skills/automaticity section (choke gap not stable year-to-year); workload section (no pressure × workload interaction in outcomes).
- **ANALYTICS:** Player-evaluation section (automaticity not rankable from outcomes); outcome-level testing (519k FT validation).

**Status:** All 14 grokbot items triaged. 5 research briefs grounded and ready for integration. 2 open threads (Zotero entries) pending. Proceed to priority holes: MEDIA, STADIUM, FIN.
