# MEDIA / FIN / STADIUM analysis — current gaps (2026-10-22)

## Overview
The three largest manuscript holes: MEDIA (7%), FIN (10%), STADIUM (20%). This file maps current sourced material and flagged gaps for nightshift requests.

---

## MEDIA (7% — essentially unwritten)

### Current sourced material
- **pr.nba.com official (2014-10-06):** ABC/ESPN and TNT/Turner nine-year agreements, 2016-17..2024-25 (from league-income-sources map, ds)
- **Zotero (Y5KFG5YX):** China sponsorship ~$500M/yr attributed; Tencent $1.5B digital deal; Weibo; Bytedance/TikTok references
- **analysis/media/nba_media_rights.md:** National TV partners documented; open questions on 2025-26 cycle, RSN consolidation, international streaming

### Open gaps (nightshift requests)
1. **2025-26 media cycle** — partner names, packages, term, streaming split (high priority)
2. **Local/regional TV revenue** — RSN impact on team revenue post-Bally consolidation (high priority)
3. **International streaming revenue** — Tencent, Weibo, others: dollar amounts, term, exclusivity (implied by existing refs, needs detail)

### Next: hoops_record (league-income-sources), paperful_ask (2025-26 cycle, RSN/local revenue, international deals)

---

## FIN (10% — mostly skeleton)

### Current sourced material
- **league-income-ingredients CSV (ds):** National media rights partners, payment structure (need to pull full CSV for detail)
- **analysis/fin/gate_licensing_sponsorship_notes.md:** 
  - Gate: ticketing share declined 29%→19% (2010-11..2019-20) [Y5KFG5YX]
  - Gate receipts = defined BRI component [78RYJHDP]
  - Licensing: Nike $1B/8yr [Y5KFG5YX]
  - Sponsorship: $1.46B (2020-21) [Y5KFG5YX], jersey patches >$150M [Y5KFG5YX]
  - No visiting-team gate split; league-wide revenue-sharing pool instead [AG49JIN4]
- **Zotero keys cited:** Y5KFG5YX, 78RYJHDP, AG49JIN4, 5ZFB9FVM

### Open gaps (nightshift requests)
1. **Salary cap CSV alignment** — urgent (deadline 2026-10-23): 2024-25 cap mislabeled in league-income-ingredients.csv; 2025-26 missing (high priority)
2. **Gate receipts definition & season-grain data** — CBA definition vs actual reporting (high priority)
3. **Sponsorship/licensing inventory** — jersey patch, naming rights, apparel contracts by category and team (medium priority)

### Next: hoops_record (league-income-ingredients CSV + source register), zotero_get (Y5KFG5YX, 78RYJHDP, AG49JIN4), paperful_ask (gate reconciliation, sponsorship inventory)

---

## STADIUM (20% — mostly skeleton)

### Current sourced material
- **analysis/fin_stadium/arena_subsidy_notes.md:**
  - Propheter [CGMDP7GN]: Pattern shift to public financing (2000s)
  - Groothuis et al. [ZQQVN8DQ]: 46 venues built/heavily renovated 1990–98; ~2/3 of $21.7B government-funded
  - Humphreys & Nowak [3EGEXSSS]: 64 new facilities 1991–2006; TIF increasingly popular
  - Irizarry [F3U6I5H7]: Case risk (Orlando Amway junk bonds, Harris County tax shortfall, abandoned venues)
- **Zotero keys:** CGMDP7GN, ZQQVN8DQ, 3EGEXSSS, F3U6I5H7

### Open gaps (nightshift requests)
1. **Post-2010 NBA arena cases** — with public subsidy %, lease terms, financing details (high priority)
2. **Lease, ownership, and control terms** — arena ownership structure, revenue splits, tax abatement duration (high priority)
3. **Construction cost trends** — new-build vs renovation, inflation, multi-purpose vs basketball-only (data, high priority)

### Next: paperful_ask (post-2010 arena cases with subsidy %, lease terms), zotero_get (ZQQVN8DQ, 3EGEXSSS, F3U6I5H7, CGMDP7GN)

---

## Cross-check & reconciliation

**hoops_status.md:** Currently shows only one-line paperful result (clobbered). Needs full chapter-by-chapter status after manuscript progress check.

**nightshift_requests.json:** 7 requests now active (merged 2025-26 media variants, added salary-cap urgent, clarified RSN/local revenue, removed unsourced items).

---

## Data ready to cite

- `analysis/fin/gate_licensing_sponsorship_notes.md` — cite Zotero keys for gate/licensing/sponsorship facts
- `analysis/fin_stadium/arena_subsidy_notes.md` — cite Zotero keys for pre-2010 subsidy patterns and case risks
- `analysis/media/nba_media_rights.md` — cite pr.nba.com and Zotero keys for national TV partners

## Data needed for first draft

- [ ] hoops_record: league-income-ingredients.csv (full rows for media, gate, licensing, sponsorship, salary cap)
- [ ] hoops_record: league-income-sources map (full source register)
- [ ] zotero_get: Y5KFG5YX, 78RYJHDP, AG49JIN4, 5ZFB9FVM (FIN keys)
- [ ] zotero_get: CGMDP7GN, ZQQVN8DQ, 3EGEXSSS, F3U6I5H7 (STADIUM keys)
- [ ] paperful_ask: National media rights 2025-26 cycle
- [ ] paperful_ask: Local/regional NBA TV revenue (RSN consolidation impact)
- [ ] paperful_ask: NBA arenas post-2010 (subsidy %, lease terms, financing)
- [ ] paperful_ask: Sponsorship/licensing contract terms and inventory
