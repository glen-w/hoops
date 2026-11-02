# Referee bias, extended: race, stars, market size and the Last Two Minute reports

**Request:** 2026-10-24-pm-researcher-04 · **Status:** done (the payroll-bias part is partial: no direct study found) · Grok Bot nightshift, 25 Oct 2026 (Europe/Paris) · Zotero keys in [brackets]

**Extends:** `prior/2026-10-23_researcher-06_ref-bias-causal-designs.md`, which covers COVID/home advantage, Gong 2022 (L2M before/after) and Price, Remer & Stone 2012. New tonight: racial bias, star bias, market/betting-line bias, more L2M studies, and a quick L2M table (`2026-10-25_researcher-04_l2m-home-error-table.csv`).

## Bottom line (suggestions, not orders)
- **Race: the best-known result is real and then faded.** Price & Wolfers (2010) found NBA players drew more fouls (1992–2004) when the refereeing crew was mostly of the other race, enough to tip some game outcomes. A follow-up (Pope, Price & Wolfers 2018) found the bias was gone after the May 2007 media coverage. *Awareness reduced it.* Using the L2M reports, Mocan & Osborne-Christenson (2022) found no racial bias in calls made, but in-group favouritism in **missed** calls (wrongful non-calls).
- **Stars: some evidence, small and specific.** All-Stars got +0.32 more free-throw attempts per minute in fourth quarters of the 2011 playoffs (Caudill, Mixon & Wallace 2014). Pelechrinis (2023, L2M 2015–22) found 12 players with a significantly kinder whistle, mostly stars (Wade, Chris Paul, Carmelo Anthony, Towns), but no player with a harsher one and no team bias. Two other studies found no star bias (Deutscher 2015; Morgulev et al. 2018).
- **Home bias in the L2M reports is small and shrinking.** Pelechrinis (2023): +146 favourable calls for home teams across 2015–22 (≈1.2 points total), larger in the playoffs, almost gone since 2020. My quick tally of the same public dataset gives the same picture: errors favoured the home team **50.5%** of the time overall, **50.0%** in the regular season, and **56.9%** in the playoffs.
- **Market size / payroll:** I found **no** study testing payroll favouritism directly. Zimmer & Kuethe (2009) show bigger-market teams did better than betting lines predicted in the 2003–08 playoffs, and early series games ran closer, which suggests longer series. This is consistent with bias but doesn't show referees cause it. Rodenberg (2011) tested Pat Riley's specific complaints about two referees and found no support.
- **New (2025):** Belasen, Belasen & Olbrecht link L2M errors to the betting line. Referees make 23% fewer incorrect calls against away underdogs and 42% fewer against home underdogs. Read as "refs help keep games close", not as proof of intent.

## Table 1: designs and findings (new items)
| Citation [Zotero] | DOI | Data / design | Finding | Bias type | Confidence |
|---|---|---|---|---|---|
| Price & Wolfers (2010) *QJE* 125(4):1859–1887 [NK7GV5BB] | 10.1162/qjec.2010.125.4.1859 | Box scores 1992–2004 (per my notes from the NBER abstract; check exact span); player, referee and game fixed effects | More fouls with an opposite-race crew; big enough to matter for wins | Race | high |
| Pope, Price & Wolfers (2018) *Mgmt Sci* 64(11):4988–4995 [2RG7ZW5N] | 10.1287/mnsc.2017.2901 | Before/after the 2007 media coverage | Bias still there 2003–06; gone after 2007 | Race | high |
| Mocan & Osborne-Christenson (2022) NBER w29860 [VDAAJJZT] | 10.3386/w29860 | L2M reports | No racial bias in calls or incorrect calls; in-group favouritism in wrongful non-calls | Race (missed calls) | medium (working paper) |
| Pelechrinis (2023) *Sci Rep* 13 [IV3MXGTR] | 10.1038/s41598-023-31799-y | L2M 2015–22, Monte Carlo permutation tests | Home +146 calls (~1.2 pts); 12 players favoured (mostly stars); no team bias; no racial bias in technicals | Home, star, race | high |
| Deutscher (2015) *J Sports Analytics* 1(2):91–96 [RGIPH5J6] | 10.3233/jsa-150012 | 113 games, 1,229 L2M calls (2015) | No bias: home, star, race or trailing team | All | medium (small, early sample) |
| Caudill, Mixon & Wallace (2014) *Int J Econ Business* 21(2):245–253 [B5JTBBID, reused] | 10.1080/13571516.2014.903110 | 2011 playoffs | All-Stars +0.32 FTA/min in fourth quarters | Star | medium (one postseason) |
| Morgulev et al. (2018) *Front Psychol* 9:2637 [MIMQY2UV, reused] | 10.3389/fpsyg.2018.02637 | Elite basketball referees' decisions (league per Pelechrinis is Israeli; check) | No star or team bias | Star | medium |
| Zimmer & Kuethe (2009) *JQAS* 5(3) [6CFM42MU, reused] | 10.2202/1559-0410.1149 | Playoffs 2003–08 vs betting lines | Larger-market teams beat expectations; early-series games closer | Market size | medium (consistent with bias, doesn't identify it) |
| Rodenberg (2011) *JQAS* 7(2) [IX9PV2KW] | 10.2202/1559-0410.1326 | Tests Pat Riley's allegations against two referees | Not supported; Heat slightly *better* than expected with one of them | Team/specific | medium |
| Belasen, Belasen & Olbrecht (2025) *JSE* 26(8):913–935 [UNKGIZMJ] | 10.1177/15270025251369447 | L2M errors by betting line | Fewer incorrect calls against underdogs (−23% away, −42% home) | Game-closeness | medium (new; not yet replicated) |
| Price, Remer & Stone (2012) *JEMS* [RKPR3BR2, reused] | 10.1111/j.1530-9134.2011.00325.x | Discretionary calls | Home and trailing teams favoured | Home, closeness | high |
| Gong (2022) *JSE* [HE36834C, reused] | 10.1177/15270025211073337 | L2M before/after COVID | No crowd-driven home bias | Home | high |

Mentioned but not added: Barrett (2021), an undergraduate study of salary-star bias cited by Pelechrinis. I didn't verify it.

## Table 2: quick L2M tally (descriptive only)
Source: atlhawksfanatic/L2M, `1-tidy/L2M/L2M.csv` (MIT licence; last push 19 May 2025), fetched 25 Oct 2026 [GRFI6F5U]. https://github.com/atlhawksfanatic/L2M. The coverage is 1 Mar 2015 to 6 Nov 2023: 3,682 games and 75,672 rows. I counted only reviewed calls with a decision: CC = correct call, IC = incorrect call, INC = incorrect non-call. CNC (correct non-call) was excluded because the league recorded it inconsistently across seasons. A call "favours home" when it is an incorrect non-call on the home side or an incorrect call against the away side, and vice versa.

| Scope | Reviewed calls | Errors (IC+INC) | Errors favouring home | Errors favouring away | Home share |
|---|---|---|---|---|---|
| All | 21,197 | 5,370 | 2,711 | 2,659 | **50.5%** |
| Regular season | – | – | 2,480 | 2,484 | 50.0% |
| Playoffs (246 games) | – | – | 231 | 175 | **56.9%** |

By season label in the dataset (the label is the season's end year, e.g. 2015 = 2014–15 from 1 Mar 2015; home share of errors): 2015 51.2 · 2016 52.7 · 2017 46.0 · 2018 52.1 · 2019 52.0 · 2020 48.1 · 2021 48.5 · 2022 51.5 · 2023 51.1 · 2024 48.0 (partial). The error rate is 22–28% of reviewed calls. Full numbers are in the CSV.

**Caveats:** this is a raw tally with no significance tests and no controls. L2M only covers close games' final minutes, and the NBA itself grades its own referees. Reports for 2024–25 onwards are not in this dataset; the NBA publishes them as PDFs. The playoff figure is consistent with Pelechrinis's "larger in playoffs", but on 406 errors it shouldn't be quoted as precise.

## What the book can safely say
The famous finding that white referees called more fouls on Black players, and vice versa, held up, and then disappeared once it made headlines. That is a rare case of publicity fixing a bias. In the NBA's own late-game audits, mistakes split almost evenly between home and away teams, a bit more in the home team's favour in the playoffs. A handful of stars do get a slightly kinder whistle. Nobody has shown that referees favour rich or big-market teams, though big-market teams did beat the betting odds in the 2000s playoffs.

## Unknowns / next steps
- Payroll favouritism: no study found. A possible test merges L2M with team payroll (data source not checked tonight).
- Barrett 2021: unverified.
- Morgulev et al.: confirm the data are Israeli, not NBA.
