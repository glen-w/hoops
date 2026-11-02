# NBA cap growth rules: why some seasons are exactly +3% or +10%

Access date: 2026-10-22 (Europe/Paris), tick r481.
Data: `data/derived/salary_cap_apron/nba_salary_cap_apron_history.csv` on `glen-w/hoops` main, re-fetched 2026-10-22 through a web-fetch extractor (raw file not diffed byte for byte).
Method: every percentage below was worked out by hand. `cap_growth.py` has **not** been run yet (no shell this tick). Treat the table as a check target for the script, not as script output.

## Finding

Four seasons land exactly on a rule bound, and the Tax Level moves with the Salary Cap each time:

| Season | Cap growth | Tax growth | Bound hit |
|---|---|---|---|
| 2021-22 | +3.000% | +3.000% | floor (3%) |
| 2022-23 | +10.000% | +10.000% | ceiling (10%) |
| 2023-24 | +10.000% | +10.000% | ceiling (10%) |
| 2025-26 | +10.000% | +10.000% | ceiling (10%) |

So the "10% jumps" are **three** seasons (2022-23, 2023-24, 2025-26), not two, and the earliest one comes before the 2023 CBA.

## Full year-on-year table (hand-computed from main CSV)

| Season | Cap (USD) | Cap YoY | Tax Level (USD) | Tax YoY |
|---|---|---|---|---|
| 2016-17 | 94,143,000 | n/a | 113,287,000 | n/a |
| 2017-18 | 99,093,000 | +5.258% | 119,266,000 | +5.278% |
| 2018-19 | 101,869,000 | +2.801% | 123,733,000 | +3.745% |
| 2019-20 | 109,140,000 | +7.138% | 132,627,000 | +7.188% |
| 2020-21 | 109,140,000 | +0.000% | 132,627,000 | +0.000% |
| 2021-22 | 112,414,000 | +3.000% | 136,606,000 | +3.000% |
| 2022-23 | 123,655,000 | +10.000% | 150,267,000 | +10.000% |
| 2023-24 | 136,021,000 | +10.000% | 165,294,000 | +10.000% |
| 2024-25 | 140,588,000 | +3.358% | 170,814,000 | +3.340% |
| 2025-26 | 154,647,000 | +10.000% | 187,895,000 | +10.000% |
| 2026-27 | 164,961,000 | +6.669% | 200,428,000 | +6.670% |

Cumulative cap, 2016-17 to 2026-27: +75.22% over 10 year-on-year steps, which is 5.77% a year compounded. This matches the hand figures reported last tick.

## Rule sources

1. **Official, primary.** NBA Communications, "NBA and NBPA agree on 2020-21 season start and adjustments to CBA", 2020-11-09, https://pr.nba.com/nba-nbpa-2020-21-season/
   - "For the 2020-21 season, the Salary Cap will be $109.140 million and the Tax Level will be $132.627 million."
   - "In subsequent seasons of the CBA, the Salary Cap and Tax Level will increase by a minimum of three percent and a maximum of 10 percent over the prior season."
2. **Secondary: the 10% limit for 2023-24.** Rory Maher, Hoops Rumors, 2022-09-09, citing ESPN's Bobby Marks: "there is a 10% limit on how much the salary cap can increase from this season to next", "due to the 'financial hardship' caused by the COVID-19 pandemic", and "$136MM is the maximum possible cap for the 2023/24 season." https://hoopsrumors.com/2022/09/2023-24-salary-cap-projection-increases-by-1mm.html
3. **Secondary: 2023 CBA cap smoothing.** James Herbert, CBS Sports, 2025-03-25: the cap "can increase by only 10% per season"; the 2025-26 rise is "the maximum increase allowed under the collective bargaining agreement." https://www.cbssports.com/nba/news/nba-salary-cap-to-rise-by-10-for-2025-26-season-what-reported-increase-means-for-aprons-luxury-tax-more/

## Which rule applies to which season (wording safe for prose)

- **2021-22 (+3%) and 2022-23 (+10%):** the 2020-11-09 NBA/NBPA adjustment. This is a primary source, and the arithmetic matches it exactly.
- **2023-24 (+10%): ambiguous.** The cap was announced 2023-06-30 and the 2023 CBA took effect 2023-07-01. Both the 2020 adjustment and the 2023 CBA (as reported) limit growth to 10%. Don't say which one governed until Article VII and the transition clauses have been read.
- **2025-26 (+10%):** 2023 CBA cap smoothing. Secondary sources only until Article VII is read.
- **2024-25 (+3.358%):** don't claim a 3% floor under the 2023 CBA. The floor is documented only in the 2020 adjustment.
- **2026-27 (+6.669%):** the 10% ceiling did not bind this season.

## Check: bound × prior figure, rounded to the nearest $1,000

| Season | Line | Prior × factor | Published |
|---|---|---|---|
| 2021-22 | Cap | 109,140,000 × 1.03 = 112,414,200 | 112,414,000 |
| 2021-22 | Tax | 132,627,000 × 1.03 = 136,605,810 | 136,606,000 |
| 2022-23 | Cap | 112,414,000 × 1.10 = 123,655,400 | 123,655,000 |
| 2022-23 | Tax | 136,606,000 × 1.10 = 150,266,600 | 150,267,000 |
| 2023-24 | Cap | 123,655,000 × 1.10 = 136,020,500 | 136,021,000 (halfway case) |
| 2023-24 | Tax | 150,267,000 × 1.10 = 165,293,700 | 165,294,000 |
| 2025-26 | Cap | 140,588,000 × 1.10 = 154,646,800 | 154,647,000 |
| 2025-26 | Tax | 170,814,000 × 1.10 = 187,895,400 | 187,895,000 |

Every published figure equals the bound applied to the prior published figure, rounded to the nearest $1,000.

## Internal consistency check (DERIVED)

The 2021-22 official release states that the minimum team salary is 90% of the Salary Cap. For 2023-24:
- 90% × 136,020,500 (unrounded 110% cap) = 122,418,450, which rounds to **122,418,000**. That is the published figure.
- 90% × 136,021,000 (rounded cap) = 122,418,900, which rounds to 122,419,000. That is not the published figure.

This suggests the league took the minimum from the exact 110% figure before rounding. It assumes the 90% rule still applied in 2023-24. It is a derived inference, not a sourced fact.

## Not claimed / open

- **2023 CBA Article VII text not read.** The NBPA PDF (https://imgix.cosmicjs.com/25da5eb0-15eb-11ee-b5b3-fbd321202bdf-Final-2023-NBA-Collective-Bargaining-Agreement-6-28-23.pdf, linked from https://nbpa.com/cba) was fetched (2.7 MB), but the extractor returned only compressed PDF streams. It needs `pdftotext` in the daytime pass. Extract:
  - the Art. VII §2 cap formula;
  - any 110% or smoothing clause, and any floor;
  - the transition rule that says which agreement set the 2023-24 cap.
- Don't write prose that says the 2023 CBA "introduced" the 10% limit. The official 2020 release shows a 10% ceiling already in force from 2021-22 onward.
