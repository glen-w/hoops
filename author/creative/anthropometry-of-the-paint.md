# Anthropometry of the Paint

*A secular trend essay in the key of climate normals and growth charts*

Basketball’s painted area is a small rectangle with outsized weather. Every season the league publishes bodies into it—listed heights, listed weights, the soft bureaucracy of the roster page—and over seventy-odd winters those listings behave less like trivia and more like a climate series. You do not need a dendrometer. You need a table.

The table we have is blunt and generous: an unweighted mean of listed heights for every player with a season record, season by season, from **1946-47** through **2020-21**. In the first BAA winter the league average sits at **6'2.13''** (**74.13** inches). By **2003-04** it has climbed to a series peak of **6'7.20''** (**79.2** inches)—a secular rise of a little more than **five inches** of mean listed height across roughly six decades. That is not a rumor about centers. That is the whole population, averaged, drifting upward the way a regional mean temperature drifts: slowly enough that a single season feels normal, fast enough that a mid-century photograph looks like another sport.

## The warming curve, then the plateau

Decade means (themselves derived from the seasonal series, not freelanced) make the curve readable as geology rather than gossip:

| Decade | League mean listed height |
|--------|---------------------------|
| 1940s | 6'2.61'' (74.61 in) |
| 1950s | 6'4.43'' (76.43 in) |
| 1960s | 6'5.46'' (77.46 in) |
| 1970s | 6'5.93'' (77.93 in) |
| 1980s | 6'6.77'' (78.77 in) |
| 1990s | 6'6.86'' (78.86 in) |
| 2000s | 6'7.04'' (79.04 in) |
| 2010s | 6'6.82'' (78.82 in) |
| 2020s (partial) | 6'6.39'' (78.39 in) |

Read it like a Holocene strip: rapid early rise, then a high stand. The **1940s** to **1960s** are the steep face—nearly three inches of decade-mean growth as the league professionalizes and taller bodies become ordinary rather than carnival. The **1980s** and **1990s** sit on a warm plateau around the high **6'6''**s. The **2000s** decade mean (**6'7.04''**) is the warmest stratum in the pack; the seasonal peak year **2003-04** lives inside it. Then—quietly, without a press conference—the series turns.

By **2013-14** the league average is **6'6.84''**. By **2020-21**, the last year in the landed RunRepeat extract, it is **6'6.33''**—**0.87** inches below the **2003-04** peak. The paint has not gotten shorter in absolute terms; the *mean* has cooled. Anthropometry people know this pattern from other populations: selection pressure changes, composition changes, the definition of a “big” changes, and the average follows.

## Position weather inside the climate

The league mean is a blunt instrument. Position series (same source, same seasons) show that the paint’s weather is stratified:

- **Centers** open at **6'7.6''** in **1946-47**, peak at **6'11''** in **1981-82**, and finish the series at **6'10''** in **2020-21**.
- **Power forwards** climb from **6'5.2''** (**1946-47**) to a peak of **6'9.4''** (**2004-05**), then ease to **6'8.3''** (**2020-21**).
- **Small forwards** rise from **6'2.9''** to a **2002-03** peak of **6'7.9''**, then sit at **6'6.6''** by **2020-21**.
- **Shooting guards** peak later (**6'5.3''** in **2008-09**) than the league mean and finish at **6'4.3''**.
- **Point guards**—the supposed “small” end of the court—move from **6'1.1''** (**1946-47**) to a late peak of **6'2.5''** (**2018-19**) and **6'2.4''** in **2020-21**. Their trough is an early-1950s **6'0.0''** (**1952-53**).

So the late cooling of the league mean is not a fairy tale about disappearing seven-footers alone. It is also a remix: wings and guards who stretch the floor, bigs who handle, position labels that no longer map cleanly onto the old growth chart. The paint still hosts giants. The *average body* in the building is a slightly different climate.

Rookies track the same long rise—from **6'2.1''** in **1946-47** to **6'5.8''** in **2020-21**—a reminder that the pipeline, not just survivor bias among veterans, participates in the secular trend. Weight (where the series is populated) opens at **186** lb in **1946-47**, peaks at **223** lb in **2010-11**, and sits at **217** lb in **2020-21**: mass and stature do not move in perfect lockstep, which is exactly what an honest anthropometric series should admit.

## What a secular trend is allowed to mean

A climate essay about basketball must refuse two temptations. First: inventing a moral. The numbers do not prove that “skill beat size,” or that “size always wins,” or that any particular superstar caused the inflection. They show a population mean that rose for decades, peaked in the early **2000s**, and then eased—while three-point volume elsewhere in the book exploded. Correlation is atmosphere; causation needs other instruments.

Second: overclaiming the instrument. These are **listed** heights, unweighted by minutes, transcribed from a secondary analysis of public roster data (RunRepeat’s Curcic series, citing public player-season records). Listed height is a social fact as much as a biomechanical one. That does not make the trend fake. It makes it *institutional*—the league’s own paperwork weather.

Still: five inches of mean listed height between the first winter and the peak year is a real shape on the page. The subsequent near-inch of cooling is a real shape too. If you want a metaphor that survives peer review, call the paint a microclimate. For half a century it warmed. Lately the thermostat—style, spacing, who gets a roster spot—has been set a degree cooler. The ice cores are CSV rows. The cores do not care who dunks.

---

## Sources

Access date for this creative pass: **2026-09-20** (Europe/Paris). Data `as_of` on source CSVs: **2026-09-19**.

| Claim / figure | Cell / row | Path |
|----------------|------------|------|
| 1946-47 league avg **6'2.13''** / **74.13** in | `season_label=1946-47`, `value_display`, `value_numeric` | `/workspace/hoops-phase0-tables/height-series/nba_height_league_by_season.csv` (also `hoops-swatches-work/data/derived/height-series/`) |
| Peak **2003-04** **6'7.20''** / **79.2** in | `season_label=2003-04` | same |
| **2020-21** **6'6.33''** / **78.33** in (series end) | `season_label=2020-21` | same |
| Decade means 1940s–2020s | `metric=avg_height_league_decade_mean` | `/workspace/hoops-phase0-tables/height-series/nba_height_series.csv` |
| Position first/peak/last (C, PF, SF, SG, PG) | `metric=avg_height_by_position` | same |
| Rookie heights 1946-47 / 2020-21 | `metric=avg_height_rookies` | same |
| Weight 1946-47 **186**, peak **2010-11** **223**, **2020-21** **217** | `metric=avg_weight_league` | same |
| Method / confidence HIGH / secondary label | — | `/workspace/hoops-phase0-tables/height-series/METHODOLOGY.md` |

Primary public source behind the extract: Curcic, D. — *70 Years of Height Evolution in the NBA*, RunRepeat, https://runrepeat.com/height-evolution-in-the-nba (accessed for transcription **2026-09-19**). Series ends at season-end year **2021** as published; no post-2021 heights invented here.
