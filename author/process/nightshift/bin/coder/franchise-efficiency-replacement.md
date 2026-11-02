# Franchise Efficiency 2015-16: hoopR PBP Validation

**Access date**: 2026-10-21  
**Data source**: hoopR::load_nba_pbp(2015)  
**Method**: Per-100-possession offensive (ORtg) and defensive (DRtg) ratings

## Targets
- Portland Trail Blazers
- Boston Celtics
- Golden State Warriors

## Execution
1. Load 2015-16 season PBP via hoopR; cite hoopR GitHub repo and version
2. Aggregate possessions by team
3. Compute ORtg = (points / possessions) * 100; DRtg = (opponent points / possessions) * 100
4. Document exact R code, dependencies, and runtime
5. Cross-validate against franchise-efficiency-sources.md
6. Report confidence (HIGH for hoopR direct load; MEDIUM if validation reveals divergence)

## Results
(Pending execution)