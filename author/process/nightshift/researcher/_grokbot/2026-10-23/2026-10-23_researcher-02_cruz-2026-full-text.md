# Cruz et al. 2026 (Sci Rep): what the full text actually reports

**Request:** 2026-10-22-researcher-02 (unblocks 2026-10-22-researcher-12)
**Status:** done. I read the full text at Nature (open access, CC BY-NC-ND 4.0).
**Paper:** Cruz, D.A., Gutiérrez-Capote, A., Jiménez-Martínez, J., López-Morales, J.J., Martínez-Muñumer, I., Torre, E., Alarcón, F. & Cárdenas, D. (2026). Environmental pressure and sensory uncertainty modulate free-throw performance: psychological, neurophysiological, and kinematic evidence. *Scientific Reports* 16, 22603. https://doi.org/10.1038/s41598-026-51871-7 (published 18 May 2026). Full text: https://www.nature.com/articles/s41598-026-51871-7. Data: https://osf.io/ewvmr. Zotero: **86WR2S8S**.

## The headline for the book: there is no direction of variability to quote
The paper **did not measure kinematic variability at all.** It compared **mean joint angles** across conditions. The authors say so themselves (Discussion):
> "Without direct measures of movement variability or mechanical stability, such mechanistic claims should be treated cautiously to avoid over-interpretation of isolated phase or joint effects."

A Discussion sentence does say occlusion-driven reweighting "can increase movement variability … particularly during the final phases of movement", but it is backed by citations, not by their data. Don't quote it as a finding.

## Design
- **Participants:** 24 male federated players, U14–U18. Mean age 15.37 ± 1.10 y, height 176.9 ± 6.6 cm (Table 1). Inclusion required at least 2 years of training and at least 270 min of training per week.
- **Design:** 2 × 2 within-subject (pressure × visual occlusion), counterbalanced, one session per condition after 2 familiarisation sessions.
- **Shots:** 100 free throws per condition, in 5 blocks of 20.
- **Self-reports** every 5 shots: anxiety (Anxiety Thermometer, 0–10), probability of failure (POF, 1–7) and cost of failure (COF, 1–7).
- **Pressure manipulation** ("high cost", Methods/Procedure):
  - +1 point for a make, −1 for a miss.
  - Three consecutive misses reset the score to 0.
  - A miss on shots 20/40/60/80/100 cost an extra −5.
  - Negative scores weren't allowed.
  - There was no audience, no money and no opponent.
- **Occlusion:** Senaptec strobe glasses set to 0.1 s visible / 0.9 s dark.
- **Kinematics:** markerless OpenCap (3 iPads, 240 Hz).
  - Only the **last 5 shots of each 20-shot block** were analysed, i.e. 25 per condition.
  - Five joint flexion angles (shoulder, elbow, hip, knee, ankle) across 4 phases (sinking, lifting, take-off, release).
  - 60 exploratory tests, Benjamini–Hochberg FDR-corrected.
- **fNIRS:** NIRSport2, 21-channel bilateral prefrontal montage. Mean OxyHb over the session.
- **Analysis:** linear mixed models (lmerTest). Psychological outcomes and accuracy were pre-specified as primary, OxyHb as secondary, kinematics as exploratory.

## Results
**Accuracy (Results, "Performance"):**
| Condition | Make % (M ± SD) |
|---|---|
| low pressure, no occlusion | 61.38 ± 12.59 |
| **high pressure, no occlusion** | **61.00 ± 14.21** |
| low pressure, occlusion | 41.12 ± 14.59 |
| high pressure, occlusion | 36.46 ± 12.00 |

> "occlusion was the sole significant predictor of performance (b = − 16.667 … p < 0.001), while the effect of pressure was not significant (b = − 1.750, SE = 1.96, t = − 0.89, p = 0.378)"

The pressure-only contrast was d = 0.076, p = 1.000. **So the pressure manipulation on its own did not lower accuracy.** The abstract's "36.46% vs ~61%" drop comes from occlusion.

**Psychological measures (all p < 0.001 for both stressors):**
- Pressure raised anxiety (b = 1.09 on the 0–10 scale; low vs high pressure, no occlusion: d = −0.84), POF (b = 0.69) and COF (b = 1.06; d = −1.04).
- The pressure × occlusion interaction was negative every time, so the effects were less than additive.
- At shot level, higher anxiety (b = −0.24), POF (b = −0.40) and COF (b = −0.08) predicted lower accuracy.
- Mediation: anxiety carried about 25% of the POF effect (partial mediation) and all of the COF effect.
- Carry-over: the previous shot's outcome predicted the next (b = 0.35). Anxiety added an independent effect (b = −0.098).

**fNIRS (Results, "OxyHb"):**
- Prefrontal OxyHb rose with occlusion (b = 0.00101, p < 0.001) and pressure (b = 0.000465, p = 0.024), with a negative interaction.
- The pressure-only contrast (low vs high pressure, no occlusion) was **not significant after Bonferroni** (p = 0.141, d = −0.91). The occlusion contrasts were large (d about 2).
- The authors call OxyHb "a non-specific indirect index … compatible with several concurrent processes" (Discussion).

**Kinematics (Results, last subsection).** Five of 60 tests survived FDR. Four involve pressure, and all are at the **hip**:
| Phase | Effect | Direction | b (deg), FDR p |
|---|---|---|---|
| Lifting | Pressure, hip flexion | **less** hip flexion under high pressure | −5.35, .003 |
| Take-off | Pressure, hip flexion | **less** hip flexion ("lowest") | −4.18, .012 |
| Release | Pressure, hip flexion | **less** hip flexion | −2.60, .044 |
| Sinking | Pressure × occlusion, hip | high pressure + occlusion had more hip flexion than high pressure alone | +10.89, .012 |
| Release | Occlusion, shoulder flexion | lower shoulder angle under occlusion (text: "reduced shoulder extension at release") | −7.32, .006 |

**Effects that did not survive correction** (uncorrected p < .05 only):
- pressure on ankle (lifting) and knee (take-off), both in the reduced-flexion direction;
- pressure on shoulder: + in sinking and lifting, − at release;
- occlusion on elbow at release (+5.3°).

**Elbow and wrist:** no pressure effect on the elbow survived, and the wrist wasn't analysed.

## Inconsistencies to flag
- **Direction.** The Discussion says "Under high-pressure and visually occluded conditions, participants exhibited greater joint flexion across the kinetic chain … likely represents a compensatory stabilisation strategy." The Results tables say pressure *reduced* hip flexion in three phases. Only the sinking-phase pressure × occlusion interaction runs toward more flexion. Quote the Results, not the Discussion.
- **Model structure.** Methods describe a condition (4 levels) × phase model, but Results report separate pressure × occlusion models per joint and phase. This is minor, but a reviewer might notice it.
- **No link to outcome.** Kinematics weren't related to makes or misses. The Discussion says: "it remains unclear whether these kinematic adaptations functionally enhance or impair shooting accuracy."

## Limitations (authors' own, Discussion)
- Self-reports only every 5 shots.
- fNIRS motion artefacts during shooting, plus hair and skin effects.
- "environmental pressure manipulation has a limited ecological validity": no audience or live competition.
- All-male sample with a broad maturational range (U14–U18).
- Within-block fatigue and learning can't be ruled out.

**My additions:**
- The kinematic sample is thin (25 shots per condition, markerless video).
- The kinematic tests were exploratory.
- Pressure alone didn't hurt accuracy, so the kinematic changes may not be "choking" kinematics at all.

## Implications for GAME TIME kinematics and PLAYERS motor control (suggestions)
Cruz et al. 2026 can't carry a claim that pressure makes the release *more variable*: they never measured variability. What it supports is narrower:
1. A points-based pressure manipulation in youth players reliably raised anxiety and perceived threat **without** lowering free-throw accuracy.
2. It came with a small, consistent postural shift: about 3–5° **less hip flexion** through lifting, take-off and release. Read plainly, that's a more upright, shallower lower-body action, a "tightening" rather than a wobble.
3. Losing vision, not pressure, wrecked accuracy, altered the shoulder at release and drove the biggest prefrontal load.

For PLAYERS motor control, the best fit is the paper's appraisal chain:
- perceived failure probability and cost → anxiety → accuracy, at shot level;
- a miss-to-miss carry-over effect.

The fNIRS result (more prefrontal OxyHb under stress) is consistent with "more executive effort" but non-specific, and pressure alone didn't reach significance after correction. For the variability claim itself, the book should keep leaning on Mullineaux & Uhl 2010 (late elbow–wrist variability on misses, no pressure arm). The pressure → variability link should stay an open question.

**Optional framing:** "Put teenagers under a points-penalty and they feel it (anxiety up, the prefrontal cortex working harder, hips a few degrees stiffer), yet they still make about 61% of their free throws. Take away their sight and they drop to about 40%."

## Does this unblock researcher-12?
**Yes, with a correction.** The open question ("which direction does variability go under pressure?") now has a definite answer: *not measured*. Researcher-12 can proceed by:
- citing Cruz 2026 for mean-angle changes (less hip flexion), the null pressure effect on accuracy, and anxiety mediation;
- dropping any "variability increased" wording attributed to it;
- keeping the "workload predicts pressure-induced variability" item marked as untested.

## Zotero
| key | item | collection(s) | created/reused |
|---|---|---|---|
| 86WR2S8S | Cruz et al. 2026, *Sci Rep* 16, 22603 (full abstract present, DOI, 8 authors) | hoops/⭐game/skills/shooting/free throws (HN7AY374) | reused (created 2026-10-22-overtime). No change was needed and nothing was attached. |
