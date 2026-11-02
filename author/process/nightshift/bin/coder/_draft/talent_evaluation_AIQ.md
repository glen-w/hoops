# Talent Evaluation: Athletic Intelligence and On-Court Performance

## Overview

The Athletic Intelligence Quotient (AIQ) is a cognitive assessment measuring four domains: Decision Making, Reaction Time, Learning Efficiency, and Visual Spatial Processing. A 2023 study by Hogan, Taylor, Boone, and Bowman examined whether AIQ scores taken at the NBA Combine (2014–2019) predicted on-court performance in drafted players.

**Source:** [Hogan et al. (2023). The Athletic Intelligence Quotient and performance in the National Basketball Association. *Frontiers in Psychology*, 10.3389/fpsyg.2023.1197190](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1197190/full)

## Study Design

- **Sample:** 356 NBA Combine attendees (2014–2019); 227 drafted or signed to NBA; 182 with 10+ games played in subsequent seasons.
- **Outcome variables:** Player Efficiency Rating (PER) and Effective Field Goal Percentage (eFG%).
- **Analysis:** Hierarchical regressions controlling draft round, then adding the four AIQ factors.

## Key Findings: AIQ Factor Predictive Validity

| AIQ Factor | PER Zero-Order r | PER Unique Variance | eFG% Zero-Order r | eFG% Unique Variance | Notes |
|---|---|---|---|---|---|
| **Decision Making** | 0.19** | +2.1% | 0.30*** | +7.0% | Unique predictor of both PER and eFG%. Strongest effect. |
| **Visual Spatial Processing** | NS | NS | 0.17* | NS | Correlated with eFG% but no unique contribution after draft round. |
| **Reaction Time** | NS | NS | Marginal† | NS | Minimal predictive validity. |
| **Learning Efficiency** | NS | NS | NS | NS | No meaningful correlation with performance metrics. |
| **Draft Round (baseline)** | — | 8.6% (PER) | — | 3.0% (eFG%) | Context effect; AIQ added variance beyond draft placement. |

*Note: *** p < 0.001, ** p < 0.01, * p < 0.05, † p < 0.10, NS = not significant. Zero-order r is the simple correlation; Unique Variance is the additional R² increment in hierarchical regression.*

## Interpretation

**Decision Making** emerged as the only AIQ subdomain with unique predictive validity after controlling for draft round. Its correlation with eFG% (r = 0.30) was approximately twice that for PER (r = 0.19), suggesting that decision-making acuity has a stronger relationship to shooting efficiency than to overall offensive rating.

Effect sizes are modest: Decision Making accounted for 2–7% additional variance beyond draft placement. This likely reflects:
1. **Range restriction** in an elite sample (all players tested at Combine).
2. **Unmeasured confounds** (e.g., college performance, physical attributes, coaching quality).
3. **Temporal separation** between Combine testing and NBA play (often 1–3 seasons later).

## Limitations and Disclosure

Hogan et al. disclosed financial ties to the AIQ's developers (Bowman & Goldman), meeting transparency standards. However, the AIQ is a proprietary, commercial assessment, so independent replication in published academic samples remains limited.

### Related Questions for Further Investigation
- Do AIQ factors predict other defensive metrics (DBPM, rim protection) or team success (wins, playoff advancement)?
- How stable are AIQ scores across retesting?
- Does AIQ predictive validity vary by position or era?
- Can simpler, public cognitive or shooting-efficiency proxies replicate the Decision Making signal?

## Data Access

**Basketball-Reference** provides PER and eFG% for 10+ game seasons (1946–2026 seasons) via:
- Leaderboards: [eFG% leaders](https://www.basketball-reference.com/leaders/efg_pct_progress.html)
- Player pages: Individual season and career PER/eFG%
- Citation-scrape permitted under Sports Reference ToS; check rate limits (≈20 req/min).

**Recommended tools for extraction:**
- R: `hoopR::load_nba_pbp()` (ESPN), `ballr` (Basketball-Reference wrapper), `nbastatR` (multi-source)
- Python: `nba_api` (official NBA.com Stats), `pbpstats` (PBP parsing)

---

**Status:** Foundation draft. Pending integration with broader talent evaluation framework and cross-check against 2024–2026 combine and performance data.

**Citation registry:** All in-text citations verified against [analysis/nightshift_requests.json](../nightshift_requests.json).
