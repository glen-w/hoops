# Methodology — NBA franchise ownership & sales ledger
**Product:** Glen’s Hoops desk — writer-facing ownership ledger  
**Access date:** 2026-09-19  
**Output root:** `/workspace/hoops-nba-ownership-ledger-2026-09-19/`

## Purpose
Chronological ledger of how NBA ownership structure changed: sales, controlling/majority stakes, minority stakes, ownership-tied relocations/rebrands/expansions, and major reported prices — for writers, not as a substitute for legal/BOG records.

## Preferred sources (in order)
1. **Official team / NBA Communications releases** — closing statements, BOG approval notices (e.g. `pr.nba.com`, team `.nba.com` newsrooms).
2. **Reputable business / sports-business press** — Forbes, Sportico, The Athletic, Bloomberg, WSJ, ESPN business/ownership desks, AP.
3. **Structured secondary timelines** — Spotrac NBA Ownership (useful for franchise-path scaffolding; always re-check prices against #1/#2).
4. **Wikipedia** — **lead / navigation only**. Every price and control claim must be verified against #1–#3 before HIGH confidence. If only Wikipedia supports a figure, mark LOW/MEDIUM and note GAP.

## Column rules
| Field | Rule |
|-------|------|
| `event_date` | ISO `YYYY-MM-DD` when known; else `YYYY-MM` or `YYYY`. |
| `event_type` | Controlled vocab: `sale` \| `majority_stake` \| `minority_stake` \| `relocation` \| `rebrand` \| `expansion` \| `bankruptcy` \| `other`. |
| `buyer_structure` | `sole` \| `majority` \| `group` \| `public` \| `municipal` \| `unknown` (align with teams desk). |
| `price_usd_reported` | Integer USD string when a widely reported figure exists. **Never invent.** Leave blank + explain in `price_notes` / `notes` with `GAP`. |
| `confidence` | `HIGH` = official or multi-outlet corroboration of closed deal; `MEDIUM` = strong press but package/stake ambiguity or pending; `LOW` = roundup-only or weakly sourced. |
| `source_url` / `source_title` | Required on every row. Prefer the primary cite; secondary OK if primary paywalled — say so in notes. |

## What counts as an event
- **Include:** Change of controlling/majority ownership; significant reported minority stakes; expansion awards where ownership is the story; relocations tied to ownership; rebrands that reallocate franchise history (e.g. CHA/NOP 2014); league stewardship; clear family succession that changes named controlling owner.
- **Exclude / deprioritize:** Routine governor title swaps without equity change; rumor-only bids; valuation rankings that are not transactions.
- **Pending deals:** Enter as events with `PENDING` in `price_notes`/`notes` and do **not** describe them as current control in the timeline until BOG approval + close.

## Price hygiene
- Distinguish **franchise valuation** vs **cash for a stake** vs **multi-asset package** (arena, sister clubs, real estate).
- ABA–NBA **entry charges** (~$3.2M) are `other`, not market sales.
- Expansion **fees** are not secondary-market sale prices; label clearly.

## Coverage priorities (this build)
1. Well-documented modern sales **2000–2026**.
2. **Pre-2000 / 20th-century thicken:** founding/expansion purchases, famous early sales, multi-city franchise paths (Hawks, Kings, Warriors, Clippers, Lakers, Nets ABA, Sonics, Sixers/Nationals, Bullets/Wizards, etc.).
3. Famous historical + modern anchors (Clippers Sterling→Ballmer; Lakers Cooke→Buss→Walter; Suns Colangelo→Sarver→Ishbia; Mavs Carter→Perot→Cuban→Adelson/Dumont; Jazz Miller→Smith; Blazers Weinberg→Allen→Dundon; etc.).
4. Expansion / relocation ownership beats (CHA return, Sonics→OKC, Vancouver→Memphis, Buffalo→SD→LA, Rochester→SAC path).
5. Stretch narrative (if any) stays in `local/` — not public.

## Final thicken (2026-09-19)
Wikipedia-led MEDIUM rows upgraded to Star-Gazette / Remember the ABA / SFGate / Journal Sentinel / NYT / Hawks.com / LA Times / NBA Communications / SBJ / OregonLive / UPI where findable. POR Weinberg controlling stake corrected from 1972→1976; added Sarkowsky←Schmertz 1972. BKN-2004 price filled at $300M (NYT). NYK-1997 package path updated to Cablevision/ITT contemporaneous ~$650M headline (team-only still GAP). **Still do not invent.**

## Known limitations (gaps)
- Pre-1980 purchase prices often sparse or packaged — many blanks by design (e.g. Turner Hawks cash, Weinberg Blazers consolidation, Fitzgerald Bucks consolidation, Secaucus Seven / Ratner Nets cash).
- Corporate parents (MSG, MLSE, Monumental, KSE) obscure team-only economics (TOR Rogers/MLSE C$ package; NYK inside MSG).
- As of 2026-09-19: **LAL Kushner/Iger** and **MIN Stad** deals announced but not treated as closed control.
- PE minority rows often have **valuation + stake %** but blank cash when Sportico/team releases omit the check size (Arctos Warriors/Jazz; Dyal Hawks/Suns).
- BAA 1946 charter fee entered as **$10,000** (American Heritage) — operating contribution, not a modern expansion market fee.
- CHI Reinsdorf row stores **$9.2M cash for ~56.8%** (not the ~$16M implied full-franchise figure).

## Refresh cadence
Re-pull after any BOG meeting that approves a control change; bump folder date or append new `event_id`s without rewriting history.
