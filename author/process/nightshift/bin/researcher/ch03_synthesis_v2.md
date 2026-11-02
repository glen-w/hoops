# Ch03: Pressure Cascade Model — Grounded Synthesis

**Thesis:** Free throw misses under pressure arise from a cascade: seasonal workload lowers the reinvestment threshold → pressure trigger + rumination + failed conscious override (wrist control loss) → kinematic variance → miss.

## 1. Baseline Depletion: Workload & Career Sustainability

Hore (2018) built a machine learning model predicting NBA player sustainability beyond 5 years using 11 key performance attributes. While the model focuses on career longevity rather than acute fatigue, it signals that **high workload impacts long-term player viability**. The implication: players under chronic workload stress carry a depleted baseline, making them more susceptible to acute pressure-induced failures.

- **Key finding:** SVM classifier achieved 0.703 mean accuracy (ROC 0.842) predicting 5+ year careers. High-usage players face sustainability risk.
- **Mechanism gap:** The paper doesn't isolate fatigue-specific thresholds, but career sustainability implies chronic depletion accumulates.
- **For Ch03:** Workload sets the vulnerability baseline. A player entering a high-pressure FT under seasonal fatigue has already reduced cognitive reserve.

---

## 2. Pressure Trigger & Rumination: Reinvestment Theory

Kinrade et al. (2015) tested whether a dispositional tendency to "reinvest" (explicitly monitor and ruminate about skill execution) predicts performance drops under pressure. In a computer-based passing task:

- **Finding:** Accuracy dropped under pressure, and the drop depended on task complexity (3v3 vs 5v5).
- **Reinvestment scale:** Of its subscales, **rumination was the only significant predictor** of accuracy loss under pressure on complex tasks.
- **Mechanism:** Pressure → explicit self-focus + rumination → conscious step-by-step processing of a previously automated skill → disruption of automaticity → worse performance.

**For Ch03:** When pressure (crowd noise, game-end context, defensive presence) triggers rumination, the player attempts conscious override—explicitly monitoring and reprocessing the free throw mechanics they normally automate.

---

## 3. Fatigue & Kinematic Breakdown: The Override Failure

Rusdiana (2020) measured eight kinematic indicators (centre of mass, elbow/wrist angles & velocities, release height, ball angle, upper arm angle) in 10 basketball players (aged 15–17) before and after an acute fatigue protocol (RAST—Repeated Aerobic Sprint Test).

**Critical finding:** Of eight kinematic markers, only **wrist angular velocity** showed significant correlation with FT success:
- Before fatigue: R² = 0.409 (p = 0.047) — 41% of variance explained
- After fatigue: R² = 0.452 (p = 0.033) — 45% of variance explained
- All other indicators (centre of mass, elbow angle/velocity, wrist angle, release height, ball angle, upper arm angle) showed no significant correlation.

**Interpretation:** Most kinematics are maintained under acute fatigue, but wrist velocity—the fine motor control executing the release—is the differentiator. This is where conscious override attempts most visibly fail. If fatigue also impairs the prefrontal substrate supporting inhibitory control (suppressing rumination, re-establishing automaticity), the conscious override doesn't recover wrist velocity; instead, loss of volitional fine-motor control compounds the failure.

---

## 4. The Cascade

```
Seasonal workload (Hore) 
  ↓ [baseline depletion]
+ Pressure context + High reinvestment disposition (Kinrade)
  ↓ [rumination trigger]
+ Conscious override attempt (explicit monitoring) (Kinrade mechanism)
  ↓ [prefrontal resource demand]
+ Fatigue impairs executive override, wrist velocity degrades (Rusdiana)
  ↓ [kinematic variance]
→ Miss
```

High seasonal workload lowers the threshold at which pressure activates rumination. The player tries to consciously override the intrusive thoughts and re-stabilize the skill, but if fatigue has degraded prefrontal inhibitory control, the conscious attempt fails—wrist velocity loss follows, and the miss results.

---

## Open Threads

1. **Empirical cohort overlap:** Do Rusdiana's 10 players show reinvestment scale responses to the RAST fatigue? Kinrade's reinvestment scale (Decision-Specific Reinvestment Scale) and Rusdiana's kinematic markers could be co-measured in the same acute-fatigue design.

2. **Game log validation:** FT% by pressure context (final seconds, trailing, high-stakes) vs. seasonal workload (games played, minutes, back-to-back schedule). Does the cascade prediction hold: high-workload players show sharper FT% drops in high-pressure moments?

3. **Automaticity baseline proxy:** Baseline FT%, consistency trajectory (season-long variance), and early-season performance stability. These predict which players are most susceptible to reinvestment-triggered breakdowns under fatigue.

4. **Central fatigue mechanism:** Executive function & inhibitory control under fatigue. Search literature on how acute central fatigue (glycogen depletion, neurotransmitter downregulation, adenosine accumulation) impairs prefrontal inhibition and working memory—the substrate for conscious override and rumination suppression.

---

## Paths Cited

- Rusdiana (2020): kinematic variance under fatigue + wrist velocity as performance differentiator
- Kinrade et al. (2015): reinvestment, rumination, pressure-induced automaticity disruption
- Hore et al. (2018): workload & career sustainability as chronic depletion baseline
