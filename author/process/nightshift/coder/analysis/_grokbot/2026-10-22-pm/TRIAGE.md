# Grokbot triage — 2026-10-22-pm (14 items)

**Status:** All items processed. 1 compact note written (`game_time/ft_pressure_cascade.md`). 5 research briefs grounded and ready for manuscript integration.

## Triage Results

| File | Type | Size | Destination | Finding | Action |
|---|---|---|---|---|---|
| `2026-10-22_nightshift-log.md` | metadata | 11.7 KB | reference | 6 requests processed; 48 Zotero items created; Zotero keys verified; coder-01 flagged salary-cap CSV error (critical 2026-10-23 deadline) | ✓ read |
| `2026-10-22_researcher-01_kinematic-variance-x-reinvestment.md` | literature brief | 9.7 KB | PLAYERS/reinvestment (future) | **No same-cohort basketball study** measures both Rusdiana kinematics + Kinrade reinvestment. Golf study (Malhotra 2015) found high reinvesters *less* variable (counter to hypothesis). Cascade is untested. | ✓ keep |
| `2026-10-22_researcher-02_ft-pressure-workload-nba.md` | analysis summary | 9.4 KB | `game_time/ft_pressure_cascade.md` | **Cascade NOT supported at outcome level.** Pressure effect real (~−2.5 pp late-close, −5.3 pp trailing). **No workload × pressure interaction** across 6 models (p-values .09–.85). 519,640 FT attempts, 2015-24. | ✓ summarized |
| `2026-10-22_researcher-02_code_1_build_ft.py` | code | 4.8 KB | archive/tools | Extract FT from stats.nba.com PBP (2015–2024), period/game context. Reproducible. | archive |
| `2026-10-22_researcher-02_code_2_enrich.py` | code | 3.4 KB | archive/tools | Merge minutes (reconstructed from subs), schedule, B2B flags. Reproducible. | archive |
| `2026-10-22_researcher-02_code_3_analyze.py` | code | 4.2 KB | archive/tools | Empirical Bayes baseline FT%, workload quartiles, context variables. Reproducible. | archive |
| `2026-10-22_researcher-02_code_4_robustness_and_proxies.py` | code | 4.1 KB | archive/tools | Logit models M1–M6, player-clustered SEs, CIs, average marginal effects. Reproducible. | archive |
| `2026-10-22_researcher-02_ft_models.csv` | results table | 17.6 KB | supporting data | 6 logit models: terms, coefs, SEs, CIs, p-values, AME (pp), n=519,640. Ready to cite in footnotes or appendix. | ✓ cite |
| `2026-10-22_researcher-02_ft_pressure_workload_summary.csv` | results table | 38.7 KB | supporting data | One row per season type × pressure context × workload split; n, makes, FT%, CI, expected from baseline, diff, source, confidence. Ready to cite or embed as table. | ✓ cite |
| `2026-10-22_researcher-02_ft_attempts_2015-2024.csv.gz` | raw data | 12.2 MB | skip | 519,640 attempt-level rows (gzipped). Summary CSV and models already extracted; no need to load binary for manuscript. | skip |
| `2026-10-22_researcher-03_automaticity-baseline-proxies.md` | literature brief | 6.7 KB | PLAYERS/skills (future) | Individual "choke gap" is **not stable** (r = 0.08 year-to-year; r = −0.09 split-half). Baseline FT% is stable (r = 0.88). No validated field-level automaticity measure in basketball lit. | ✓ keep |
| `2026-10-22_researcher-03_player_season_automaticity_proxies.csv` | results table | 785.7 KB | supporting data | One row per player-season (2015–24): low-pressure FT%, pressure FT%, gap, season start/end consistency, workload. Ready to cite or append as supplementary data. | ✓ cite |
| `2026-10-22_researcher-04_fatigue-executive-control.md` | literature brief | 10.9 KB | GAME TIME/fatigue (future) | **Exercise fatigue → executive control:** small, intensity-dependent effects. **Ego depletion → choking in FT** (Englert & Bertrams 2012, n=64) is strongest link. **Key twist:** Fatigue *specifically hurts explicitly learned skills* (Poolton 2007; Masters 2008; Banihosseini 2025), not implicit. Full chain untested. | ✓ keep |
| `2026-10-22_researcher-05_release-variability-under-pressure.md` | literature brief | 8.9 KB | GAME TIME/kinematics (future) | **Pressure → kinematics:** Cruz et al. 2026 is only direct test (n=24 youth). Mascret 2016 null. **Quiet-eye shortens under anxiety** (Wilson 2009), but no fatigue × pressure interaction on kinematics found. | ✓ keep |

## Zotero Verification

- **48 new items created** during grokbot run (tag: nightshift-2026-10-22); all DOIs verified via Crossref/OpenAlex.
- **Collections:** Exercise-cognition papers → hoops/physical or hoops/physical/recovery. Reinvestment theory → hoops/⭐psych/mental.
- **Keys cited in `ft_pressure_cascade.md`:** Cao/Price AAQT69K4, Toma DHQ9VHRN, Englert & Bertrams S5XB8I7S, Poolton V693HCNS, Masters PGRIUACI, Cruz 86WR2S8S, Malhotra 6NMFFTRA.

## Open Threads

1. **Coder-01 salary-cap error:** CSV off by one season (2024-25 cap is actually 2025-26). Deadline: 2026-10-23 EOD. Researcher must fix before approving FIN dataset build.
2. **Priority holes remain:** MEDIA (7% complete), FIN (10%), STADIUM (20%). Grokbot work addresses GAME TIME/PLAYERS only.
3. **Next hr batch:** Must target MEDIA, STADIUM, FIN primary sources (hoops_record for league-income ingredients; paperful_ask for national media rights 2025-26+, arena subsidy post-2010, sponsorship inventory).

**Status:** All 14 grokbot items triaged. 1 compact chapter note written. 5 research briefs grounded and ready. No junk; no duplicates. Proceed to priority holes.
