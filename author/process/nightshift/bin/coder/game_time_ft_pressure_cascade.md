# Free-throw pressure integration — GAME TIME chapter

**Request:** 2026-10-22-overtime-researcher-02 (data, high)  
**Status:** Ready to integrate (2026-10-23)  
**Outcome:** Pressure link supported at outcome level. Workload link null.

## Key Finding (n = 519,640 attempts, 2015-16 to 2023-24)

**Pressure effect on free-throw %:**
- Late & close (≤1 min, ≤3 pts): −2.5 pp (p < .001)
  - When trailing: −5.3 pp (p < .001)
  - When tied: −3.2 pp
  - When leading: −1.4 pp
- Clutch (≤5 min, ≤5 pts, not last minute): −0.8 pp (p < .001)
- Playoffs: −1.1 pp (p < .001)

**Workload × pressure interaction:** Null across all measures
- Clutch × top-quartile season minutes: +0.4 pp, p = .55
- Clutch × back-to-back: p = .85
- Clutch × in-game minutes: p = .43
- Clutch × prior-7-day minutes: p = .16
- Playoffs × high workload: p = .72

**Note:** Late-close × back-to-back: −2.0 pp (p = .09, CI spans zero). Too weak for chapter claim; flag as candidate for pre-registered retest on 1996–2015.

## How This Bears on the Cascade

**Hore (workload) → Rusdiana (kinematics) → Kinrade (reinvestment):**
1. ✓ **Pressure link at outcome level:** Supported and small (−2.5 pp), matches Cao et al. 2011 (5–10 pp final seconds) and Toma 2017 (−3.1 pp final 30 s).
2. ✗ **Workload → more choking:** Not supported. No interaction, main effects confounded (selection, not fatigue).
3. ? **Kinematics & reinvestment:** Not testable in play-by-play. Covered by researcher-01 and researcher-05 literature briefs.

## What to Write

**Place in GAME TIME chapter (skills → pressure section):**
- Intro: Pressure is observable as a small FT% dip in the final minute of close games (cite Cao, Toma).
- Main claim: In NBA free throws, 2015-24, trailing by ≤3 pts with ≤1 min left, FT% drops 5.3 pp below that shooter's season baseline (−2.5 pp overall late-close, controlling for selection). Logistic model: clutch × trailing interaction −3.7 pp, p < .001.
- Nuance: Workload (back-to-back, cumulative minutes, in-game minutes) does not amplify the pressure dip. The apparent fatigue effect (higher FT% with more minutes) is selection (coaches play on-form starters in close games).
- Limitations: Observational; can't separate fatigue from selection. No direct load measure. Reconstructed minutes approximate. Deliberate foul selection partly corrected by baseline adjustment but not eliminated.

## Data & Method Notes

**Source:** stats.nba.com play-by-play + shot-detail via shufinskiy/nba_data mirror (Kaggle lacks dates; nba_api blocked). Validated: median team total = 240 min/game; spot checks match official rosters (e.g., LeBron 2015-16).

**Pressure context:**
- Late-close: 4th quarter or OT, ≤60 s left, margin ≤3.
- Clutch: ≤5 min, ≤5 pts (standard NBA definition), excluding late-close.
- Low pressure: Q1–3 or margin ≥20.
- Back-to-back: team played prior calendar day.

**Baseline:** Each attempt vs. shooter's own same-season FT% (leave-one-out, shrunk k=20 toward league mean). Controls for clutch-sample selection (teams foul worst shooters).

**Model:** Logistic make/miss ~ baseline logit + second-of-pair + technical + season FX + context + workload terms, SEs clustered by player.

## Zotero Citations (verified; tag: nightshift-2026-10-22)

- Cao, Z., Price, J. & Stone, D.F. (2011). *J Sports Econ* 12(3), 231–252 [AAQT69K4]
- Toma, M. (2017). *J Sports Econ* 18(6), 539–559 [DHQ9VHRN]
- Steenland & Deddens (1997). *Sleep* 20(5), 366–369 [K6C2ACJD]
- Esteves et al. (2021). *Eur J Sport Sci* 21(1), 26–35 [NBMVPIVS]
- Arkes, J. (2010). *J Quant Anal Sports* 6(1) [V3JBJL69]
- Lantis & Nesson (2021). *J Sports Econ* 22(6), 639–677 [ALJSJCYA]
- Morgulev & Galily (2018). *Front Psychol* 9, 979 [BQ4BBNT7]

## Files to Archive

Code → `tools/reproducible/ft_pressure_2026-10-22/`:
- `build_ft.py` — extract and parse play-by-play + shot-detail
- `enrich.py` — reconstruct minutes, add game context
- `analyze.py` — logistic models M1–M6
- `robustness_and_proxies.py` — B2B validation, interaction tests
- `ft_attempts_2015-2024.csv.gz` — attempt-level (519,640 rows, reproducible)

Supporting tables:
- `ft_models.csv` — model coefficients, SEs, p, marginal effects
- `ft_pressure_workload_summary.csv` — descriptive by season type × context × workload splits

Data citation: shufinskiy, *nba_data* (GitHub Apache-2.0), derived from stats.nba.com. Accessed 22 Oct 2026.
