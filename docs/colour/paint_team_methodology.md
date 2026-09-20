# Methodology — Paint language × NBA team colours (Pack B)

**Pack date:** 2026-09-20 (Europe/Paris)  
**Access date for cited fetches:** 2026-09-20

## Honesty locks

- **No invented hexes** for paint or teams.
- **hoops `teams.csv` colour columns are empty (0/30)** — confirmed from `https://raw.githubusercontent.com/glen-w/hoops/main/data/derived/teams/teams.csv` on access date. Those columns are **not** filled by this pack.
- Team hexes live only in `data/derived/teams/nba_team_colours_cited.csv`, cited from Wikipedia Module:Sports color/basketball, confidence **MEDIUM** (community template module — **not** official NBA brand-guide PDFs).
- Paint hexes cited from public datasets with provenance URLs on every row.
- ToS: used published GitHub/gist mirrors and Wikipedia raw module; no login-walled scrapes.

## Paint corpora (seed)

### Dulux — `data/derived/paint/dulux_colours.csv`

| Item | Value |
|------|-------|
| Upstream | [shanmoorthy/dulux-paint-colour-data](https://github.com/shanmoorthy/dulux-paint-colour-data) |
| Origin | RGB (+ LRV, product URL) scraped from public Dulux Australia colour pages |
| Full corpus | 5032 colours in `data/raw/dulux_shan.json` |
| Seed size | **442** hue-bucket stratified subsample |
| Row cite | `source_url` → `https://www.dulux.com.au/colour/…` plus dataset URL |

**Expansion path:** ingest full 5032 rows; optional Dulux NZ `__NEXT_DATA__` collections (public pages) as a second brand/line.

### Pantone — `data/derived/paint/pantone_colours.csv`

| Item | Value |
|------|-------|
| Named FHI | [Margaret2/pantone-colors](https://github.com/Margaret2/pantone-colors) CSS (2310 named Fashion/Home/Interiors; README: hexes from Pantone site, names © Pantone) — **390** stratified into seed |
| Coated codes | [bconglet/Pantoner](https://github.com/bconglet/Pantoner) `csv/pantone-coated.csv` (MIT, unofficial hex approximations) — **150** sampled → seed total **540** |
| Confidence | Named FHI MEDIUM–HIGH (public hex mirror); coated codes **MEDIUM** (community approximation, not Pantone LLC digital API) |

**Expansion path:** remaining named + coated/uncoated sets from Pantoner; never invent chips.

## Team colours

| Source | File | Confidence |
|--------|------|------------|
| enwiki `Module:Sports color/basketball` raw | `nba_team_colours_cited.csv` | MEDIUM |
| hoops `teams.csv` colour columns | empty | GAP 0/30 (documented in `teams_csv_colour_status.md`) |

Module field order interpreted as primary / secondary / accent / quaternary. Secondary is often `#FFFFFF` (template foreground) — matches retained but flagged as weakly meaningful in notes.

**Not claimed as official:** TeamColorsGuide / sportsblogs blocked or thin in this environment; TruColor / brand PDFs not ingested this pass (optional upgrade → raise confidence to HIGH where official guides exist).

## Distance formula (crosswalk)

File: `data/derived/paint/team_colour_paint_matches.csv`

1. Convert team hex and paint hex from sRGB 8-bit → linear sRGB → CIE XYZ (D65) → CIE L*a*b*.  
2. **Primary metric:** CIE76 ΔE\*  
   \(\Delta E_{76} = \sqrt{(L_1-L_2)^2 + (a_1-a_2)^2 + (b_1-b_2)^2}\)  
3. Also report **Euclidean RGB** distance in 0–255 space for transparency.  
4. For each team role (primary, secondary, accent), keep nearest Dulux and nearest Pantone in the **seed** corpora (`match_rank_within_brand=1`).

CIE76 is sufficient for seed nearest-neighbour storytelling; CIEDE2000 is an expansion-path upgrade.

## Coverage summary

| Artifact | Rows | Notes |
|----------|------|-------|
| dulux_colours.csv | 442 | of 5032 full |
| pantone_colours.csv | 540 | 390 named + 150 coated |
| nba_team_colours_cited.csv | 30 | all current NBA |
| team_colour_paint_matches.csv | 180 | 30 × 3 roles × 2 brands |
| teams.csv primary hex | 0/30 | GAP (expected) |
