# Methodology — NBA salary cap / tax / apron history

**Access date:** 2026-09-20 (Europe/Paris)  
**Product:** `data/derived/salary_cap_apron/nba_salary_cap_apron_history.csv`  
**Rule:** cite-backed only; blank cells mean the cited official PR did not state that figure — **no invented numbers**.

## Why this table

Book chapters on CBA / salary / front-office need a single season-grain spine for Salary Cap, Tax Level, Minimum Team Salary, First/Second Apron (when published), and the three Mid-Level Exception bands. Repo already has CBA *structure* JSON (2017/2023) but not a dollar-level history. This fills that gap from **primary** NBA Communications releases.

## Source class

| Priority | Source | Use |
|----------|--------|-----|
| 1 | `pr.nba.com` annual “Salary Cap … set at …” releases | Cap, Tax, Min, Aprons (when named), MLEs |
| 1 | `pr.nba.com` 2020-11-09 NBA/NBPA COVID CBA adjustment | Cap + Tax held flat for 2020-21 |
| — | Aggregators (RealGM, Spotrac, etc.) | **Not used** for cell values |

Tag index used for discovery: https://pr.nba.com/tag/salary-cap/

## Schema

| Column | Meaning |
|--------|---------|
| `season` | NBA season label (e.g. `2023-24`) |
| `announced_date` | Date on the PR |
| `salary_cap_usd` | Salary Cap (integer USD) |
| `tax_level_usd` | Luxury Tax Level |
| `min_team_salary_usd` | Minimum Team Salary (often stated as 90% of Cap) |
| `first_apron_usd` | First Apron Level (blank before 2023-24 PR naming) |
| `second_apron_usd` | Second Apron Level (blank before 2023-24; created by 2023 CBA) |
| `non_taxpayer_mle_usd` / `taxpayer_mle_usd` / `room_mle_usd` | Three MLE bands when stated |
| `source_url` / `source_title` | Official PR |
| `as_of` | Access date for this derive |
| `confidence` | `HIGH` when figures copied from official PR body |
| `notes` | Caveats (COVID flat year; pre-apron naming; blanks) |

## Coverage

Seasons **2016-17 through 2026-27** (11 rows). Apron columns populated only from **2023-24** onward, when NBA Communications began publishing First/Second Apron dollars in the annual Cap PR.

## Explicit non-claims

- Pre-2023 “tax apron” dollar levels from secondary sites are **not** backfilled.
- CBA PDF article text is **not** scraped into this CSV (structure lives under `data/cba/`; cite structure metadata separately).
- Player salaries, team payrolls, and luxury-tax *payments* are out of scope.

## Regeneration

Manual: open each `source_url`, copy stated million figures × 1,000,000 into integers. Prefer full PR body over tag teasers.
