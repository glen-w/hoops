# Marmarinos (2019) — Total Performance Index (TPI)

**Source:** `hoops/Christos Marmarinos - 2019 - Structural validity and reliability of new index for evaluation of high-level basketball -- 25NDF7BW`

## Summary
New metric TPI vs. Euroleague standard PIR. 442 players, 2 seasons (2016-18), ≥6 min & ≥6/30 games.

## TPI Formula
```
Offensive Part = (Weighted Points Made / Weighted Points Attempted) ×
                 (Points + Assists − Turnovers + OffReb × Team Pts/Poss)

Points Offered (def) = (DefReb + Steals + Blocks × Team DefReb%) × Team Pts/Poss

Points Received (def) = Personal Possessions × Team Def Pts/Poss
Personal Possessions ≈ 0.2 × Team Def Poss (40 min) − Defensive Stops

TPI = Offensive Part + Points Offered − Points Received
```

## Results
| Metric | TPI | PIR |
|---|---|---|
| Team win% R² | **0.646** | 0.327 |
| 1 unit → win% | +1.8% | +1.3% |
| TPI↔PIR corr | r=0.825 | — |
| Reliability (same team) | 58.5% (r=0.765) | 55% (r=0.742) |
| Reliability (diff team) | **38.5% (r=0.62)** | **NS** |

**Takeaway:** TPI doubles PIR's explanatory power for winning; survives team changes.

## Chapter Seeds
- *Beyond the Box Score* — why PIR fails & TPI works
- *Portable Value* — metrics that travel with the player
- *The 1/5 Assumption* — personal possessions ≈ 20% of team defense

---
*Grounded in hoops_summary output (25NDF7BW)*