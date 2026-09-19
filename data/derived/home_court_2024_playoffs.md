# Home-court advantage — 2024 NBA playoffs (derived)

**Repo target:** `glen-w/hoops` → `data/derived/home_court_2024_playoffs.md` (+ companion CSV)  
**Access date:** 2026-09-19 (Europe/Paris)  
**Phase 0 seed:** `hoops-phase0/studies/home-court-2024-playoffs.md`  
**Draft claim under test:** STADIUM binder — “home-court advantage appeared to evaporate in the 2024 playoffs” (unsourced).

## Verdict

**“Evaporated” is not supported.** Across all **82** 2024 NBA playoff games on Basketball-Reference’s schedule/results page, home teams went **48–34** (**58.54%**). That is a clear majority. Soft relative to older eras is a possible hedge; disappearance is not.

## Methodology

1. **Primary count surface:** [Basketball-Reference 2024 NBA Playoffs Summary](https://www.basketball-reference.com/playoffs/NBA_2024.html) series tables (Finals through first round). Label: **SECONDARY** stats site; box-score–backed schedule.
2. **Home definition:** In BRef’s `Away SCORE @ Home SCORE` lines, the team after `@` is the home team. The higher final score wins. No overtime special cases needed for the W/L tally.
3. **Independent recount (2026-09-19):** All 15 series’ game lines were parsed; **n = 82**, home **48–34**, **48/82 = 0.5854**. Matches Phase 0.
4. **No invented totals.** Blank preferred over guesses. Percentages shown only as explicit ratios of cited counts.
5. **Optional regular-season comparison:** Fox Sports reprint of an AP end-of-season numbers piece (2024-04-14) reports 2023–24 home **668–562** (**.5431**), called the worst home-court mark in league history (barely under **.5435** in 2020–21). Wire journalism, not an NBA Communications release → **MEDIUM**.
6. **Early-playoffs context (not a full-tournament substitute):** ESPN Insider (Kevin Pelton, 2024-04-25) notes first-round Game 1s **8–0** for home teams (fifth such sweep in the 16-team era) and ~**58%** Round 1 home wins over the prior four arena playoffs. Independently consistent with BRef R1 Game 1 lines for the 8–0 figure.

## Cited sources

| Label | URL | What it supports |
|-------|-----|------------------|
| SECONDARY (BRef) | https://www.basketball-reference.com/playoffs/NBA_2024.html | Full-playoffs home W–L / games / win % |
| SECONDARY (Fox / AP) | https://www.foxsports.com/articles/nba/inside-the-nba-numbers-lots-of-comebacks-no-homecourt-edge-3s-went-up-scoring-went-down | 2023–24 RS home 668–562 / .5431 / “worst … in league history” |
| SECONDARY (ESPN Insider) | https://www.espn.co.uk/nba/insider/story/_/id/40018981/2024-nba-playoffs-real-not-siakam-brunson-scoring | R1 Game 1s 8–0; recent R1 arena home ~58% |

Companion metrics table: [`home_court_2024_playoffs.csv`](home_court_2024_playoffs.csv) (`metric,value,source_url,as_of,confidence,notes`).

## Writer hedge (Scrivener — pursue later)

Do **not** edit Scrivener from this pack. Suggested replacement for the unsourced STADIUM sentence (paste when ready):

> Home-court advantage did not vanish in the 2024 playoffs: across 82 postseason games, home teams still went 48–34 (about 58.5 percent), per Basketball-Reference’s schedule. What *did* look historically soft was the preceding regular season, when home teams won only about 54.3 percent of games—the worst home mark on record in contemporary reporting.

Optional shorter cut:

> The 2024 playoffs did not erase home court—home teams won about 59 percent of 82 games (48–34)—even as the 2023–24 regular season set a historically low home win rate (~54.3 percent).

Guardrails for the rewrite:

- Cite BRef for the playoff count; cite Fox/AP (or equivalent) if the regular-season “worst ever” clause is kept.
- Do not claim HCA “returned” or “died”; stick to the two percentages.
- Do not promote the early 8–0 Game 1 streak into a full-playoffs story without labeling it first-round / early.

## Gaps / next research (optional)

- Official NBA Communications home/away season summary (if published) to upgrade the RS row from MEDIUM.
- Longer playoff-era home % series (decade buckets) if STADIUM wants historical soft-vs-hard framing beyond 2024.
- Point-margin / close-game splits are **out of scope** here; do not invent them.

## Confidence key

- **HIGH** — Recountable from named public game lists (BRef) or a contemporaneous specialist article whose cited early-round figure matches those lists.
- **MEDIUM** — Wire/trade secondary without an official NBA release behind the RS aggregate.
- **GAP** — Not filled in this pack.
