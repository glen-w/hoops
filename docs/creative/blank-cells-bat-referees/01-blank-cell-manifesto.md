# The Blank-Cell Manifesto

**Desk:** Glen's Hoops — creative, cite-backed  
**Access date:** 2026-09-20  
**Rule:** Voice and structure are imaginative; **every factual claim** traces to existing data in this repository. No invented numbers.

The blank cell is not a mistake. It is a grammatical fact.

---

## I. The COVID Stall

On 9 November 2020, the NBA and NBPA announced adjustments for the 2020–21 season. The salary cap held flat at $109,140,000 — the same figure from 2019–20. The tax level stayed locked at $132,627,000. And then the Mid-Level Exception rows went silent.

In `nba_salary_cap_apron_history.csv`, the 2020–21 season carries empty cells where other years list `non_taxpayer_mle_usd`, `taxpayer_mle_usd`, and `room_mle_usd`. The official press release cited does not restate them; the ledger leaves the blanks unfilled. This is not redaction. It is data's way of saying: what did not need adjustment was not republished.

The blank is evidence. It means the MLE values rolled forward from the prior year without formal reannouncement. The silence itself is a CBA artifact: when a global pandemic forces collective bargaining adjustments, only the changed numbers get the spotlight. What stays the same stays unprinted — and blank cells preserve that institutional grammar.

---

## II. The Pre-Apron Years

Before the 2023 CBA, "First Apron" and "Second Apron" did not exist as published dollar figures.

The `nba_salary_cap_apron_history.csv` file runs from 2016–17 forward. For the 2016–17 through 2022–23 seasons, the columns `first_apron_usd` and `second_apron_usd` are blank. Not zero — blank. The 2017 CBA included a tax apron as a concept, but the NBA Communications press releases for those seasons do not state an apron dollar threshold. The methodology note for 2016–17 is explicit: "Pre–named First/Second Apron era; tax apron existed under prior CBA but dollar apron not in this PR."

These blanks are not missing data. They are the paper trail of a rule that existed but was not yet named with a public price tag. When the 2023 CBA arrived, First Apron and Second Apron became published thresholds with dollar values and formal names: $172,346,000 and $182,794,000 for 2023–24. Before that moment, the cells stayed empty because the league's own announcements left them empty. The blank is fidelity to the source.

---

## III. The Minimum Salary Footnote

The 2020–21 row has one more intentional omission: `min_team_salary_usd` is blank.

In every other season from 2016–17 onward, the minimum team salary is published. For 2020–21, the COVID adjustment press release does not restate it. The ledger honors that silence. The value existed — the CBA formula did not evaporate — but the league did not republish it in that November 2020 announcement. What the source does not state, the CSV does not invent.

The blank cell becomes a timestamp. It says: this row reflects only what was formally communicated on that date. Filling in a calculated or assumed figure would erase the documentary record of what the league chose to say — and what it chose not to repeat.

---

## IV. The Ethics of the Empty String

Blank cells make uncomfortable reading. Software wants defaults. Analysts want complete matrices. But data ethics sometimes requires leaving a cell empty.

When a league does not publish a figure, inventing one — even if the formula is known — is to claim authority the dataset does not have. The blank preserves provenance. It tells future readers: *this value was not in the cited source on the cited date*. That is not a flaw. It is precision.

The `nba_salary_cap_apron_history.csv` file carries 13 rows (2016–17 through 2026–27, minus the split COVID entries). Seven seasons have blank First Apron cells. Seven seasons have blank Second Apron cells. One season (2020–21) has blank MLE and minimum salary cells. Those blanks are load-bearing: they hold the shape of institutional memory.

In a data-ethics vignette, the blank cell is the protagonist. It refuses to lie. It marks the edge of what can be cited. It is the most honest character in the table.

---

**Citations:**

- **2020–21 cap/tax freeze; blank MLE/min cells**: `data/derived/salary_cap_apron/nba_salary_cap_apron_history.csv`, row `season=2020-21` (cap=$109,140,000; tax=$132,627,000; MLE columns blank; min_team_salary_usd blank). Press release: https://pr.nba.com/nba-nbpa-2020-21-season/. Accessed 2026-09-20.
- **Pre–2023 blank apron cells**: Same CSV, rows `season=2016-17` through `season=2022-23` (7 seasons), columns `first_apron_usd` and `second_apron_usd` all blank. Methodology note for 2016–17: "Pre–named First/Second Apron era; tax apron existed under prior CBA but dollar apron not in this PR."
- **2023–24 First/Second Apron figures**: Same CSV, row `season=2023-24`, `first_apron_usd=172346000`, `second_apron_usd=182794000`. Press release: https://pr.nba.com/nba-salary-cap-for-2023-24-season-set-at-136-021-million/. Accessed 2026-09-20.
- **Dataset span**: Same CSV, 13 rows covering 2016–17 through 2026–27. Row count includes split COVID season entries.
