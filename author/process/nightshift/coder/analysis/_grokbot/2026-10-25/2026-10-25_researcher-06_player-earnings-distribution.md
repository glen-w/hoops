# researcher-06: Player earnings distribution (G League, two-way, overseas, NBA inequality)
Fetch date for all sources: 2026-10-25. Files:
- `2026-10-25_researcher-06_earnings_ladder.csv`: the pay tiers, each with its source.
- `2026-10-25_researcher-06_nba_salaries_2026-27_snapshot.csv`: 461 contract rows from Basketball-Reference, used for the Gini calculation.

## Bottom line
**The pay ladder, 2025-26, as a share of the $154.647M salary cap:**
- G League standard salary: **$45,000**, or 0.029% of the cap.
- Two-way contract: **$636,435**, or 0.41%.
- Rookie minimum: **$1,272,870**, or 0.82%.

In 2026-27 the top NBA salary is Stephen Curry's **$62.59M**, about 38% of the $164.961M cap. That is roughly **1,350 times** the derived 2026-27 G League standard salary of $46,350.

**My own calculation of NBA salary inequality (2026-27 contracts snapshot):**
- **Gini 0.55** (0.546, one value per player; n = 455)
- **Top 10% of players take 37%** of salaries
- **Bottom half take 13%**
- Median **$6.65M** against a mean **$13.3M**

No published Gini for the 2023-CBA era was found, so this figure is **computed by me, not quoted**. The method and caveats are below.

**Overseas:** the best-paid EuroLeague player earns **$5.6M net** (Micic). Eurohoops's rule of thumb is to double net figures to compare with NBA gross pay, which gives about $11M. The 10th-highest EuroLeague salary is about $2.7–3M net. So a EuroLeague star earns about the same as an NBA rotation player on a mid-level contract, and far more than a G League or two-way player.

## What's new compared with the 23 Oct files
The 23 Oct run did not cover player pay. Everything here is new:
1. Primary sources for the 2025-26 and 2026-27 caps.
2. The terms of the first G League CBA (Oct 2025).
3. Two-way and Exhibit 10 amounts.
4. EuroLeague salaries and payrolls.
5. A computed Gini and top shares.
6. Five academic papers on salary inequality.

## 1. The ladder under the 2023 CBA
- **The 2023 CBA** runs 2023-24 to 2029-30, with a mutual opt-out after 2028-29. Players' share of BRI stays in the **49–51% band (currently 51%)**. Rules on minimum, maximum and rookie-scale salaries are unchanged. Two-way slots go **from 2 to 3** per team. The maximum Exhibit 10 bonus rises from $50,000 to $75,000 in 2023-24, then grows with the cap. (NBA, *2023 CBA Key Deal Points*, 28 Jun 2023, https://ak-static.cms.nba.com/wp-content/uploads/sites/4/2023/06/2023-CBA-Summary.pdf, SX8PRPSA. The PDF's text reads "$75,00", a typo for $75,000.)
- **Cap 2025-26:** $154.647M; tax $187.895M (JQUWETVU).
- **Cap 2026-27:** $164.961M; tax $200.428M; first and second aprons $209.015M and $221.686M; non-taxpayer MLE $15.044M (NBA.com, 30 Jun 2026, TEHS7JXJ).
- **Two-way contracts:** 50% of the zero-years minimum, which is **$636,435 for 2025-26**. Players are capped at 50 NBA games and must be in their fourth season or earlier. (G League "101", 7NIWPXA5.) The two-way amount for 2026-27 was **not checked** tonight.
- **Exhibit 10 bonus:** up to **$85,300 in 2025-26**, paid if a waived player spends 60 days with the team's G League affiliate (Hoops Rumors glossary, 2XNVSQS4).
- **G League's first CBA** (NBA G League and the NGBPU, 2025-26 to 2028-29; NBPA summary QPZG9RP4):
  - Standard salary **$45,000**, up 4.7%, then +3% a year.
  - An **extra $5,000** for players who stay the full season without any NBA compensation.
  - Affiliate players per team rise from 4 to 5.
- **Example:** Cui Yongxi's two-way contract was about $578,600 in 2024-25 (Economic Observer; see researcher-02).

## 2. Overseas
- **Eurohoops top-10 EuroLeague salaries, 2025-26** (24 Sep 2025, ERQBWESA):
  - Micic $5.6M net; Nunn $5.3M; Vezenkov $4.1M; Larkin $3.75M; …; the 10th–11th place is about $2.7M net.
  - Nine of the top ten are above roughly $3M net, a first.
  - The median is "at least one million net", which Eurohoops itself calls an educated guess; low confidence.
  - Eurohoops explains why net figures matter: tax varies by country (Spain is high; Dubai and Monaco have no income tax).
- **BasketNews team payrolls** (18 Mar 2026, DE8R2EFI):
  - Average EuroLeague team payroll is about **€14.5M**, up from about €9.5M in 2021-22. The median is €13.5–14.0M.
  - Panathinaikos is highest at about €26.5–27M.
  - The minimum required net salary threshold is €5.85M.
- **Not covered tonight:** CBA China, Australia's NBL and Japan's B.League. Their salary caps are public in principle, but I did not fetch them.

## 3. Inequality within the NBA (computed)
**Data:** Basketball-Reference, "2026-27 NBA Player Contracts", https://www.basketball-reference.com/contracts/players.html (4XEV32MB). Snapshot taken 2026-10-25: 461 rows, 455 unique players, $6.042B in total salaries.

**Method:** standard Gini on sorted salaries. Top-k share means the share of total salaries held by the top k% of players.

| Measure | Rows as listed (n=461) | Per player, summed across teams (n=455) | Rows ≥$1M (n=455) |
|---|---|---|---|
| Gini | 0.540 | **0.546** | 0.535 |
| Top 1% share | 4.9% | 5.1% | 4.9% |
| Top 10% share | 36.5% | **37.4%** | 36.6% |
| Bottom 50% share | 12.9% | 12.7% | 13.2% |
| Mean / median | $13.11M / $6.75M | $13.28M / $6.65M | $13.27M / $7.00M |
| p90/p10 | 15.7 | 17.2 | 16.1 |

**Caveats:**
1. The table includes dead-money rows for waived players, e.g. Ricky Rubio at CLE ($424,672) and Taj Gibson at NOP ($148,828). The ≥$1M column shows the result barely moves without them.
2. **Two-way contracts are excluded.** Adding about 90 two-way players at about $0.6–0.7M would push the Gini **up**.
3. It is an early-season snapshot.
4. It cannot be compared directly with Gini figures from other leagues or from the general population. I quote none here.

## 4. Academic anchors (filed to economics J3XVUX2F unless noted)
- **Hill & Jolly (2012)**, "Salary Distribution and Collective Bargaining Agreements: A Case Study of the NBA", *Industrial Relations* 51(2):342-363, doi:10.1111/j.1468-232x.2012.00680.x (4ENS66N4). Shows how successive CBAs, with their minimum, maximum and seniority rules, reshaped the NBA salary distribution. This is the closest analogue to what tonight's request asks for.
- **Berri & Jewell (2004)**, "Wage inequality and firm performance: Professional basketball's natural experiment", *Atlantic Economic Journal* 32(2):130-139, doi:10.1007/bf02298830 (NPQ4KNG9).
- **Simmons & Berri (2011)**, "Mixing the princes and the paupers: Pay and performance in the NBA", *Labour Economics* 18(3):381-388, doi:10.1016/j.labeco.2010.11.012 (7M6V9VZV).
- **Katayama & Nuch (2011)**, "A game-level analysis of salary dispersion and team performance in the NBA", *Applied Economics* 43(10):1193-1207, doi:10.1080/00036840802600335 (DSWUH78X).
- **Cyrenne (2017/18)**, "Salary Inequality, Team Success, League Policies, and the Superstar Effect", *Contemporary Economic Policy* 36(1):200-214, doi:10.1111/coep.12217 (94W7M53T). This is an **NHL** study, filed under other sports.

I only read the Crossref abstracts. I didn't open the papers, so I quote no Gini values from them.

**Found but not added:**
- Hoffer & Freidel, SSRN 10.2139/ssrn.2274725, on pay discrimination against foreign players.
- Naito & Takagi, SSRN 10.2139/ssrn.2988961.

## Unknowns
- 2026-27 two-way and minimum-salary amounts.
- A published Gini for the 2023 CBA era.
- Average G League pay including NBA-affiliated bonuses.
- Gross-equivalent EuroLeague pay by country.
