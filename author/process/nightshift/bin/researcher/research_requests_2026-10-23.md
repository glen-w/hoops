# Research Requests for MEDIA, STADIUM, FIN Holes — 2026-10-23

## Summary

Three chapters have major gaps requiring literature queries via `paperful_ask` (hoops RAG). MEDIA is 7% complete (film/TV only); STADIUM is 20% complete (no grounded case studies); FIN needs chapter clarification.

## MEDIA Queries (3 requests)

### 1. Basketball documentary films and cultural impact (film/TV section)
Query: "basketball documentary films cultural impact Last Dance Hoop Dreams cultural analysis race class identity memoirs production history"

**What we have:** Film/TV (282 w) mentions Last Dance, Hoop Dreams, Magic & Bird, The Carter Effect. Needs: canonical films pre-2010, production credits verified, cultural role and audience impact, anime/international transmedia.

**For MEDIA.md:** Film and Documentary section (currently ungrounded).

---

### 2. Basketball journalism, sports writing, and beat reporting history
Query: "basketball journalism sports writing David Halberstam Bill Bradley John Feinstein sports reporters beat reporters basketball newspaper coverage traditional media"

**What we have:** Scaffold mentions Bill Bradley memoirs, Halberstam's *Playing for Keeps*, Feinstein's journalism. Needs: history of NBA newspaper coverage (1946–2000), journalism transitions, beat reporter role and decline, shift to digital outlets (The Athletic, Substack).

**For MEDIA.md:** Traditional Journalism section (currently ungrounded).

---

### 3. Insider transaction reporting and operational impact
Query: "NBA insider reporting Wojnarowski transaction reporting impact free agency operations front office relations organizational effects media narrative"

**What we have:** Scaffold mentions "Wojbomb" phenomenon. Needs: empirical analysis of whether insider reporting affects player-front office relations, fan behavior, league operations, or free-agency dynamics. Known literature gap — this may require nightshift data request if no academic study exists.

**For MEDIA.md:** Journalism and Narrative section (operational impact gap explicitly identified).

---

## STADIUM Queries (4 requests)

### 4. Home-court advantage, crowd effects, and 2020 bubble experiment
Query: "home-court advantage NBA crowd effects 2020-21 bubble playoff home advantage win percentage referee bias crowd noise"

**What we have:** Scaffold cites Monash 2021 (58.65% with crowds, 50.6% without) and AEI working paper (2.13-pt and 0.39-pt effects). Need full source citations. Bubble data: home teams' win % dropped to ~50% without crowds.

**For STADIUM.md:** Home-Court Advantage section (Monash/AEI sources need verification; bubble analysis needs expansion).

---

### 5. Warriors relocation (Oakland to San Francisco) and Chase Center design
Query: "Warriors relocation Oakland San Francisco 2019 Chase Center arena design home-court advantage arena finance construction cost"

**What we have:** Scaffold mentions Warriors/Oakland and Chase Center but unverified. Need: Oakland-to-SF move details, Chase Center design features, arena financing (public vs. private), impact on home-court advantage, fan experience changes.

**For STADIUM.md:** Arena Design and Infrastructure section (real case study).

---

### 6. Clippers Intuit Dome and arena design innovation
Query: "LA Clippers Intuit Dome Inglewood 2024 arena design features financing public private partnership fan experience wall design"

**What we have:** Scaffold mentions "Clippers wall" unverified. Need: Intuit Dome design features, financing model breakdown, fan-experience innovations, home-court advantage implications, cost and stakeholder breakdown.

**For STADIUM.md:** Arena Design and Infrastructure section (real case study).

---

### 7. NBA international games: London, Mexico City, Toronto scheduling and competitive balance
Query: "NBA London games Mexico City Toronto international venues home-court advantage travel fatigue competitive balance scheduling"

**What we have:** Scaffold mentions London since 2011, Mexico City, Toronto but lacks specifics. Need: detailed London games data (home-court dynamics, travel impact), Mexico City/Toronto venue economics and player fatigue effects, international attendance revenue, competitive balance implications.

**For STADIUM.md:** International and Non-Contiguous Venues section.

---

## FIN Chapter Clarification

**PENDING DECISION:** Current FIN.md has finance/revenue content ([VERIFY] flags throughout). But hoops_status.md indicates FIN is a closing chapter with 18 sections (only 2 written: Future, first shot). 

**Action:** Need to resolve:
1. Is FIN the closing/finale chapter (18 sections)? If so, what are those 18 sections?
2. Does finance/revenue content belong in LEAGUE chapter instead?
3. If FIN is the finale, what is its purpose and structure?

**Until resolved:** Do not build hr queries for FIN. Mark as blocked in nightshift_requests.json.

---

## Execution Plan

1. Run paperful_ask queries 1–7 to gather literature.
2. Ground MEDIA.md (film/TV, journalism, books, insider reporting) with returned citations.
3. Ground STADIUM.md (home-court, Warriors/Chase, Clippers/Intuit, international games) with returned citations.
4. Resolve FIN chapter structure; add to nightshift_requests if external research needed.
5. Update nightshift_requests.json to mark these queries as pending (not yet filed).
