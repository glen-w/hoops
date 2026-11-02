# Nightshift log for 2026-10-29 (night 2026-10-28-watch-r1, *Hoops*)

Run by Grok Bot on the box, finished 29 Oct 2026 around 11:23 CET (Paris). There were four requests, all kind=data. requests.json was not edited. Each output builds on the 2026-10-28 outputs and points back to them.

| id | title | status | outputs |
|---|---|---|---|
| 2026-10-28-watch-r1-researcher-01 | NBA backboard specs 1946–1952 | done (the BAA/NBA rulebook text itself is a GAP) | 2026-10-29_researcher-01_backboard-specs-1946-1952.md/.csv/.parquet |
| 2026-10-28-watch-r1-researcher-02 | AAC 2001: SEC filings and capital structure | done (EMMA documents need a manual click-through) | 2026-10-29_researcher-02_aac-sec-capital-structure.md/.csv/.parquet |
| 2026-10-28-watch-r1-researcher-03 | NBA arenas 1990–2010 | partly done (public share for the 1990s arenas is a GAP) | 2026-10-29_researcher-03_nba-arenas-1990-2010.md/.csv/.parquet |
| 2026-10-28-watch-r1-coder-01 | D/E, leverage and interest coverage 2000–2026 | done (pre-2009 covers EPR only; the rest is a GAP) | 2026-10-29_coder-01_arena-operator-leverage-coverage-2000-2026.md/.csv/.parquet |

## Key findings
- **R1.** The BAA made glass backboards mandatory on 10 May 1948 (APBR minutes). The NCAA authorised transparent boards in 1946-47 and the fan-shaped board in 1940-41. Under the 1933 rules the board was 6×4 ft (that text is the women's rules; the men's spec is assumed to be the same), set 4 ft inside the end line from 1939-40. Connors shattered the glass at Boston Arena on 5 Nov 1946. The file also lists 16 patents for 1929–55.
- **R2.**
  - Belo's FY1999 10-K shows it bought 12.38% of the Mavericks LP and 6.19% (non-voting) of the arena entity for about $24.5M. It sold both on 30 Jan 2002 for $27M.
  - AMR's filings never disclose the naming-rights deal; only "American Airlines Center Foundation, Inc." appears, in Exhibit 21.
  - No EDGAR filer exists for Center Operating Co. or for any Hicks/Cuban entity.
  - The bonds' EMMA CUSIP-6 is 235375. Series 1998A was paid off in Feb 2010, and Series 1998B was due to be paid off by end-2011.
- **R3.** 30 arenas, with Wikipedia infobox figures pinned to oldid revisions (MEDIUM, summary-only). Public share comes from yesterday's capex rows (4 sourced).
- **C1.** 98 entity-years across MSG-family, LYV, EPR, VICI and Braves. The MSG entities and LYV have had negative equity in recent years, so use debt/assets for them. For the REITs, coverage is computed as net income plus interest over interest.

## Zotero
Added via the Web API (user 11334554); the key worked (HTTP 200). Items were deduped by title search first. Every new item is tagged `nightshift-2026-10-29`. No existing items or notes were edited, nothing was deleted, and "my pubs" was not touched.

**Created (6)**
- APDP4I6A: NCAA, Men's Basketball Rules History. Filed in rules 4ZHZ2Y3I and ⭐history D4A783AU.
- 7AXE5E78: APBR, BAA League Minutes 1946-49. Filed in history, rules and league design HPSLPRXB.
- 2HFFHXK8: Schwartz, "Rifleman is first to shatter an NBA backboard" (ESPN Classic). Filed in history and court 4S4CFP4M.
- NIVDI94J: Morey, US2553105A (transparent backboard; filed 1947, granted 1951). Filed in court and history.
- Z8VXESTS: Belo Corp. 10-K FY1999. Filed in teams/ownership J642VFUB and stadiums 3IGASUT5.
- TW273TR9: City of Dallas, 1998 Sports Arena Project Bonds Optional Redemption (memo, 10 Dec 2010). Filed in stadiums and economics J3XVUX2F.

**Reused (cited only, not edited):** 82ADZHU4 (Long 2012), 3C5SQUCK, 3Z9ZDBZT, VSSARAK9, XMZTSJJQ, CV844ZN9, RQZSN7V2, 5VRHQ89B.

## Needs Glen
- R1: an actual BAA/NBA Official Guide covering 1946–52. Not found online, so the rule text for that period is a GAP.
- R2: if wanted, an EMMA click-through for CUSIP-6 235375 (redemption notices from 2009–11).
- R3: public share for the 1990s arenas from Long 2012 (82ADZHU4), plus renovation costs for KeyArena 1995 and Oakland 1997.
- C1: pre-2009 figures for Cablevision/MSG, SFX/Live Nation predecessors, Ascent Entertainment and the Celtics LP were not pulled.
