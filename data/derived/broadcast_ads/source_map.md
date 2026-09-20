# Broadcast / ads — source map (writer-facing)

**Pack:** `hoops-broadcast-ads-2026-09-19`  
**Access / as_of:** 2026-09-19 (Europe/Paris)  
**Upstream:** `hoops-thicken-2026-09-19/broadcast-ads-sources.md`, `hoops-thicken-efficiency-income-2026-09-19/03-broadcast-ads-vs-rights-fees.md`, `hoops-league-income-2026-09-19/`

## Prose rule (do not blur)

| Stream | Who pays whom | What it is |
|--------|---------------|------------|
| **Media rights fees** | Networks/streamers → **NBA** (then BRI / distributions) | Contract price for game windows |
| **Ad sales / bookings** | Advertisers → **networks/streamers** (and sometimes local RSN / team inventory sellers) | Monetization of airtime / impressions — **not** the rights fee |
| **Sponsorship rights fees** | Brands → **league / team** | Patches, naming rights, in-arena, digital, hospitality, entitlement of “moments” |

Never write “the TV deal is a $X ad market.” Say rights fee, ad sales, or sponsorship rights explicitly.

---

## A. National TV / streaming media rights

| What exists publicly | Label | Notes |
|----------------------|-------|-------|
| Partners, term, package structure | **OFFICIAL** | [NBA.com media agreements 2024](https://www.nba.com/news/nba-media-agreements-2024) (Disney/ABC-ESPN, NBCU/Peacock, Amazon Prime Video; 2025-26–2035-36). Prior cycle: [NBA Communications Disney/Turner 2014](https://pr.nba.com/nba-partnerships-walt-disney-company-turner-broadcasting-system/) (2016-17–2024-25). |
| Contract dollar totals / AAV | **SECONDARY** only | League does **not** publish package dollars in those releases. Journalism consensus in league-income pack: ~$24B / ~$2.6B·yr (2016–25, SI); ~$76B–$77B / ~$6.9B·yr framing (2025–36, Sportico/CNBC). Partner splits (Disney / NBCU / Amazon annual) are CNBC “people familiar,” not official. |
| Per-team national TV payout | **SECONDARY** | Sportico: $103M (2024-25) → $143M (2025-26). Not an NBA audited receipt line. |

**Paywalled / unknowable:** full rate cards inside rights contracts; escalator schedules year-by-year; exact BRI recognition timing vs contract AAV; any WNBA bundling inside some secondary “~$76–77B” tallies (flag when using).

---

## B. Local RSN / local media

| What exists publicly | Label | Notes |
|----------------------|-------|-------|
| Narrative of RSN distress / Diamond→Main Street cuts | **SECONDARY** | Sportico team-economics pieces (local media ~10% of 2024-25 leaguewide revenue in reporting; individual team anecdotes). |
| Occasional team-level fees | **SECONDARY / UNCONFIRMED** for leaguewide table | Examples cited in trade press (e.g. Lakers–Spectrum, Knicks–MSG haircut, Celtics local TV including RSN equity) — team-specific, methodology often “someone familiar,” not a consistent series. |
| Leaguewide local-media rollup | **GAP** | Explicit empty row in `hoops-league-income-2026-09-19/league_income_ingredients.csv`. |

**Paywalled / unknowable:** most team RSN contracts; make-goods; streaming-substitute economics; a clean 30-team fee table with one definition.

---

## C. In-game / courtside / LED / “Sponsored Moments” inventory

**Taxonomy note:** “Sponsored Moments” in this binder is a **writer label**, not a single NBA.com SKU with a published rate card. It covers (1) entitlement/title partners of named game moments (tip-off, halftime, awards, Cup, etc. — see NBA Communications partnership releases) and (2) emerging **augmented / data-triggered in-broadcast** inventory (e.g. Genius Sports + local RSN platforms). Do not invent a leaguewide “Sponsored Moments” revenue line.

| Inventory type | Public enough to cite | Usually unknowable |
|----------------|----------------------|--------------------|
| Courtside / apron / floor / stanchion LED | Existence of assets; team announcements of new surfaces (e.g. SBJ on Fiserv Forum stair LED); brand-exposure white papers that **estimate media value** | Team rate cards; sold vs unsold units; national blackout rules for some LED during ABC/ESPN/Amazon/Peacock windows (team-announced, not a league ledger) |
| League partner entitlements (“moments”) | Official PR naming the asset (Amex tip-off / halftime; Kia awards; Emirates Cup / patches; etc.) | Fee schedules; exclusivity term sheets |
| Augmented / AI in-broadcast ads | Company press (platform footprint, game counts) | Inventory prices; fill rates |
| National commercial spot inventory | Trade press + measurement vendors (iSpot, Guideline via Sportico) for **estimated spend / airings / impressions** | Network sellable-unit books; makegoods; net vs gross after agency |

### Source register (ads / sponsorship side)

| ID | Source | Label | Use |
|----|--------|-------|-----|
| BA-01 | [IEG NBA Sponsorship Snapshot 2024-25 PDF](https://sponsorship.com/wp-content/uploads/2025/07/IEG_NBA_Sponsorship_Snapshot_2024-25_Season.pdf) | SECONDARY | Rights-fee / deal-count snapshot; **excludes** commercial media buys |
| BA-02 | [SponsorUnited NBA Sponsorship Intelligence Report 2025-26](https://www.sponsorunited.com/insights/nba-sponsorship-intelligence-report-2025-26) | SECONDARY | Public summary; deeper DB may be gated |
| BA-03 | [MediaPost / iSpot: regular-season ad spend ~$760M (2025-26)](https://www.mediapost.com/publications/article/414480/nba-2025-26-video-ad-revenue-hits-760m-viewing-u.html?edition=142360) | SECONDARY | Vendor estimate of national TV/streaming **ad** revenue — not NBA filing |
| BA-04 | [Sportico: national ad sales ~$2.1B first season of new rights](https://www.sportico.com/business/media/2026/nba-ad-sales-media-rights-deal-tv-1234942133/) | SECONDARY | Guideline-based; paywall possible; preserve season definition |
| BA-05 | [NBA media agreements 2024](https://www.nba.com/news/nba-media-agreements-2024) | OFFICIAL | Partners / windows only — **no** ad inventory dollars |
| BA-06 | [NBA Partners hub](https://www.nba.com/partners) | OFFICIAL | Named partners, not a price list |
| BA-07 | [iSpot.tv NBA brand page](https://www.ispot.tv/brands/0m/nba) | SECONDARY | Lead for airings / creatives |
| BA-08 | Team / league partnership PR (Amex, Kia, Emirates, etc. on pr.nba.com) | OFFICIAL for **existence** of asset | Amount = UNCONFIRMED unless disclosed |
| BA-09 | Genius Sports / NBCSRN augmented advertising releases (2026) | SECONDARY | Platform scope; not a rate card |
| BA-10 | Agency marketing pages quoting LED “$250k–$3M/season” ranges | UNCONFIRMED | Do **not** treat as confirmed public fact without primary deal disclosure |

---

## D. What to leave blank in any derived table

- Network/streamer sellable-unit counts, unsold inventory, makegoods  
- Complete team-by-team sponsor fee schedules  
- League-audited split of broadcast ad revenue vs sponsorship vs activation vs endorsement  
- Leaguewide RSN fee series with one definition  
- Any figure computed by averaging competing secondary tallies (e.g. $76B vs $77B)

**Status rule:** unpriced official announcement → partnership existence can be OFFICIAL; amount stays blank / UNCONFIRMED.

