# Proxy measures for an "automaticity baseline" to predict reinvestment susceptibility

**Request:** 2026-10-22-overtime-researcher-03 (info, med)
**Status:** done. This is a literature grounding plus a quick reliability check on the NBA data.
**Companion data:** `2026-10-22_researcher-03_player_season_automaticity_proxies.csv` has one row per player-season, 2015-16 to 2023-24. It holds low-pressure FT%, pressure FT%, the gap between them, FT% over the first 20 and last 20 games, game-to-game FT% SD, minutes and games, with `source` and `confidence` columns.

## What the literature uses to index automaticity (and what each would mean on an NBA court)
| Proxy | Literature basis | Feasible with public NBA data? |
|---|---|---|
| **Dual-task cost.** Performance with vs without a secondary task: small cost means automated. | The standard operationalisation. Kal et al. 2018 review 25 trials. Beilock & Carr 2001 and Gray 2004 show experts are robust to extraneous dual tasks but hurt by skill-focused ones. | **No.** Lab only. |
| **Trait reinvestment scales** (MSRS movement; DSRS decision). | Masters & Maxwell 2008. Kinrade et al. 2010 (DSRS r = .74 with coach choking ratings). Jackson et al. 2006. Iwatsuki et al. 2018. | Only via questionnaires with players. Not public. |
| **Explicit-knowledge pool.** The number of technical rules a player can report. | Masters 1992. Lam et al. 2009 (analogy learners reported fewer rules and didn't break down). | Interviews and biographies only. A qualitative proxy is a coach-taught "rule-heavy" form vs an analogy cue. |
| **Kinematic consistency or variability.** | Button et al. 2003; Mullineaux & Uhl 2010; Verhoeven & Newell 2016. Note Malhotra 2015, where *higher* reinvestment went with *lower* variability. | Needs tracking (proprietary). |
| **EEG T3–Fz coherence / left-temporal alpha.** | Zhu et al. 2011. Parr et al. 2023 found only 36–47% of studies support these markers. | No. Weak marker anyway. |
| **Low-pressure FT% (skill level).** | Cao et al. 2011: worse shooters choke more. Toma 2017: the pressure drop is larger at higher levels and for future pros. | **Yes.** |
| **Within-season consistency (first vs last 20 games; game-to-game SD).** | Not an established automaticity measure, so this would be a new operationalisation. | Yes. |

## What the NBA data say about the outcome-based proxies (quick check, my analysis)
Using the 519,640-attempt dataset from researcher-02:
- **Baseline FT% is a highly stable trait.** Low-pressure FT% correlates **r = 0.88** year to year (143 player pairs with 30 or more pressure attempts in consecutive seasons).
- **An individual "choke gap" (pressure FT% minus own baseline) is *not* a stable trait at NBA level.**
  - Year-to-year r = **0.08** (143 pairs).
  - Split-half (odd vs even pressure attempts) r = **−0.09**, for 102 players with 100 or more pressure attempts across 2015-24.
  - That is what noise looks like. With about 100 clutch attempts per player, the binomial SE (~4 pp) swamps true differences of a few points.
- **Low-pressure FT% barely predicts the gap:** r = 0.10 (102 players). The direction is consistent with Cao et al. 2011 (better shooters lose a bit less), but it's weak.
- **Season-start vs season-end drift isn't stable:** year-to-year r = 0.02 (811 pairs). **Game-to-game FT% SD** is moderately stable (r = 0.48, 636 pairs), but it's partly mechanical: binomial variance depends on FT% and attempts per game. Read it as a consistency descriptor, not an automaticity measure.

## Suggestions (non-prescriptive)
1. **Group-level, not player-level.** The data support "pressure costs NBA free-throw shooters a couple of points on average, more when trailing late". They don't support ranking individual players by choke susceptibility from box-score outcomes. That's a nice "uncommon" point for the book: the clutch reputation is mostly noise.
2. If the book wants an automaticity baseline per player, the defensible candidates are **low-pressure FT% plus a qualitative "explicit-rules" proxy**, such as documented mechanical rebuilds or a shooting-coach overhaul. The Masters (1992) and Lam (2009) logic predicts that recently rebuilt (explicit) forms are most fragile. That's testable in the data: compare pressure gaps in the season after a publicised form change. It's an idea, not something done here.
3. Treat kinematic variability with care as an automaticity marker. Its sign relative to reinvestment differs across studies (see researcher-01).

## Sources (verified DOIs; Zotero keys)
- Kal, E. et al. (2018). Does implicit motor learning lead to greater automatization of motor skills compared to explicit motor learning? A systematic review. *PLoS ONE* 13(9), e0203591. https://doi.org/10.1371/journal.pone.0203591 [48PMTJ6G]. Most comparisons showed no automaticity differences, and the evidence is level 3.
- Beilock, S.L. & Carr, T.H. (2001). On the fragility of skilled performance: what governs choking under pressure? *J Exp Psychol Gen* 130(4), 701–725. https://doi.org/10.1037/0096-3445.130.4.701 [3ZD3W5EQ]. Proceduralised putting choked, and self-consciousness training prevented it.
- Gray, R. (2004). *J Exp Psychol Appl* 10(1), 42–54. https://doi.org/10.1037/1076-898x.10.1.42 [29H4I5CF].
- Masters, R.S.W. (1992). *Br J Psychol* 83(3), 343–358. https://doi.org/10.1111/j.2044-8295.1992.tb02446.x [MZH5RB84]; Masters & Maxwell (2008). *Int Rev Sport Exerc Psychol* 1(2), 160–183. https://doi.org/10.1080/17509840802287218 [M4M9SCEP].
- Kinrade, N.P., Jackson, R.C. & Ashford, K.J. (2010). DSRS. *J Sports Sci* 28(10), 1127–1135. https://doi.org/10.1080/02640414.2010.499439 [WZTH4FH4].
- Lam, W.K., Maxwell, J.P. & Masters, R.S.W. (2009). *J Sports Sci* 27(2), 179–191. https://doi.org/10.1080/02640410802448764 [ME4JJMFX].
- Carson, H.J. & Collins, D. (2016). The fourth dimension. *Int Rev Sport Exerc Psychol* 9(1), 1–21. https://doi.org/10.1080/1750984x.2015.1072231 [9CE97W59]. "Skill establishment" (the level and consistency of automaticity) as the protective dimension is the closest *conceptual* match to "automaticity baseline".
- Cao, Price & Stone (2011) [AAQT69K4] and Toma (2017) [DHQ9VHRN]. Full citations are in the researcher-02 note.
- Malhotra et al. (2015) [6NMFFTRA], Zhu et al. (2011) [IJD8QBA2], Parr et al. (2023) [B4FT8QJ4], Button et al. (2003) [H3WPJBPT], Mullineaux & Uhl (2010) [9PXHES4X], Verhoeven & Newell (2016) [U45UM6YQ]. Full citations are in the researcher-01 and -05 briefs.

**Where thin:** no validated *field* (game-data) measure of automaticity exists in the basketball literature found. Anything built from NBA outcomes is a new proxy, and should be labelled that way.
