# Portland Trail Blazers 2015–16 PBP & Efficiency Calculation

**Data load**:
```r
library(hoopR)
pbp_2015_16 <- load_nba_pbp(2015)
portland <- pbp_2015_16 %>% filter(team == "POR") # or similar
```

**Efficiency calculation**:
- Offensive Rating (ORtg) = (Points Scored / Possessions) × 100
- Defensive Rating (DRtg) = (Points Allowed / Opponent Possessions) × 100
- Possessions ≈ FGA − OReb + TO + (0.44 × FTA)

**Validation**:
- Season record: 44–38 (official NBA record)
- Aggregate efficiency vs. nba.com or Basketball-Reference published rankings
- Confidence grade the match and note any divergence

**Output**: Sourced efficiency table (ORtg/DRtg) + season totals for chapter use.

**Citation**: 
- hoopR ESPN PBP load: Gilani, sportsdataverse/hoopR
- Cross-check: nba.com or Basketball-Reference

**Access date**: 2026-10-21