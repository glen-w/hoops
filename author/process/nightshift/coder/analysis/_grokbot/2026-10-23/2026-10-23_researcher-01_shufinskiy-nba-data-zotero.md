# shufinskiy/nba_data: Zotero entry for the FT-analysis data source

**Request:** 2026-10-22-researcher-01 (paper, high)
**Status:** done. I reused the existing Zotero item and filed it in the free-throws collection. Some of its metadata gaps need Glen's OK to fill (see below).

## Zotero
| key | item | collection(s) | created/reused |
|---|---|---|---|
| TFI7VXII | dataset: "shufinskiy/nba_data — multi-source PBP and shots bulk archive" | hoops/* repo citeables/open datasets / catalog (UCA95QWQ) **+ hoops/⭐game/skills/shooting/free throws (HN7AY374), added today** | reused (it already existed from 2026-09-25) |

The item already existed, so tonight's rules allowed me to add a collection and nothing more. I didn't edit its fields or tags. It currently has:
- no creator;
- `accessDate` 2026-09-25;
- empty version/date fields;
- an abstract written as a usage note (local research only, Apache-2.0 covers the repo, not the rows, NBA ToS still apply).

**Proposed field edits (need Glen's approval, not applied):**
- Creator (author, single-field name): `shufinskiy`. GitHub's API exposes no real name for this account (https://api.github.com/users/shufinskiy).
- `date`: 2026-07-17 (date of the last commit).
- `versionNumber`: commit `e829d46`.
- `accessDate`: 2026-10-23.
- `repository`: GitHub.
- `rights`: Apache-2.0.
- Abstract: add the README description below the existing usage note.

## What the repo is (from the README and GitHub API, checked 2026-10-23)
- README title: "Dataset NBA play-by-play data and shotdetails from 1996/1997 to 2024/25" (https://github.com/shufinskiy/nba_data).
- What it covers: play-by-play from **stats.nba.com** (from 1996/97), **pbpstats.com** (from 2000/01, which adds possession start type and timing) and **data.nba.com** (from 2016/17, which adds court coordinates). It also has **shot details** from 1996/97, playoff play-by-play and shot detail for all seasons (added 2023-07-11), and matchups 2017/18–2024/25 (added 2025-02-26). The loader also lists `cdnnba`, `nbastatsv3` and WNBA variants.
- The author's stated reason: stats.nba.com allows one game per request and limits requests, so pulling a season takes hours. Mirrors of the data are also on Kaggle and Google Drive.
- GitHub API facts:
  - Created 2023-01-07.
  - Last commit `e829d4678be1e075f99e5d41a1c5f97089be446b` on 2026-07-17, message "add full nba PO 2025/26". The repo already holds 2025/26 playoffs even though the README header still says 2024/25.
  - No tagged releases.
  - Apache-2.0 licence.
  - About 248 stars.
- Our FT analysis (2026-10-22, researcher-02) used the `nbastats_*` / `nbastats_po_*` play-by-play files and `shotdetail_*` (for game dates) for 2015-16 to 2023-24.

## Suggested citation strings
- Plain: shufinskiy (2026). *nba_data: NBA play-by-play and shot details, 1996/97–2025/26* [dataset, GitHub repository, commit e829d46]. Derived from stats.nba.com, pbpstats.com and data.nba.com. Apache-2.0. https://github.com/shufinskiy/nba_data (accessed 23 October 2026).
- Short in-text: "NBA play-by-play via the shufinskiy/nba_data mirror of stats.nba.com (2015-16 to 2023-24)."
- Caveat for the manuscript (suggestion): the licence covers the repository, not the underlying NBA data, so the data are best cited as derived from stats.nba.com.
