# NBA salary cap / tax / apron / MLE history — verification + derived numbers

Access date: 2026-10-22 (coder tick, nightshift 2026-10-19 window)
Canonical table (now on main): https://raw.githubusercontent.com/glen-w/hoops/main/data/derived/salary_cap_apron/nba_salary_cap_apron_history.csv
Zotero entry: bib/glen-w/hoopsHoopsDerivedNBA2026 (still says "pending data PR — not yet on main"; URL field empty → stale, see Open items)
Regenerator: `python3 -I analysis/salary_cap/cap_growth.py <path to canonical csv>`

Rule: verify only; no new figures beyond the official releases. Blank stays blank.

## 1. Verification — canonical CSV vs official league releases (re-fetched 2026-10-22)

Every field below was re-read from the league release and compared with the canonical CSV.
Result: **all 11 seasons match** on cap, tax, minimum team salary, first/second apron and all three MLEs (USD, $M shown).

Provenance caveat: both sides of this comparison were read through a web-fetch extraction step (release pages and the canonical CSV), not a byte-level diff of the raw file. The canonical CSV's own `source_url` column was not inspected this tick; the URLs below are the pages this check fetched.

| season | release date | cap | tax | min team | 1st apron | 2nd apron | NT-MLE | T-MLE | room MLE | source |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016-17 | 2016-07-02 | 94.143 | 113.287 | 84.729 | — | — | 5.628 | 3.477 | 2.898 | https://pr.nba.com/nba-salary-cap-2016-17-season |
| 2017-18 | 2017-06-30 | 99.093 | 119.266 | 89.184 | — | — | 8.406 | 5.192 | 4.328 | https://pr.nba.com/nba-salary-cap-2017-18-season |
| 2018-19 | 2018-07-01 | 101.869 | 123.733 | 91.682 | — | — | 8.641 | 5.337 | 4.449 | https://www.nba.com/news/nba-salary-cap-set-2018-19-season |
| 2019-20 | 2019-06-30 | 109.140 | 132.627 | 98.226 | — | — | 9.258 | 5.718 | 4.767 | https://www.nba.com/news/nba-salary-cap-2019-20-season-set-10914-million |
| 2020-21 | 2020-11-09 | 109.140 | 132.627 | blank | — | — | blank | blank | blank | https://pr.nba.com/nba-nbpa-2020-21-season/ |
| 2021-22 | 2021-08-02 | 112.414 | 136.606 | 101.173 | — | — | 9.536 | 5.890 | 4.910 | https://pr.nba.com/nba-salary-cap-for-2021-22-season-set-at-112-414-million |
| 2022-23 | 2022-06-30 | 123.655 | 150.267 | 111.290 | — | — | 10.490 | 6.479 | 5.401 | https://pr.nba.com/nba-salary-cap-2022-23-season/ |
| 2023-24 | 2023-06-30 | 136.021 | 165.294 | 122.418 | 172.346 | 182.794 | 12.405 | 5.000 | 7.723 | https://pr.nba.com/nba-salary-cap-for-2023-24-season-set-at-136-021-million/ |
| 2024-25 | 2024-06-30 | 140.588 | 170.814 | 126.529 | 178.132 | 188.931 | 12.822 | 5.168 | 7.983 | https://www.nba.com/news/nba-salary-cap-set-2024-25-season |
| 2025-26 | 2025-06-30 | 154.647 | 187.895 | 139.182 | 195.945 | 207.824 | 14.104 | 5.685 | 8.781 | https://pr.nba.com/nba-salary-cap-2025-26-season/ |
| 2026-27 | 2026-06-30 | 164.961 | 200.428 | 148.465 | 209.015 | 221.686 | 15.044 | 6.064 | 9.366 | https://pr.nba.com/2026-27-salary-cap/ |

Notes
- "—" = the fetched release text contains no first/second apron line. The canonical CSV leaves these blank. Correct: do not backfill from secondary trackers.
- **Apron guardrail:** pre-2023-24 blanks mean "not stated in the fetched release", NOT "no apron existed". Hoops Rumors (https://hoopsrumors.com/2021/08/salary-cap-tax-line-set-for-2021-22-nba-season.html, via search snippet) lists a 2021-22 "tax apron" of $143.002M "per the league release", but the fetched pr.nba.com 2021-22 page showed no apron. Unresolved → logged as UNVERIFIED, not entered. Prose must not say "aprons began with the 2023 CBA" unless a cited source says so; the 2023 CBA introduced a *second* apron/first-vs-second structure only if a fetched source confirms it.
- 2020-21: the joint NBA–NBPA release (2020-11-09) states cap $109.140M and tax $132.627M only — unchanged from 2019-20. Min team salary and MLEs are not in that release → blank. Do not compute 90% × cap.
- 2023-24 min team salary: official release says $122.418M; ingredients CSV note records Spotrac $122,418,900. Canonical CSV uses 122418000 (official). Consistent.
- Cross-file check: `data/derived/league_income_ingredients.csv` cap/tax/min rows for 2022-23 → 2025-26 and 2025-26 aprons agree with the canonical CSV.
- 2018-19, 2019-20, 2024-25 were verified on nba.com news pages (league site), not pr.nba.com. Same figures.

## 2. Derived numbers (DERIVED — hand-computed from the table above; rerun cap_growth.py to regenerate)

Formula: YoY = cap_t / cap_(t-1) − 1. Inputs in $M.

| season | cap $M | prior cap $M | YoY cap |
|---|---|---|---|
| 2016-17 | 94.143 | — | — |
| 2017-18 | 99.093 | 94.143 | 5.26% |
| 2018-19 | 101.869 | 99.093 | 2.80% |
| 2019-20 | 109.140 | 101.869 | 7.14% |
| 2020-21 | 109.140 | 109.140 | 0.00% |
| 2021-22 | 112.414 | 109.140 | 3.00% |
| 2022-23 | 123.655 | 112.414 | 10.00% |
| 2023-24 | 136.021 | 123.655 | 10.00% |
| 2024-25 | 140.588 | 136.021 | 3.36% |
| 2025-26 | 154.647 | 140.588 | 10.00% |
| 2026-27 | 164.961 | 154.647 | 6.67% |

- Cumulative 2016-17 → 2026-27: 164.961 / 94.143 − 1 = **+75.22%**.
- CAGR over 10 season steps: (164.961 / 94.143)^(1/10) − 1 = **5.77%**.

Tax / cap (tax_level ÷ salary_cap): 2016-17 1.203; 2017-18 1.204; 2018-19 1.215; 2019-20 through 2026-27 each 1.215.

Apron gaps above the tax line (formula: apron − tax, $M):

| season | tax | 1st apron | 1st − tax | 2nd apron | 2nd − tax |
|---|---|---|---|---|---|
| 2023-24 | 165.294 | 172.346 | 7.052 | 182.794 | 17.500 |
| 2024-25 | 170.814 | 178.132 | 7.318 | 188.931 | 18.117 |
| 2025-26 | 187.895 | 195.945 | 8.050 | 207.824 | 19.929 |
| 2026-27 | 200.428 | 209.015 | 8.587 | 221.686 | 21.258 |

### Interpretation guardrails (for the researcher)
- The 2020-11-09 release says that in subsequent seasons *of that CBA* cap and tax rise by a minimum 3% and maximum 10% over the prior season. That rule is cited for the 2017 CBA as amended only. The 10.00% steps in 2023-24 and 2025-26 fall under the 2023 CBA; this pack has no fetched source for the 2023 CBA's growth limit → report those steps as numbers only, do not explain them with the 2020 rule.
- Cap ≠ payroll ≠ BRI. The cap is BRI-derived under the CBA but is a threshold, not money spent.

### Side-by-side only (do not merge measures)
Per the league-income source map, media revenue and cap are different measures. Shown next to each other for context, no ratio drawn:

| season | official cap $M (HIGH) | per-team national TV revenue $M (MEDIUM, Sportico 2025-11-12) |
|---|---|---|
| 2024-25 | 140.588 | 103 |
| 2025-26 | 154.647 | 143 |

Source for TV column: https://www.sportico.com/leagues/basketball/2025/nba-revenue-projected-2025-26-season-1234876505/ (secondary; league declined comment on projections).

## Open items
1. Zotero `bib/glen-w/hoopsHoopsDerivedNBA2026`: update note/URL — CSV is now on main at the raw URL above.
2. Run `cap_growth.py` once against the canonical CSV and diff its output with section 2 (hand-computed here; the script was not executed this tick).
3. 2023 CBA cap-growth limit: fetch the CBA Article VII text (already in source register as OFFICIAL) before any prose explains the 10% steps.
4. Pre-2023-24 apron: resolve Hoops Rumors 2021-22 "tax apron $143.002M" vs pr.nba.com page (no apron shown). Check full release text or CBA Article VII; enter only if an official source states it.
5. 2024-25 attendance total: still GAP after 2026-10-22 search (only "exceeded 22.3 million" via SBJ/theScore; no official exact total found).
