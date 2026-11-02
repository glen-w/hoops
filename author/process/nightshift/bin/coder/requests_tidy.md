# requests_tidy — nightshift open requests

- **Source read:** `analysis/nightshift_requests.json`
  - Working copy read: `factory/sandbox/coder/analysis/nightshift_requests.json`
  - Read during factory night tick `2026-10-30` (free lane; run log `factory/runs/live-2026-10-30.log`; menu job `requests_tidy`)
- **Date:** 2026-10-30
- **Scope:** open (`status: open`) requests from the source file. This pass flags duplicates and uncomputable open requests. Flagged listing capped at 8 entries. No data was invented in this pass; figures cited come from files read here or from cited repo artifacts.

## Open requests in source (all open, all priority high)

| # | kind | title | priority | status | source_key |
|---|------|-------|----------|--------|-----------|
| 1 | paper | Little Caesars Arena EMMA official statement | high | open | emma:little-caesars-arena |
| 2 | paper | Amway Center bond rating documents | high | open | emma:amway-center |
| 3 | data | ENR Construction Cost Index annual 2000-2026 | high | open | enr:cci |
| 4 | paper | Post-2010 NBA arena lease reserve obligations | high | open | — |

## Flagged: uncomputable open requests

1. **ENR Construction Cost Index annual 2000-2026** — kind `data`, priority high, status open. **Uncomputable.**
   - Detail: "Annual ENR CCI values to deflate post-2010 NBA arena project costs; map to source_key enr:cci; blank until sourced."
   - Blocked on: annual ENR CCI series 2000-2026 not yet sourced; source_key `enr:cci` unmapped; no values. Until sourced, the deflated cost index for arena financing cannot be computed. Latest tick: "The ENR deflator is missing."

2. **Little Caesars Arena EMMA official statement** — kind `paper`, priority high, status open. **Uncomputable (extraction blocked).**
   - Detail: "Locate EMMA/MSRB official statement; extract bond amount, debt service coverage, public subsidy share; map to source_key emma:little-caesars-arena."
   - Blocked on: EMMA/MSRB official statement not located (`emma:little-caesars-arena` unmapped; latest tick: "Little Caesars EMMA is missing"). Bond amount / DSCR / public subsidy share cannot be computed until source is located.

3. **Amway Center bond rating documents** — kind `paper`, priority high, status open. **Uncomputable (extraction blocked).**
   - Detail: "Locate EMMA/MSRB rating and official statement; extract bond amount, DSCR, public subsidy share; map to source_key emma:amway-center."
   - Blocked on: EMMA/MSRB rating/official statement not located (`emma:amway-center` unmapped; latest tick: "Amway EMMA is missing"). Extraction blocked.

4. **Post-2010 NBA arena lease reserve obligations** — kind `paper`, priority high, status open. **Uncomputable (source blocked).**
   - Detail: "Paperful missed standard capital repair and lease reserve obligations in post-2010 NBA arena operating leases and official-statement reporting; seek lease agreements or official statements with reserve terms."
   - Blocked on: lease agreements / official statements with reserve terms not yet sourced (Paperful missed). Source retrieval blocked.

## Flagged: duplicate open requests

1. **Little Caesars Arena EMMA official statement** — kind `paper`, priority high, status open. **Duplicate / overlap.**
   - The figures this request asks to extract (bond amount, debt service coverage, public subsidy share) are already captured in `analysis/arena_financing_post2010.csv` (Little Caesars row: source_key `ASQSSF2Q`; public subsidy $324M, 37.5% of ~$862.9M total cost, via Detroit DDA tax-increment financing; HIGH confidence, Sroka 2024) and in the FIN/STADIUM grounded notes (`FIN_grounded_2026-10-23.md`, `STADIUM_grounded_2026-10-23.md`).
   - The open `emma:little-caesars-arena` seek therefore overlaps already-served financing data; source_key naming needs reconciliation (`emma:*` scheme vs established `ASQSSF2Q` mapping) before re-filing.

## Flagged summary

- Open requests in source: **4** (all open, all high priority).
- Flagged as **uncomputable**: **4**.
- Flagged as **duplicate / overlap**: **1** (Little Caesars Arena EMMA official statement).
- Distinct flagged open requests: **4** (cap applied: max 8).
