# Methodology: Home-court pilgrimage field guide

**Pack:** Creative overnight (2026-09-20)  
**Source constraint:** Cite-only from `data/derived/home_court_2024_playoffs.csv` + methodology  
**Confidence rule:** HIGH for Basketball-Reference recount; MEDIUM for regular-season wire service; GAP for unknowable

---

## Source hierarchy

1. **PRIMARY SURFACE (SECONDARY label):** Basketball-Reference 2024 NBA Playoffs schedule/results page  
   URL: https://www.basketball-reference.com/playoffs/NBA_2024.html  
   Label: SECONDARY (stats site; box-score-backed but not official NBA data)  
   Access: 2026-09-19

2. **SUPPORTING CONTEXT (SECONDARY):** ESPN Insider (Kevin Pelton, 2024-04-25)  
   URL: https://www.espn.co.uk/nba/insider/story/_/id/40018981/2024-nba-playoffs-real-not-siakam-brunson-scoring  
   What it supports: First-round Game 1s 8–0 home sweep; ~58% home win rate in recent Round 1 arena playoffs

3. **REGULAR-SEASON COMPARISON (SECONDARY):** Fox Sports / AP (updated 2024-04-14)  
   URL: https://www.foxsports.com/articles/nba/inside-the-nba-numbers-lots-of-comebacks-no-homecourt-edge-3s-went-up-scoring-went-down  
   What it supports: 2023–24 regular season 668–562 home record (.5431); "worst home-court mark in league history"  
   Confidence: MEDIUM (wire journalism, not NBA Communications release)

---

## Counting rules

### Home team definition
- In Basketball-Reference game lines formatted as `Away SCORE @ Home SCORE`, the team after `@` is the home team
- No special cases for neutral-site games (none in 2024 playoffs)

### Win/loss determination
- Winner = team with higher final score
- No need to track overtime (W/L binary sufficient for aggregate)

### Series and game scope
- **Series count:** 15 (Finals: 1, Conference Finals: 2, Conference Semifinals: 4, First Round: 8)
- **Game count:** 82 total across all series
- Independent recount performed 2026-09-19 on Basketball-Reference series tables

### Derived percentages
- Always shown as ratio of cited counts
- Example: 48/82 = 0.585365… reported as 0.5854 or ~58.5% in prose
- Never fabricated from partial data

---

## What we did NOT have (intentional gaps)

### Venue-by-venue breakdowns
Basketball-Reference provides series-level results (team matchups) but does not publish a per-arena home record table. We cannot state:
- Which specific arenas had the highest home win rates
- Attendance figures by game
- Crowd noise measurements
- Building-specific environmental factors

We inferred **ritual typology** (fortress / contested / overturned) from the aggregate 58.5% figure, not from per-venue tallies.

### Point margins and pace
Out of scope for this guide. The pilgrimage framework focuses on **win/loss outcomes** and **place** (home vs away), not scoring dynamics.

### Player or coaching variables
We treat the arena as the primary unit of analysis. Individual performance, coaching adjustments, and roster health are bracketed.

---

## Ritual geography framework: Justification

### Why "pilgrimage"?
The playoff series structure creates a **bounded itinerary**: teams travel between exactly two cities (home and away) for 4–7 games. Each arena becomes a **station** in a ritual sequence. The home team's advantage is not merely logistical (sleep, travel fatigue) but also **social** (crowd energy, familiarity) and **symbolic** (defending one's ground).

### Why "sacred" vs "profane"?
The regular season's 54.3% home win rate (historically low) vs the playoffs' 58.5% suggests a **qualitative shift** when the stakes rise. We borrow Durkheim's sacred/profane binary:
- **Profane time:** Regular season's 82 games per team, diluted stakes, sometimes sparse crowds
- **Sacred time:** Playoffs' do-or-die intensity, packed arenas, heightened ritual function

This is not a literal religious claim but an **analytical frame** for understanding why home court matters *more* in the postseason.

### Why not just say "home-court advantage"?
We could. But "advantage" is a flat statistical term. **Pilgrimage** and **ritual geography** foreground:
- The spatial dimension (arenas as sites)
- The temporal dimension (games as ceremonies)
- The experiential dimension (crowds as congregations)

The quirky pop-sci tone invites the reader to see the familiar (playoff home wins) as **strange and structured**—a field-guide approach rather than a recap.

---

## Confidence bands

| Metric | Confidence | Justification |
|--------|-----------|---------------|
| Playoff games count (82) | HIGH | Recountable from BRef schedule |
| Playoff home wins (48–34) | HIGH | Independent recount matches Phase 0 |
| Playoff home % (58.54%) | HIGH | Derived from HIGH counts |
| First-round Game 1s (8–0) | HIGH | ESPN Insider figure matches BRef R1 Game 1 lines |
| Regular-season home record (668–562) | MEDIUM | Wire journalism (Fox/AP), not NBA official release |
| Regular-season % (.5431) | MEDIUM | Derived from MEDIUM counts |
| "Worst home mark in history" claim | MEDIUM | Contemporaneous reporting; no contradicting source found |

### Why not HIGH for regular season?
The Fox Sports piece cites AP but does not link to an NBA Communications release. We trust the figure is accurate (no contradicting tallies found) but label it MEDIUM per protocol (secondary without primary trail).

---

## What we left blank

- Venue-specific home records (not in source CSV)
- Attendance per game (not in source CSV)
- Arena capacities or sellout rates (out of scope)
- Historical playoff home-court % by decade (could be added in future pass but not in this pack's scope)
- Game-by-game date/time (available in BRef but not relevant to ritual geography framing)

**Blank preferred over invention.** The pilgrimage map is **partial by design**.

---

## Reproducibility

1. Access Basketball-Reference 2024 NBA Playoffs page: https://www.basketball-reference.com/playoffs/NBA_2024.html
2. Count series (15) and games (82) from series tables (Finals, Conference Finals, Conference Semifinals, First Round)
3. For each game line in format `Away SCORE @ Home SCORE`, note winner (higher score) and home team (after `@`)
4. Tally home wins and home losses
5. Compute 48/82 = 0.5854

For regular-season comparison:
1. Retrieve Fox Sports / AP piece (2024-04-14) with 668–562 figure
2. Compute 668/1230 = 0.5431
3. Note "worst home-court mark" claim in article text

**No web scraping or API calls were used.** All counts are manual from publicly accessible HTML tables and articles, recorded in `home_court_2024_playoffs.csv` upstream.

---

**Compiled:** 2026-09-20  
**Reviewer:** Check against `data/derived/home_court_2024_playoffs.csv` (12 rows) and `home_court_2024_playoffs.md` (methodology doc) for consistency.
