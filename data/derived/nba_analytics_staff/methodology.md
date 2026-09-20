# Methodology — NBA analytics department staff counts

**Artifact:** `data/derived/nba_analytics_staff/`  
**Access date:** 2026-09-20  
**Mentions target:** TEAM / front office / staff/roles (NBAstuffer analytics-dept list)

## Sources

- NBAstuffer, *NBA Teams That Have Analytics Department* (team-grouped staff directory):  
  https://www.nbastuffer.com/analytics101/nba-teams-that-have-analytics-department/

## Schema

### `nba_analytics_dept_counts.csv`
One row per current NBA franchise (30).

- `n_staff_heading` — integer in the page `Team (N)` heading (page claim)
- `n_staff_current_parsed` — rows whose Status starts with `Current`
- `has_analytics_dept_listed` — `yes` when section present

### `nba_analytics_dept_roster.csv`
One row per **Current** staffer parsed from the team table (name, position, last_updated).

## Blank / GAP rules

- No invented staffers or titles.
- If a franchise section is missing → `GAP` (none missing this pass).
- Former staff rows are **excluded** from counts and roster.
- Heading count and parsed Current count matched (148) on access date; if they diverge later, keep both columns and note the mismatch.

## Confidence

**MEDIUM** — third-party, crowd-updated directory, not an NBA official release. Fine for “which desks exist / rough headcount” prose; not for HR truth.

## Regenerate

Parse `div.nba-staff-view-team section.nba-team-section` tables; keep Status starting with `Current`.

## Non-goals

Do not scrape private org charts. Do not treat NBAstuffer as official. Org-chart CSVs already on main via other packs remain separate.
