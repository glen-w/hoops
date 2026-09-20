# NBA players historical — Phase 1 summary stats

**Access:** 2026-09-20 (Europe/Paris / PT)  
**Universe file:** `nba_players_historical.csv`  
**Row count:** **4550**  
**Source:** teaching dump `player_data.csv` (columns: name, year_start, year_end, position, height, weight, birth_date, college), mirrored at [msyamkumar/cs220-projects](https://raw.githubusercontent.com/msyamkumar/cs220-projects/master/spring20/final/player_data.csv); commonly attributed to Basketball-Reference-derived public dumps (same schema as Kaggle “NBA Players data”). **Not** an official NBA Stats extract.

## Coverage (honest)

| Item | Value |
|------|-------|
| Players (rows) | 4550 |
| year_start range | 1947–2018 |
| year_end range | 1947–2018 |
| Draft fields | **blank in v1** (not in source dump) |
| Post-2018 debuts | **not in this dump** — see Phase 2 |
| “Every player ever” | **NOT claimed** |

Raw ESPN `player_core_YYYY.csv` snapshots (2002, 2010, 2015, 2020, 2024–2026) are retained under `data/raw/` for a later merge/dedup pass (draft_year available there for modern players).

## Body measures

| Metric | n | mean | median | notes |
|--------|--:|-----:|-------:|-------|
| Height (inches) | 4549 | 78.02 | 78 | parsed from ft-in |
| Weight (lb) | 4544 | 208.9 | 210.0 | |
| Career span (years, inclusive) | 4550 | 5.2 | 3.0 | year_end − year_start + 1 |

### Mean height by debut decade (year_start)

| Decade | n | mean height (in) |
|--------|--:|-----------------:|
| 1940s | 295 | 74.62 |
| 1950s | 384 | 76 |
| 1960s | 479 | 77.29 |
| 1970s | 684 | 77.67 |
| 1980s | 634 | 78.81 |
| 1990s | 689 | 78.72 |
| 2000s | 689 | 79.18 |
| 2010s | 695 | 78.85 |

## Position mix (as coded in dump)

{'G': 1574, 'F': 1290, 'C': 502, 'F-C': 388, 'G-F': 360, 'C-F': 219, 'F-G': 216}

## Names — modal parts (honesty lock)

**Never** string-mean a name. Report modal first and modal last **separately**, with distributions:

| Part | Mode | Count | Share of rows |
|------|------|------:|--------------:|
| First name | **John** | 91 | 2.0% |
| Last name | **Williams** | 73 | 1.6% |

**Composite label (optional prose only):** “modal-first + modal-last” → **John Williams** — this is a **juxtaposition of two modes**, not a person who existed under that full name in the data (coincidence possible but not asserted).

### Top 10 first names
[('John', 91), ('Bob', 87), ('Mike', 71), ('Jim', 68), ('Bill', 53), ('Chris', 50), ('Joe', 47), ('Tom', 45), ('George', 44), ('Larry', 41)]

### Top 10 last names
[('Williams', 73), ('Johnson', 65), ('Smith', 59), ('Jones', 53), ('Brown', 40), ('Davis', 40), ('Jackson', 30), ('Anderson', 24), ('Green', 23), ('Robinson', 22)]

## Phase 2+ expansion path

1. Dedup-merge ESPN sportsdataverse `player_core_*` (already downloaded) for 2019–2026 debuts + draft fields.
2. Optional: Basketball-Reference etiquette scrape / licensed dump for full all-time bios — document ToS; prefer bulk mirrors with attribution.
3. Add wingspan/combine where public (NBA Draft Combine).
