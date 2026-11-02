# Reconcile the new CSVs with the existing analysis/ CSVs

**Request:** 2026-10-21-coder-03 (high)
**Status:** done. Merged drafts are written to out/, and **no source files were modified.**

## What's in `sandbox/coder/analysis/`
| File | Content | Verdict |
|---|---|---|
| `attendance_2018_22.csv` | Header only (`season,team,attendance,notes`), no rows | Empty stub with a per-team grain. Nothing to merge |
| `national_tv_revenue.csv` | Header only (`season,category,value,unit,source`) | Empty stub. Nothing to merge |
| `league_income_ingredients.csv` | **Not a CSV.** It's one sentence: "League income ingredients CSV updated with cite-graded BRI/media/attendance/licensing data and methodology." | Placeholder that claims work which isn't there. **Needs Glen** |
| `attendance_2018_24.csv` (new) | 6 seasons, 2017-18 to 2022-23 | Has the content, but with errors (below) |
| `national_tv_revenue_2016_26.csv` (new) | 2 contract rows | Has the content, with sourcing and confidence issues |

## Recommendation: merge into the new files, don't overwrite blindly
- The old attendance and TV files contain **no data**, so nothing is lost by going with the new files' structure.
- The new files can't be used as they stand either, because of the errors below. Use the corrected drafts in out/.
- Retire the two empty stubs and the placeholder `league_income_ingredients.csv` (move them to an `_archive/`). I'd rather not delete them; that's Glen's call.
- Decide on one schema. The scaffolding doc (coder-05) specifies a **long format**: `season,category,value,unit,currency,source_url,as_of,confidence,notes`. The new CSVs are **wide**. I've drafted both, so Glen can pick.

## Errors found in `attendance_2018_24.csv`
| Row | Problem | Fix in the draft |
|---|---|---|
| 2017-18 | Average 17,914 is wrong. The source URL (`…fourth-straight-year`) **returns 404** | Average **17,987** (NBA PR 2023 release). Source replaced with the NBA PR 2019 release, which also gives **741 sellouts** |
| 2018-19 | Average 17,741 is wrong | Average **17,857** (NBA PR 2023) |
| 2019-20 | Marked GAP, "bubble, no fans". **Wrong:** about 971 games had crowds before the suspension | **≈17,274,600** (BRef league average 575,820 × 30), ≈17,788 per game, MEDIUM |
| 2020-21 | 671,000, average 893, capacity 25%, from RunRepeat. Unsupported (coder-02) | **1,492,605** (ESPN sum, a lower bound), **LOW**. Capacity and average left blank |
| 2021-22 | GAP, and the row is **malformed** (one field short, so the notes text lands in `confidence`) | **20,910,813**, average 17,186, 91.6% (SBJ, NBA paid), MEDIUM. Row fixed |
| 2022-23 | Correct | Kept as is |
| 2023-24 | **Missing,** although the file name says `_2018_24` | Added: **22,538,518**, average 18,324, 873 sellouts, 98% (NBA PR) |

## Issues found in `national_tv_revenue_2016_26.csv`
- **2016-25 deal.** The source was a theScore page in its NCAA-basketball section. I replaced it with SBJ (6 Oct 2014) and the NBA PR release. The NBA disclosed no dollar figures, so it stays **MEDIUM** as a reported value.
- **2025-36 deal.** Rated HIGH, but the $76B figure is **reported, not disclosed**, so I downgraded it to MEDIUM. The CBS source URL returns 406 to scripts. I used AP plus the NBA PR release (no $). The as_of date of 2024-06-17 came before the 24 Jul 2024 announcement.
- The per-partner split (Disney about $2.62B, NBC about $2.45B, Amazon about $1.8B a year) was **not re-verified** tonight.
- The file name says `2016_26`, but the second deal runs to 2035-36. The draft is renamed `2016_36`.

## Drafts written (out/)
- `2026-10-21_coder-03_attendance_2017_24_merged.csv`: wide, same columns as `attendance_2018_24.csv`, corrected and extended.
- `2026-10-21_coder-03_league_attendance_long_draft.csv`: the same data in the scaffolding's long schema. The schema allows only HIGH/MEDIUM/GAP, so 2020-21 LOW is mapped to MEDIUM with a note.
- `2026-10-21_coder-03_national_tv_revenue_2016_36_merged.csv`: TV deals with corrected sources and confidence.

## Source URLs (all resolved on 2026-10-21)
- NBA PR 2019 (2015-19 totals, 2018-19 sellouts): https://pr.nba.com/nba-attendance-even-with-last-years-record-mark
- NBA PR 2023 (2022-23, plus 2017-18 and 2018-19 averages): https://pr.nba.com/nba-sets-all-time-records-for-attendance-and-sellouts-during-2022-23-regular-season
- NBA PR 2024: https://pr.nba.com/nba-attendance-records-2023-24-regular-season/
- SBJ 2021-22: https://www.sportsbusinessjournal.com/Daily/Closing-Bell/2022/04/13/NBA/
- BRef 2019-20: https://www.basketball-reference.com/leagues/NBA_2020.html
- ESPN 2020-21: https://www.espn.com/nba/attendance/_/year/2021
- TV: https://www.sportsbusinessjournal.com/Daily/Issues/2014/10/06/Media/NBA-media/ · https://pr.nba.com/nba-partnerships-walt-disney-company-turner-broadcasting-system/ · https://apnews.com/article/nba-tv-deal-tnt-855da6a644947d74ad3330c0470a7c94 · https://pr.nba.com/nba-walt-disney-company-nbcuniversal-amazon-prime-video-media-agreements/
