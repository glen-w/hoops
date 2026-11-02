# FT Pressure Ready to Cite — GAME TIME Integration Note

**Status:** Ready to integrate. Do not wait for other batches.

**Key Finding:** Free-throw % drops under pressure are small but real and significant.
- Late & close (≤60s, ≤3pt margin): −2.5pp, p<.01, n=9,824
- Late & close *and trailing*: −5.3pp, p<.01, n=2,549
- Clutch (≤5 min, ≤5 pts, not late-close): −0.8pp, p<.01, n=23,779
- Playoffs: −0.8pp, p<.01, n=34,197

**Replication:** Matches Cao et al. 2011 (5–10pp final seconds) and Toma 2017 (−3.1pp final 30s). Our window is slightly wider (60s vs 30s), explaining smaller magnitude.

**Critical Finding:** Workload does NOT amplify pressure dip.
- Clutch × top-quartile season minutes: +0.4pp, p=.55
- Clutch × back-to-back: p=.85
- Clutch × in-game minutes: p=.43
- Late-close × back-to-back: −2.0pp, p=.09 (confidence interval spans zero; candidate for pre-registered re-test, not a claimed effect)

**Implications:** Cascade hypothesis (Hore workload → Rusdiana kinematics → Kinrade reinvestment) is NOT supported at outcome level. Kinematics/reinvestment untested in this dataset. Cite as: "NBA play-by-play outcome data show pressure effects but no workload amplification; kinematics and reinvestment paths remain unexplored in this grain."

## Supporting Files

| File | Role |
|---|---|
| `2026-10-22_researcher-02_ft_pressure_workload_summary.csv` | Descriptive table: n, FT%, baseline-adjusted diff (pp), 95% CI, p-value per season-type × pressure × workload split |
| `2026-10-22_researcher-02_ft_models.csv` | Logistic models M1–M6: coefficients, player-clustered SEs, CIs, p, marginal effects in pp |
| `2026-10-22_researcher-02_ft_attempts_2015-2024.csv.gz` | Attempt-level data (519,640 rows, 12 MB): game context, rest days, reconstructed minutes, shooter baseline |
| `2026-10-22_researcher-02_code_*.py` | Four pipeline scripts (build, enrich, analyze, robustness); reproducible pull from shufinskiy/nba_data mirror |

## Data & Methodology

**Source:** stats.nba.com play-by-play and shot-detail logs (mirrored at github.com/shufinskiy/nba_data).
**Coverage:** 2015-16 to 2023-24, regular season + playoffs; 11,496 games; 519,640 free-throw attempts.
**Validation:** League FT% by season matches published figures (75.6% in 2015-16 → 78.4% in 2023-24).

**Pressure definitions:**
- *Late-close:* 4th quarter or OT, ≤60s left, margin ≤3
- *Clutch:* NBA definition (≤5 min, ≤5 pts) excluding late-close
- *Low-pressure:* quarters 1–3 or margin ≥20

**Workload measures:**
- Season minutes (quartiled)
- Back-to-back (team-level, prior calendar day)
- Cumulative minutes before the game
- In-game minutes before the attempt

**Shooter baseline:** Logit-scale FT% computed leave-one-out per player per season, shrunk toward league mean (k=20). Clutch shots taken disproportionately by good shooters (deliberate fouls on weak shooters), so baseline adjustment critical.

**Models:** Logistic regression with baseline logit, second-of-pair, technical, season FE, context and workload terms. SEs clustered by player.

## Zotero Keys (48 items, tag: nightshift-2026-10-22)

Literature cited:
- Cao et al. 2011 [AAQT69K4]: Performance under pressure in the NBA (2002-03 to 2009-10)
- Toma 2017 [DHQ9VHRN]: Missed shots at the free-throw line (NBA, WNBA, NCAA)
- Steenland & Deddens 1997 [K6C2ACJD]: Effect of travel and rest on performance
- Esteves et al. 2021 [NBMVPIVS]: Basketball performance affected by schedule congestion
- Arkes 2010 [V3JBJL69]: Hot hand theory with free throw data
- Lantis & Nesson 2021 [ALJSJCYA]: Hot shots—NBA FG and FT shooting
- Morgulev & Galily 2018 [BQ4BBNT7]: Choking or delivering under pressure (elimination games)

See 2026-10-22_researcher-02_ft-pressure-workload-nba.md for full literature section.

## What NOT to claim

- Workload does not explain pressure sensitivity (interaction p>.05)
- This dataset cannot separate fatigue from selection (coaches play in-form players)
- Cascade hypothesis (kinematics, reinvestment) is untested
- Back-to-back × pressure hint (p=.09) is not a confirmed effect
