# Grounded Literature Numbers (from HR summaries 2026-10-19)

All figures below come from hr_out hoops_summary excerpts. No invented values.

## Karamousalidis et al. 2025 — Euroleague vs NCAA DI 3PT (2020–21)
- Sample: 70 games (35 EL, 35 NCAA); 3,249 3PA sequences (1,774 EL; 1,475 NCAA).
- Overall 3P%: 36.9%. EL 38.4% vs NCAA 35.1%.
- Type of offense: χ²(2)=20.84, p<.001. NCAA transition share 9.4% vs EL 8%; transition accuracy EL 39% vs NCAA 32.8%. Set plays 75.3% of attempts; set-play 3P% EL 38.4% vs NCAA 35.5%.
- Shot timing: χ²(2)=206.52, p<.001 (strongest differentiator). EL end-of-possession attempts 19.4% vs NCAA 6.1%. Mid-possession most efficient (EL 41.2%, NCAA 36.1%).
- Position: χ²(2)=30.79, p<.001. Guards 59.7% of attempts. EL forwards 39.3% (highest); NCAA forwards 33.4% (lowest).
- CHAID: summary truncated in HR excerpt — full CHAID tree results still need a second-pass re-read (open thread).
- Reliability: weighted Cohen's κ 0.78–0.84.

## Foteinakis & Pavlidou 2025 — NBA vs EuroLeague decade (2012–13→2022–23, excl. 2019–20)
- Confirmed denominator: 12,150 = NBA regular-season games; 2,538 EuroLeague games; total 14,688. Source: stats.nba.com + euroleague.net official pages.
- 3PA/FGA%: EL 37.59% vs NBA 32.44%. 3PA/100poss: EL 32.79 vs NBA 27.94.
- 2PA/100poss: NBA 58.29 vs EL 54.50.
- Efficiency: 2P% EL 52.90% vs NBA 51.11%; 3P% EL 36.38% vs NBA 35.62%; eFG% EL 53.95% vs NBA 52.14%.
- Trends: both leagues up in efficiency; NBA steeper recent eFG% rise; both down in 2PA/100poss; NBA nearly closed 3PT-reliance gap by recent seasons.
- Stats: Shapiro-Wilk non-normal → Mann-Whitney U, JASP v0.19.

## Wang & Zheng 2022 — NBA shooting patterns 2011–12→2020–21
- Resolution of 163→177: league-wide field goals attempted per game (both teams combined), not per-team. Games/season 1,059–1,230 via NBA shot chart API.
- 3PA share (24ft+): 22%→39% (~+1.85 pp/yr, p<.001). 16–24ft share: 21%→~7.2% (p<.001).
- Accuracy: rising for all distances except 3PT (flat, p=.150). Restricted area >60% every season; long range ~35–36%.
- Timing: Q1 accuracy highest; last 3-min segment of each quarter lowest accuracy; 2nd and 4th segments of each quarter highest attempt volume.
- Method: 5 distance bands, 16×3-min segments, Mann-Kendall trends, Matlab 2020a.

## Cross-paper anchors for analysis chapter
- 3P% ~35–38% stable across leagues/eras (all three papers agree directionally).
- Volume/reliance rises; accuracy flat (Wang NBA; Foteinakis both leagues).
- Context splits matter more than league label alone (Karamousalidis timing/offense-type; Foteinakis rule/court context).