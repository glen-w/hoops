# Free Throws Under Pressure: Outcome Data 2015-24

**Source:** NBA outcome analysis, 519,640 free-throw attempts (2015-16 to 2023-24, regular season + playoffs). Pressure contexts defined by final-minute score margin and game situation.

## Pressure Effects at Outcome Level

Free-throw performance declines measurably in high-pressure situations, with the largest drops in the final minute of close games.

**Late-close situations show a concentrated dip.** In the final minute of games with a ≤3-point margin, shooters made 77.5% of attempts, compared to a baseline of 80.0% expected from their own season average (Cao et al. 2011; Toma 2017). This represents a −2.5 percentage-point drop [AAQT69K4, DHQ9VHRN]. The dip is largest when the shooter's team is trailing: −5.3 pp (74.0% observed vs. 79.3% expected; n = 2,549). Tied games show an intermediate effect (−3.2 pp), while leading shooters are less affected (−1.4 pp). This pattern replicates the published findings of Cao et al. (2011, final seconds; 5–10 pp drops) and Toma (2017, final 30 s; −3.1 pp for the NBA).

**Playoff competition compounds the effect slightly.** Across all playoff free throws, the shortfall is −0.8 pp, or about −1.1 pp after controlling for season and other factors. This is smaller than the late-close effect, suggesting that playoff-wide pressure is ambient but not as acute as the final-minute margin situations.

**Clutch fouls away from the final minute** (NBA clutch definition: ≤5 min, ≤5 pts, excluding the final minute) show a −0.8 pp dip, or −1.4 pp in adjusted models.

## No Amplification from Workload

The hypothesis that workload (fatigue, back-to-backs, accumulated minutes) would amplify pressure-induced choking finds **no support** in the outcome data. Across six tests—clutch×season-high-workload, clutch×back-to-back, clutch×in-game minutes, clutch×prior-7-day minutes, late-close×back-to-back, and playoffs×high-workload—all interaction p-values exceed .05, and most exceed .20 (clutch×in-game minutes p = .43; clutch×back-to-back p = .85; playoffs×high-workload p = .72).

A hint (not a claim): late-close free throws on back-to-back nights showed a −4.0 pp dip vs. −2.2 pp otherwise (n = 1,638), but the difference carries a 95% CI spanning zero (p = .09). This is a candidate for a pre-registered re-test on earlier seasons.

**Selection confound:** The apparent "backwards" main effect of workload (high-minute players shooting slightly *better* under pressure, +0.2 to +0.5 pp) likely reflects that coaches play the players in form. Starters' late-game minutes co-occur with being hot, so minutes isn't a measure of fatigue here. The dataset has no direct fatigue proxy (heart rate, blood lactate) and minutes aren't randomly assigned, so observational designs can't separate fatigue from selection [Steenland & Deddens 1997; Esteves et al. 2021].

## Replication and Scope

League free-throw percentage by season matched published figures (75.6% in 2015-16, rising to 78.4% in 2023-24). The data exclude the 2019-20 bubble and 2020-21 no-crowd seasons from the final models as a robustness check, since crowd attendance is not measured separately.

**Limitations:**
- Observational: associations, not causal.
- Reconstructed minutes from substitution logs are approximate; players with no recorded event in a starting period may be under-counted.
- Back-to-backs are a team-level proxy; load management (stars resting on B2Bs) means players who *do* play B2Bs are selected.
- Clutch fouls are disproportionately called on poor shooters, which the baseline adjustment handles but can't fully eliminate.
- Free throws within a trip are not independent (hot-hand effect: +4.5 pp for the second attempt in a pair).
- Playoff baselines are pooled with regular season; playoff players are a selected, higher-skill group.

**Data and methods:** shufinskiy, *nba_data* (stats.nba.com play-by-play and shot-detail logs, GitHub mirror). Logistic regression: make/miss ~ baseline-FT% logit + second-of-pair + technical-foul flag + season FE + pressure/workload terms, player-clustered SEs.
