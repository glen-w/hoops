# MEDIA / FIN / STADIUM Gap Assessment — 2026-10-22-pm

## Summary

Grokbot batch `2026-10-22-pm` completed; paperful_ask results confirm major library gaps. Analysis readiness:

- **GAME TIME** data ready (ft_pressure_cascade complete; no workload × pressure interaction found)
- **PLAYERS** literature briefs ready (reinvestment, automaticity, fatigue, kinematics)
- **MEDIA** blocked: 2025-26 cycle not in library
- **FIN** partially blocked: post-2010 arena subsidy cases absent; sponsorship needs retry
- **STADIUM** blocked: post-2010 case data absent from library

## Findings from hr_out Batch (2026-10-22)

### MEDIA 2025-26 Cycle
**Status:** Not in library (too recent)  
**Paperful result:** ABC, Amazon Prime, current RSN consolidation not documented in available sources. Library contains only 2016-24 deals (ABC/ESPN TNT via pr.nba.com 2014-10-06 announcement).  
**Next:** Daytime search required (pr.nba.com announcements, ESPN official docs, 2024-25 proxy season data).

### Arenas Post-2010
**Status:** Not in library (only planning-stage mentions)  
**Paperful result:** Chicago (proposed), Milwaukee (early planning) only. Confirmed NBA arena builds 2010+ (Barclays 2012, Chase 2019, Kings Arena 2016, etc.) not documented with subsidy %, lease, financing detail.  
**Next:** Daytime research needed (municipal bond records, team/city press releases, sports law databases).

### Sponsorship Inventory
**Status:** Timeout (180s) — retry pending  
**Current:** Gate/licensing notes cite partial values (2020-21 US$1.46B total; jersey patches >US$150M). Detail (category breakdown, duration, team variation, 2022-26 trajectory) incomplete.  
**Next:** Retry paperful_ask on sponsorship structure and values.

## Zotero Context Pending

11 keys cited in FIN/STADIUM notes require full context (author, title, DOI, publication date):
- **FIN:** Y5KFG5YX, 78RYJHDP, AG49JIN4, 5ZFB9FVM, JZIGK6FA
- **STADIUM:** CGMDP7GN, ZQQVN8DQ, 3EGEXSSS, F3U6I5H7

These are in library (found via paperful); Zotero pull will validate details and surface any missing refs.

## Action Plan (Next Tick)

1. **Retry sponsorship paperful_ask** (transient timeout)
2. **Pull 11 Zotero keys** for FIN/STADIUM context enrichment
3. **File nightshift_requests** (done; updated with "library_gap_confirmed" status)
4. **Prepare GAME TIME + PLAYERS drafts** once Zotero context ready

## Data Ready for Manuscript

- `analysis/game_time/ft_pressure_cascade.md` — full analysis note, ready to cite
- `analysis/game_time/ft_pressure_workload_summary.csv` — 519,640 FT attempts, context × workload splits
- `analysis/game_time/ft_models.csv` — 6 logit models, p-values, average marginal effects
- `PLAYERS/reinvestment`, `automaticity`, `fatigue`, `kinematics` — literature briefs grounded (5 docs)
- `PLAYERS/player_season_automaticity_proxies.csv` — 2015-24 choke gaps, baseline stability, workload
