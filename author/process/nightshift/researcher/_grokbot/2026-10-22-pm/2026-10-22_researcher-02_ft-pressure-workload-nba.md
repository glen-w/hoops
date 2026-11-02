# NBA free-throw % by pressure context vs workload, 2015-16 to 2023-24

**Request:** 2026-10-22-overtime-researcher-02 (data, high)
**Status:** done. This is a real pull, about 520k attempts. It tests the Hore → Rusdiana → Kinrade "cascade" at outcome level only, and **the cascade prediction is not supported**.

## Files
| File | What |
|---|---|
| `2026-10-22_researcher-02_ft_pressure_workload_summary.csv` | A tidy summary. One row per season type × pressure context × split (season-minutes quartile, back-to-back, in-game minutes before the free throw). Columns: n, makes, FT%, Wilson 95% CI, **expected FT% from the shooters' own baselines**, observed minus expected (pp), `source`, `confidence`. |
| `2026-10-22_researcher-02_ft_models.csv` | Logistic models M1–M6. Columns: coefficients, player-clustered SEs, CIs, p, approximate average marginal effect in pp, `source`, `confidence`. |
| `2026-10-22_researcher-02_ft_attempts_2015-2024.csv.gz` | Attempt-level data (519,640 rows, 12 MB gzipped), with game context, rest days, reconstructed minutes and the shooter baseline, for the coder to slice further. |
| `2026-10-22_researcher-02_code_*.py` | The four pipeline scripts, so the pull is reproducible. |

## Data and methods (short)
- **Source.** stats.nba.com play-by-play and shot-detail logs, mirrored at `github.com/shufinskiy/nba_data`. stats.nba.com itself blocks my box, so `nba_api` wasn't usable. The Kaggle 2006–16 free-throw set needs a login and lacks dates and minutes, so I used this mirror instead.
  - Coverage: 9 seasons, regular season plus playoffs (play-in excluded); 11,496 games; 519,640 free-throw attempts.
  - Check: league FT% by season matches published league figures (75.6% in 2015-16 rising to 78.4% in 2023-24).
- **Pressure context.** Pre-shot score margin from the running score, from the shooter's side.
  - *late_close*: 4th quarter or OT, ≤60 s left, margin ≤3.
  - *clutch_other*: the NBA's "clutch" definition (≤5 min, ≤5 pts) excluding late_close.
  - *low_pressure*: quarters 1–3, or a margin of 20 or more.
  - *playoffs*: separate flag.
- **Back-to-back.** The team played the previous calendar day (dates from shot-detail logs). Teams average about 12–18 B2Bs per season, which matches league schedules.
- **Workload.** Player minutes are **reconstructed from substitution events**. Period starters are inferred from first appearance, the standard approach.
  - Validation: the median team total is exactly 240 min per game, and spot checks match official totals (e.g. LeBron 2015-16 2,709 min over 76 games; Jokić 2022-23 2,324 min).
  - Measures: (a) season regular-season minutes → within-season quartile; (b) cumulative minutes before the game; (c) minutes in the prior 7 days; (d) **in-game minutes on court before the free throw**.
- **Shooter baseline.** Each attempt is compared with the shooter's own same-season FT% computed *leaving that attempt out* and shrunk toward the league mean (k = 20). Clutch free throws are taken disproportionately by good shooters, partly because teams foul the worst shooter, so raw FT% comparisons mislead.
- **Models.** Logistic regression of make/miss on the baseline logit, plus second-of-pair, technical and season fixed effects, plus context and workload terms. SEs are clustered by player.

## Results
**1. Pressure: a small, real dip, concentrated in the last minute and when trailing.**

| Context (all seasons) | n | FT% | Expected from shooter | Diff |
|---|---|---|---|---|
| All attempts | 519,640 | 77.3% | 77.5% | −0.2 pp |
| Low pressure | 387,368 | 77.3% | 77.4% | 0.0 pp |
| Clutch (≤5 min, ≤5 pts; not last minute) | 23,779 | 77.7% | 78.5% | −0.8 pp |
| Late & close (≤1 min, ≤3 pts) | 9,824 | 77.5% | 80.0% | **−2.5 pp** |
| ↳ shooter's team trailing | 2,549 | 74.0% | 79.3% | **−5.3 pp** |
| ↳ tied | 670 | 76.0% | 79.2% | −3.2 pp |
| ↳ leading | 6,605 | 79.0% | 80.4% | −1.4 pp |
| Playoffs (all) | 34,197 | 77.8% | 78.6% | −0.8 pp |

The models agree, with approximate marginal effects:
- Clutch: −1.4 pp (p < .001).
- Late-close: a further −1.7 pp, so about −3 pp in total.
- Late-close *and trailing*: a further −3.7 pp (p < .001).
- Playoffs: −1.1 pp (p < .001).
- The pattern survives dropping the 2019-20 and 2020-21 bubble and no-crowd seasons.

This replicates the published NBA findings: Cao, Price & Stone 2011 found 5–10 pp drops in the final seconds of very close games; Toma 2017 found −3.1 pp for the NBA in the final 30 s of tight games. Ours is somewhat smaller, probably because our late-close window (60 s, ≤3 pts) is wider.

**2. Workload doesn't amplify the pressure dip.** Every interaction is null:
- clutch × top-quartile season minutes: +0.4 pp, p = .55;
- clutch × back-to-back: p = .85;
- clutch × in-game minutes: p = .43;
- clutch × prior-7-day minutes: p = .16;
- playoffs × high workload: p = .72.

One hint worth flagging *as a hint*: late-close × back-to-back came out at −2.0 pp, but with **p = .09** and a CI spanning zero. In the descriptive table, late-close on B2Bs is −4.0 pp vs −2.2 pp otherwise (n = 1,638). Don't build a chapter claim on it. It's a candidate for a pre-registered re-test on more seasons (1996–2015 are available from the same mirror).

**3. The main workload effects run "backwards", and that's a selection effect, not a benefit of fatigue.** More in-game minutes, cumulative minutes and prior-7-day minutes all go with slightly *higher* FT% (+0.2 to +0.5 pp per unit) after the baseline adjustment.
- Back-to-backs have no main effect (+0.1 pp, p = .51).
- The likely reason is that coaches play the players who are on form, and starters' late-game minutes coincide with being on court in close games.
- **This dataset can't separate fatigue from selection.** It has no direct fatigue measure (no load or HR data) and minutes aren't randomly assigned.

## How this bears on the "cascade" (Hore workload → Rusdiana kinematics → Kinrade reinvestment)
- The *pressure* link at outcome level is supported and small, matching the literature.
- The *workload → more choking* link is **not supported**: there's no interaction, and the main effects are confounded.
- Kinematics and reinvestment aren't observable in play-by-play, so these data can't test the middle links. Researcher-01 and researcher-05 cover the lab literature.

## Limitations (to state plainly in the book)
1. Observational data, so these are associations, not causes. Shooters in clutch moments are selected (deliberate fouls on poor shooters), which the baseline adjusts for but can't eliminate.
2. Reconstructed minutes are approximate. A player who records no event in a period they started is missed, which may cause a slight under-count.
3. B2B is a team-level proxy. Individual load management (stars resting on B2Bs) means players who *do* play B2Bs are selected.
4. No crowd-size or attendance variable. Bubble and no-crowd seasons were dropped as a robustness check rather than modelled.
5. Free throws within a trip aren't independent (hot hand: Arkes 2010; Lantis & Nesson 2021), which is why second-of-pair is controlled for. Its effect is large (+4.5 pp).
6. Playoff baselines are pooled with the regular season. Playoff shooters are a selected, better group.

## Literature cited (verified; Zotero keys in brackets)
- Cao, Z., Price, J. & Stone, D.F. (2011). Performance under pressure in the NBA. *J Sports Econ* 12(3), 231–252. https://doi.org/10.1177/1527002511404785 [AAQT69K4]. 2002-03 to 2009-10 free throws; 5–10 pp worse in the final seconds of very close games; no playoff effect found.
- Toma, M. (2017). Missed shots at the free-throw line. *J Sports Econ* 18(6), 539–559. https://doi.org/10.1177/1527002515593779 [DHQ9VHRN]. Over 2M free throws (NBA, WNBA, NCAA); NBA −3.11 pp in the final 30 s of tight games.
- Steenland, K. & Deddens, J.A. (1997). Effect of travel and rest on performance of professional basketball players. *Sleep* 20(5), 366–369. https://doi.org/10.1093/sleep/20.5.366 [K6C2ACJD]. 8,495 games; more rest improved team scoring.
- Esteves, P.T. et al. (2021). Basketball performance is affected by the schedule congestion: NBA back-to-backs under the microscope. *Eur J Sport Sci* 21(1), 26–35. https://doi.org/10.1080/17461391.2020.1736179 [NBMVPIVS, existing; added to physical/recovery]. 2016-17 season; win likelihood and shooting efficacy differ across congestion cycles.
- Arkes, J. (2010). Revisiting the hot hand theory with free throw data in a multivariate framework. *J Quant Anal Sports* 6(1). https://doi.org/10.2202/1559-0410.1198 [V3JBJL69, existing; added to hot hand and free throws].
- Lantis, R. & Nesson, E. (2021). Hot shots: an analysis of the "hot hand" in NBA field goal and free throw shooting. *J Sports Econ* 22(6), 639–677. https://doi.org/10.1177/15270025211006889 [ALJSJCYA, existing; added to hot hand].
- Morgulev, E. & Galily, Y. (2018). Choking or delivering under pressure? The case of elimination games in NBA playoffs. *Front Psychol* 9, 979. https://doi.org/10.3389/fpsyg.2018.00979 [BQ4BBNT7]. Facing elimination didn't raise team performance (1,930 playoff games).

**Data citation:** shufinskiy, *nba_data: NBA play-by-play and shot details 1996/97–2024/25* (GitHub, Apache-2.0), derived from stats.nba.com. Accessed 22 Oct 2026.
