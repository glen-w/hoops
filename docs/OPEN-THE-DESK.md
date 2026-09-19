# Open the Desk — Writer's Field Guide

**For**: Hoops manuscript authors working in Scrivener  
**Purpose**: Connect binder sections → CHAPTER-MAP → derived data → citation paths  
**Status**: Three starter journeys; expand as desk matures

---

## Journey A: Salary-Cap Clause Lookup

**When to use**: Writing about CBA rules, salary cap exceptions, or contract structures mid-draft.

### Steps

1. **Scrivener binder hint**: `CBA / salary cap / CBA articles` or `CBA / defined terms / CBA glossary`

2. **CHAPTER-MAP row IDs**: 
   - Row 65 (CBA / salary cap / CBA articles)
   - Row 66 (CBA / defined terms / CBA glossary)
   - Row 67 (CBA / Article I / Definitions)
   - Row 69 (CBA / Article VII / Team Salary)
   - Row 70 (CBA / Article VII / Section 6 / Exceptions (MLE))

3. **Derived paths**:
   - `docs/CBA-LOOKUP.md` — CLI reference for quick lookups
   - `scripts/cba_lookup.py` — lookup script
   - `data/cba/2023/derived/structure.json` — 42 articles, 279 sections with clause IDs, page ranges
   - `data/cba/2023/derived/defined_terms.json` — 83 defined terms from Article I with locators
   - `data/cba/2023/derived/headings_index.json` — section-level index

4. **How to cite**:
   - **Structure lookup**: Run `python scripts/cba_lookup.py "Article VII"` to get clause ID, page range
   - **Example**: "CBA Art. VII §1 (pp. 42–44)" or "as defined in Article I(f) (Average Player Salary)"
   - **Defined term**: Run `python scripts/cba_lookup.py --term "Salary Cap"` for locator
   - **Note CBA edition**: 2023 is default; use `--edition 2017` flag if comparing editions

### Status caveats

- **Structure lookup**: ✅ **ready** — clause IDs, page ranges, and metadata are in committed JSON
- **Verbatim quotes**: ⚠️ **quotes_need_pdf** — fulltext extraction requires local PDF (gitignored); structure-based citations work without it
- **PDF SHA-256**: `cf59d43fe46f63d7ba07364563046d766c487c26032fcc88432310d47effd9d9` (2023 edition)
- **Fixture mode**: If local PDF missing, page ranges may show `[fixture - needs_local_pdf]`; clause IDs and titles still usable

### Open risks

- CBA body text not committed to git (PDFs gitignored for size/licensing)
- Direct quote extraction needs local PDF placement at `data/raw/cba/2023/cba.pdf`
- 2017 CBA has parallel structure files; use `--all-editions` flag to compare

---

## Journey B: Franchise Chapter (Teams Desk)

**When to use**: Writing team profiles, ownership structure, or league comparisons.

### Steps

1. **Scrivener binder hint**: `TEAM / {team name} / front office` (rows 27–56 for NBA teams) or `LEAGUE / teams desk` (row 87)

2. **CHAPTER-MAP row IDs**:
   - Row 87 (LEAGUE / teams desk) — 441-team global desk
   - Rows 27–56 (TEAM / NBA team front offices) — per-team org charts
   - Rows 88–114 (TEAMS / global leagues) — EuroLeague, WNBA, domestic leagues
   - Row 115 (TEAMS / ownership — NBA franchise sales & control)
   - Row 116 (TEAMS / ownership — EuroLeague club structures & sales)

3. **Derived paths**:
   - `data/derived/teams/teams.csv` — 441 teams (NBA 30, WNBA 12, EuroLeague 20, EuroLeague Women 22, plus 357 domestic league clubs across 20 leagues)
   - `data/derived/teams/ownership_events.csv` — NBA ownership timeline (158 events)
   - `data/derived/teams/ownership_timeline_by_team.md` — narrative NBA ownership history
   - `data/derived/teams/euroleague_current_ownership.csv` — EuroLeague ownership structures (20 clubs, 54 events)
   - `data/derived/teams/logos.csv` — logo URL manifest (sparse; fair-use = URL-only)
   - `data/derived/teams/README.md` — desk coverage and schema documentation
   - `data/derived/teams/LOGOS-README.md` — logo policy (no binaries; Wikimedia Commons SVG preferred)

4. **How to cite**:
   - **Team lookup**: Filter `teams.csv` by `team_id` (e.g., `nba_celtics_q131371`) or `abbr` (e.g., `BOS`)
   - **Ownership structure vocab**: `sole`, `majority`, `group`, `public`, `association` (from `ownership_structure` column)
   - **Former names**: Pipe-separated in `former_names` column (e.g., `New Jersey Americans|New York Nets|New Jersey Nets`)
   - **Colours**: `colours_primary_hex`, `colours_secondary_hex`, `colours_accent_hex` — prefer official team palette over logo-sampled hex
   - **Logos**: Check `logos.csv` for URL; if empty, see `LOGOS-GAPS.md`; **do not scrape** — cite fair-use URL from official source only
   - **Ownership events**: Filter `ownership_events.csv` by `team_id` for sale/control timeline; use `confidence` column (`HIGH`/`MEDIUM`/`LOW`)
   - **Wikidata**: Every team (except 44 documented gaps) has validated `wikidata_qid` for structured citation

### Status caveats

- **Teams desk**: ✅ **partial** (P0h complete 2026-09-19) — 441 teams present, 44 QID gaps documented in women's domestic leagues
  - 2 EuroLeague Women gaps
  - 7 Liga Femenina de Baloncesto (Spain) gaps
  - 2 Ligue Féminine de Basketball (France) gaps
  - 7 WCBA (China) gaps
  - 1 NBB (Brazil) gap
  - 9 LBF (Brazil women) gaps
  - 16 LFB (Argentina women) gaps
- **Colours enrichment**: Deferred — `colours_*_hex` columns present but unpopulated; schema locked
- **Logos**: Sparse — Wikimedia Commons SVG preferred; copyrighted logos = fair-use URL reference only (see `LOGOS-README.md`)
- **NBA org charts**: TOR, CLE, MIL relied on press releases vs official directories; check row-level `confidence` + `as_of` when citing (rows 27–56 in CHAPTER-MAP)
- **NBA ownership**: LAL (Kushner/Iger) and MIN (Stad) flagged; blanks intentional (see `ownership_methodology.md`)

### Open risks

- Thin women's league coverage acknowledged per hard requirements
- QID gaps stay empty (no invented identifiers)
- Logo files never committed (fair-use policy); URLs may break if external host changes
- Ownership `confidence` varies (HIGH for major sales, MEDIUM/LOW for minority stakes or unclear timelines)

---

## Journey C: Comparable Shelf (Books Desk)

**When to use**: Positioning manuscript, understanding market lanes, or citing companion reads.

### Steps

1. **Scrivener binder hint**: `Binder / comparable books desk` (CHAPTER-MAP row 117)

2. **CHAPTER-MAP row ID**: 
   - Row 117 (Binder / comparable books desk)

3. **Derived paths**:
   - `data/derived/books/comparable.csv` — 19 basketball books with Goodreads/Amazon data
   - `data/derived/books/comparable.md` — prose summaries of lane positioning
   - `data/derived/books/README.md` — desk methodology and source confidence

4. **How to cite**:
   - **Filter by lane**: `lane` column values are `narrative`, `analytics`, `how_to_watch`, `history`, `memoir`
   - **Use `why_comparable`**: Each row explains positioning vs your manuscript (e.g., "Simmons entertainment vs Taylor analysis")
   - **Goodreads ratings**: `goodreads_rating` (e.g., 4.20), `goodreads_ratings_count` (e.g., 38,724) — **high confidence**
   - **Amazon data**: `amazon_rating`, `amazon_reviews_count`, `price_band` often **GAP** (UK scrape blocked/stale)
   - **Price bands**: Where present, captured from UK retailers (Waterstones, LoveReading, publisher pages) as of `price_as_of` date
   - **Example citation**: "Bill Simmons' *The Book of Basketball* (4.20/38K Goodreads) is the fan-intellectual bible this desk is measured against"

### Status caveats

- **Goodreads data**: ✅ **ready** — ratings and counts are high confidence (live scrape 2026-09-19)
- **Amazon UK data**: ⚠️ **GAP** — most `amazon_rating`, `amazon_reviews_count`, and live prices are missing (scrape blocked or manual-only)
- **Price bands**: Mixed — some books have retailer-sourced price ranges (Waterstones, publisher pages); others show `GAP` or `varies`
- **ISBN-13**: Present for standard citation; `format_notes` clarifies hardcover/paperback/Kindle availability

### Open risks

- Amazon price/star data may remain **GAP** indefinitely (scraping reliability vs manual updates)
- Price bands are **indicative only** (retailer snippets, not live e-commerce data)
- Goodreads ratings change over time; `as_of` date is 2026-09-19
- Some older titles (e.g., *The Breaks of the Game* 1981, *The City Game* 1970) have reprint ISBNs; see `format_notes` for edition clarity
- Publisher/format availability (`varies`) means cite by ISBN-13 when precision matters

---

## Using This Guide

1. **Start in Scrivener**: Identify the section you're drafting (e.g., "CBA / salary cap")
2. **Check CHAPTER-MAP**: Look up the row number(s) that match your binder path
3. **Pick a journey**: Use the matching journey card above (A, B, or C)
4. **Follow the derived path**: Open the CSV, run the script, or check the README
5. **Cite with confidence**: Use the status caveats to flag what's ready vs what's still a gap
6. **Flag new journeys**: If your binder path isn't covered, open an issue for desk expansion

## Status Legend

| Status | Meaning |
|--------|---------|
| ✅ **ready** | Data committed; cite freely |
| ⚠️ **partial** | Core rows present; enrichment incomplete (check row-level notes) |
| ⚠️ **quotes_need_pdf** | Lookup/structure ready; verbatim quotes need local PDF |
| ⚠️ **GAP** | Known missing data (Amazon prices, ownership details, QIDs); documented gaps stay empty |

## Maintenance

This guide is **append-only** for journey cards. As new desks mature (e.g., broadcast ads, league income), add new journey sections below Journey C. Do not rewrite existing journeys; update status caveats in place if data changes.

**Last updated**: 2026-09-19  
**Desk status**: P0h complete (teams 441 rows, CBA 2023 structure committed, comparable books 19 rows)
