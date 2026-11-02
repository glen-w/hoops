# NBA arenas built or renovated 1990–2010: per-arena table

Request: 2026-10-28-watch-r1-researcher-03 · Night 2026-10-29 · Retrieved 2026-10-29
Data: `2026-10-29_researcher-03_nba-arenas-1990-2010.csv` / `.parquet` (30 rows)
**Reuses** `2026-10-28/out/2026-10-28_coder-01_nba-arena-capex-2000-2026.csv`. Seven rows overlap: AAC, SBC Center, Toyota Center, FedExForum, Charlotte, OKC 2010, Amway. Public-share figures and their sources are carried over from it unchanged. For operating costs, see the 2026-10-25 researcher-07 note.

## Scope
- Every arena that hosted an NBA team and opened, or had a major rebuild, between 1990 and 2010. That gives 26 new builds and 4 renovations (MSG 1991, KeyArena 1995, Oakland 1997, plus the OKC 2010 improvements noted on the Ford Center row).
- Shared or temporary NBA homes are included and flagged: Alamodome, Pyramid, Prudential Center.
- Arenas that opened in 1988–89 (ARCO, Bradley Center, Miami Arena, Orlando Arena, Charlotte Coliseum) are excluded.

## Sourcing
- **Opened year, architect, capacity, nominal cost, owner and contractor** come from each arena's Wikipedia infobox. Each one is pinned to a revision id (`oldid` in `cost_source`), so the exact text can be re-checked.
  - Confidence is **MEDIUM [summary-only]**. Infobox costs are often the headline construction figure; they rarely include land or infrastructure and mix inflation bases.
  - Use them for orientation, then confirm against primary sources (city or authority documents, bond OS) before quoting.
- **Public share** is filled only where yesterday's dataset had a source: AAC 29.8%, SBC 78.8%, Toyota 77.4%, FedExForum 100%. Every other row is marked **GAP**. No figure was invented.
- Canadian arenas (GM Place CAD 160M, Air Canada Centre CAD 265M) have their costs left in CAD. The USD column is blank for them.
- **Materials and engineering are mostly a GAP.** Infoboxes give contractors but not structural systems. Notes marked [unverified] are general knowledge that still needs a source:
  - Target Center was built privately and bought by the city in 1995.
  - United Center and Staples Center were mostly privately financed.
  - Gund Arena was funded by the Gateway "sin tax".
  - Rose Garden was built by Paul Allen's company.

## Patterns (descriptive, n=30, nominal USD)
- **Ellerbe Becket designed 10 of the 30**, nearly all in the 1992–2005 wave. HOK Sport/Populous designed 7.
- **Nominal costs rose from about $90–175M** (1990–94: Target, Delta, America West, Gund, United Center) **to $375–480M** (Staples, Prudential, AAC, Amway).
- **The public share is high** in the four sourced 2001–04 Sun Belt deals (30–100%), but there are too few sourced rows to generalise.

## Gaps and next steps for Glen
- Public share for the 1990s arenas. The best single next source is Judith Grant Long, *Public/Private Partnerships for Major League Sports Facilities* (Routledge 2012). It is already in Zotero (82ADZHU4, under stadiums and economics) and is the best single next source, since it reports public costs facility by facility. It was not opened tonight.
- Renovation costs for KeyArena 1995 and Oakland 1997.
- Pyramid opening date, capacities for Target Center, Rose Garden and Oakland, and materials.
