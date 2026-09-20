# The Thermostat That Is the Salary Cap

*Cap, tax, and apron history as a control system — an institutional-design essay in degrees of dollars*

A thermostat does not heat a room by wishing. It publishes a setpoint, tolerates a band, and—when the air misbehaves—engages secondary stages. The NBA’s salary architecture, read through the landed dollar history from official Communications releases, is exactly that sort of device: a primary Cap, a Tax Level that behaves like a second stage, a Minimum Team Salary that prevents cold spots, Mid-Level Exception bands that act as controlled vents, and—starting when the league began printing the names in the annual Cap PR—a First Apron and Second Apron that function as hard lockouts on certain maneuvers.

We will not invent prehistory. The cite-backed spine on disk covers seasons **2016-17** through **2026-27**. That is enough weather to watch the controller learn new stages.

## Setpoints on the wall

Salary Cap (USD, official PR integers):

| Season | Cap | Tax Level | Min team salary |
|--------|-----|-----------|-----------------|
| 2016-17 | 94,143,000 | 113,287,000 | 84,729,000 |
| 2017-18 | 99,093,000 | 119,266,000 | 89,184,000 |
| 2018-19 | 101,869,000 | 123,733,000 | 91,682,000 |
| 2019-20 | 109,140,000 | 132,627,000 | 98,226,000 |
| 2020-21 | 109,140,000 | 132,627,000 | — (not restated in COVID PR) |
| 2021-22 | 112,414,000 | 136,606,000 | 101,173,000 |
| 2022-23 | 123,655,000 | 150,267,000 | 111,290,000 |
| 2023-24 | 136,021,000 | 165,294,000 | 122,418,000 |
| 2024-25 | 140,588,000 | 170,814,000 | 126,529,000 |
| 2025-26 | 154,647,000 | 187,895,000 | 139,182,000 |
| 2026-27 | 164,961,000 | 200,428,000 | 148,465,000 |

From **2016-17** to **2026-27** the Cap rises from **$94.143M** to **$164.961M**—a ratio of about **1.75×**, an absolute rise of **$70.818M**. The Tax Level tracks above it the whole way, from **$113.287M** to **$200.428M**. The minimum team salary, when published, sits near ninety percent of Cap (the methodology note records that institutional habit; the CSV stores the PR dollars, not a recomputed percent).

## The flat year: a held setpoint

Control systems reveal themselves when someone tapes over the dial. For **2020-21**, the NBA/NBPA COVID adjustment PR held Cap and Tax **flat** versus **2019-20**: both seasons show Cap **109,140,000** and Tax **132,627,000**. Mid-level bands and minimums are blank in that row because the cited release did not restate them—blank means blank, not zero. In thermostat language: emergency hold. The room’s long-run heating resumed afterward (**2021-22** Cap **112,414,000**), then accelerated through the early **2020s**.

## Second-stage heat: Tax gap as hysteresis band

A Cap alone is a soft ceiling in a league that allows taxpaying. The interesting institutional measurement is the **Tax − Cap** gap—the width of the band where “over the Cap” and “into the Tax” are not the same sentence. In **2023-24**, the first season with published named aprons, Cap **136,021,000** and Tax **165,294,000** leave a gap of **29,273,000**. That band is where many roster stories actually live: not under the setpoint, not yet in the penalty stage.

## Aprons: lockout stages with printed names

Before **2023-24**, the annual Cap PRs in this extract do not publish First/Second Apron dollar columns; those cells stay empty on purpose (a prior informal “tax apron” is **not** backfilled from secondary sites). From **2023-24** onward the thermostat grows labels:

| Season | First Apron | Second Apron |
|--------|-------------|--------------|
| 2023-24 | 172,346,000 | 182,794,000 |
| 2024-25 | 178,132,000 | 188,931,000 |
| 2025-26 | 195,945,000 | 207,824,000 |
| 2026-27 | 209,015,000 | 221,686,000 |

In **2023-24**, relative to Tax **165,294,000**: First Apron sits **7,052,000** above Tax; Second Apron sits **10,448,000** above First. By **2026-27** the Second Apron prints at **221,686,000**—a second-stage lockout far above the Cap setpoint of **164,961,000**. Designers of multi-stage HVAC will recognize the pattern: each threshold disables a different class of behavior. The CSV does not editorialize *which* roster tools lock; the CBA structure notes live elsewhere. The dollar spine merely shows that the league chose to **publish** the stages beside the Cap.

## Vents: three Mid-Level Exception bands

When Cap, Tax, and Aprons are the dampers, the Mid-Level Exception bands are the intentional leaks that keep the system from sealing shut. Non-taxpayer / taxpayer / room MLE dollars (when stated) for the bookends:

- **2016-17:** 5,628,000 / 3,477,000 / 2,898,000  
- **2026-27:** 15,044,000 / 6,064,000 / 9,366,000  

The non-taxpayer MLE roughly triples across the decade of PRs; the taxpayer band stays the narrowest vent; the room exception sits between them by **2026-27**. That ordering is institutional design made numeric: different rooms get different authorized drafts of air.

## What “thermostat” is allowed to claim

It may claim that Cap dollars are a published setpoint that rose almost continuously after a one-year hold. It may claim that Tax Level is a durable second threshold above Cap. It may claim that named First and Second Aprons appear in the official annual Cap releases beginning **2023-24**, stacking above Tax. It may claim MLE bands scale with the system.

It may **not** invent apron dollars for **2016-17–2022-23**, invent tax *payments*, invent team payrolls, or pretend a secondary aggregator is an official PR. Blank cells are load-bearing silence.

In the end the metaphor earns its keep because the league’s own paperwork looks like a staged controller: setpoint (Cap), comfort band (toward Tax), penalty stage (Tax), then—once printed—apron lockouts, with MLE vents cut into the ductwork. Basketball argument will forever shout about who “broke” the Cap. The thermostat essay is quieter. It asks only: what temperatures did the institution agree to post on the wall, and when did it add another switch?

---

## Sources

Access date: **2026-09-20** (Europe/Paris). CSV `as_of`: **2026-09-20**. Confidence on cited PR rows: **HIGH**.

| Claim / figure | Cell / row | Path |
|----------------|------------|------|
| Cap / Tax / Min / Aprons / MLEs by season **2016-17…2026-27** | all numeric columns | `/workspace/hoops-thicken-book-data-2026-09-20/data/derived/salary_cap_apron/nba_salary_cap_apron_history.csv` |
| COVID flat Cap+Tax **2019-20 = 2020-21 = 109,140,000 / 132,627,000** | seasons `2019-20`, `2020-21` | same |
| First published aprons **2023-24**: FA **172,346,000**, SA **182,794,000** | season `2023-24` | same |
| **2026-27** Cap **164,961,000**, Tax **200,428,000**, FA **209,015,000**, SA **221,686,000** | season `2026-27` | same |
| Method (official `pr.nba.com` only; blanks = not stated; no aggregator backfill) | — | `/workspace/hoops-thicken-book-data-2026-09-20/data/derived/salary_cap_apron/methodology.md` |

Example official releases (also in `source_url` column):  
https://pr.nba.com/nba-salary-cap-2016-17-season/ · https://pr.nba.com/nba-nbpa-2020-21-season/ · https://pr.nba.com/nba-salary-cap-for-2023-24-season-set-at-136-021-million/ · https://pr.nba.com/2026-27-salary-cap/
