# NBA 2024-25 regular-season attendance: what is sourced and what is derived

Access date: 2026-10-22 (Europe/Paris), tick r481.
Status: **no official NBA total found.** Keep the 2024-25 total out of `league_income_ingredients.csv` until an official or original-SBJ figure is fetched.

## Sourced (secondary)

Caitlyn Holroyd, theScore, citing David Broughton and Tom Friend, Sports Business Journal. The SBJ link path suggests 2025-04-15; the SBJ original was not fetched.
https://video.thescore.com/nba/news/3268109/nba-set-2nd-highest-regular-season-attendance-mark-in-2024-25

- "The average attendance for the 2024-25 regular season was 18,147"
- "It was the second time ever that the NBA's total regular-season attendance exceeded 22.3 million fans."
- Bulls "had the highest average among teams at 20,138 fans per game"
- Clippers: "the biggest drop in attendance with a 12.6% decline"
- No sellout count and no game count are given.

Confidence: MEDIUM (secondary report of the trade press).

## Derived (label DERIVED in any prose)

Assumption: 18,147 is a per-game average over 1,230 regular-season games (30 teams × 82 games ÷ 2). The article does not say which games are included.

- Point value: 18,147 × 1,230 = 22,320,810.
- 18,147 is rounded to the nearest fan, so the implied total lies between 18,146.5 × 1,230 = **22,320,195** and 18,147.5 × 1,230 = **22,321,425**.
- So: about **22.32 million**. This fits theScore's "exceeded 22.3 million".

## Cross-check of the method (snippet-grade)

The AP report on 2023-24 (https://www.burnabynow.com/basketball/nba-average-attendance-was-18324-this-season-league-says-71-of-games-were-sellouts-8602203) returned HTTP 403 on fetch. These figures come from the search-result snippet only:
- 2023-24 total 22,538,518; average 18,324; 873 sellouts (71%).
- 2022-23 total 22,234,502.

Checks:
- 22,538,518 ÷ 1,230 = 18,324.0. The snippet's average matches, which supports the 1,230-game basis.
- "Second time above 22.3M" is consistent with these figures. 2023-24 (22.54M) is above the line, 2022-23 (22.23M) is below it, and 2024-25 (about 22.32M) is above it.

## Open

- An official NBA release or the original SBJ article for the exact 2024-25 total.
- A 2024-25 sellout count, which no source fetched so far gives.
- Verify the AP 2023-24 and 2022-23 totals from a fetchable copy (AP News or another syndicated outlet) before they go into the CSV.
