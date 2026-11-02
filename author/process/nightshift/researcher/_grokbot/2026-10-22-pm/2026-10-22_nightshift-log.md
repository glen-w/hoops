# Nightshift log: 2026-10-22 (night_id 2026-10-22-overtime)

Processed 6 requests from `requests.json` (sha256 502f50ac…8b26b18ed, updated 09:24 UTC = 11:24 Paris). Finished around 12:20 Paris time (CEST, UTC+2).

**Constraints honoured:**
- Nothing was sent or posted, and nothing was bought.
- `requests.json` was not edited, and no files of Glen's were deleted or overwritten outside grokbot_outputs.
- Zotero "my pubs" was not touched. No Zotero item was deleted or trashed, and no existing item's fields or notes were edited. The only change to existing items was adding collections.
- The API key was never printed.

**Verification:** every DOI cited resolved via Crossref and OpenAlex. No citations were invented. Where only a title was found and no abstract, that's stated in the brief.

| id | title | status | output file(s) | note |
|---|---|---|---|---|
| 2026-10-22-overtime-researcher-01 | Kinematic variance × Kinrade reinvestment | done | 2026-10-22_researcher-01_kinematic-variance-x-reinvestment.md | No same-cohort or cross-cohort basketball study exists. The closest is golf (Malhotra 2015), where high reinvesters were *less* variable. Rusdiana has no variance measure; Kinrade 2015 is a passing-decision task. |
| 2026-10-22-overtime-researcher-02 | Workload × pressure in game logs | done | 2026-10-22_researcher-02_ft-pressure-workload-nba.md; …_ft_pressure_workload_summary.csv; …_ft_models.csv; …_ft_attempts_2015-2024.csv.gz; …_code_1-4_*.py | 519,640 NBA free throws, 2015-24. Late-and-close is about −2.5 to −3 pp vs the shooter's baseline, and −5.3 pp when trailing. Playoffs −1 pp. B2B has no effect. **No workload × pressure interaction**, so the cascade isn't supported. Workload main effects are confounded by selection. |
| 2026-10-22-overtime-researcher-03 | Automaticity baseline proxies | done | 2026-10-22_researcher-03_automaticity-baseline-proxies.md; …_player_season_automaticity_proxies.csv | Lit-grounded proxy table. Baseline FT% is stable (r = .88), but an individual "choke gap" is noise (year-to-year r = .08, split-half r = −.09), so player-level susceptibility can't be ranked from outcomes. |
| 2026-10-22-overtime-researcher-04 | Inhibitory control under fatigue | done | 2026-10-22_researcher-04_fatigue-executive-control.md | Exercise fatigue → executive control: small, intensity-dependent effects, and inhibition is often spared (Schmit 2015). Ego depletion × anxiety → worse free throws (Englert & Bertrams 2012). Twist: fatigue hurts *explicit* skills (Poolton 2007; Masters 2008). The full chain is untested. |
| 2026-10-22-overtime-researcher-05 | Release-point variability under pressure | done (evidence partial) | 2026-10-22_researcher-05_release-variability-under-pressure.md | Cruz 2026 (*Sci Rep*): pressure altered free-throw kinematics and prefrontal OxyHb (check direction in the full text). Mascret 2016 is null. Late elbow–wrist variability marks misses (Mullineaux 2010). Prediction from fatigue or workload is untested. |
| 2026-10-22-overtime-coder-01 | League-income Path A validation | **internal, awaiting researcher** (not fulfilled) | this log (note below) | A handoff between agents. It's logged, and the decision is left to the researcher. |

## coder-01: neutral note on the proposed sources (read-only look at the coder's sandbox)
The Path A scope (national media, salary cap/tax, attendance, BRI definition; licensing and local media deferred) looks coherent, and the official NBA cap/tax and attendance releases are the right primary sources. Some issues the researcher may want to weigh before approving:
1. **The salary-cap rows in `league-income-complete.csv` are off by one season.** The CSV gives 2024-25 = $154.647M cap and $188.103M tax, but the official NBA releases (pr.nba.com) give **2024-25 cap $140.588M, tax $170.814M** and **2025-26 cap $154.647M, tax $187.895M**. The 2025-26 row ("$165M, estimated") is therefore wrong as well. The coder's own `league_income_ingredients_sourced.md` has the correct values, so the two files disagree.
2. **2021-22 attendance:** the CSV has 20,862,460 (summed from ESPN). Last night's coder-01 found 20,910,813 (SBJ, NBA paid). They differ by about 48k, so pick one definition and say which.
3. **Source URLs are bare domains** for the media-rights rows (`https://www.cnbc.com`, `https://variety.com`, `https://pr.nba.com`). They can't be cited as they stand and need article-level URLs.
4. **`league-income-sources.md`, which the request cites, doesn't exist** in the coder's analysis folder. `league_income_ingredients.csv` is still the 107-byte placeholder sentence flagged on 21 Oct.
5. Several MEDIUM figures have no source attached: BRI 2024-25 $10.25B, team revenue $12.75B, per-team national TV share $103M/$143M.
6. A schema quirk: attendance rows carry `currency = USD`.

## Zotero additions (Glen's instruction, relayed mid-run)
- **48 new items created**, all journalArticle, with full Crossref metadata and abstracts where available. Each is tagged `nightshift-2026-10-22` and its Extra field reads "Added by Grok Bot nightshift 2026-10-22-overtime". Verified 48/48.
- **4 existing items** had a collection added (nothing else changed).
- **3 existing items** were cited unchanged: Rusdiana 6REBX2D3, Wilson 2009 QDQPA32B, and Englert 2015 BGDSL665 (plus WVNEJ5BP and 74QZDR69, also cited and unchanged).
- Collections used:
  - hoops/⭐game/skills/shooting/free throws (HN7AY374)
  - …/shooting (TXW37UV2)
  - …/clutch (VTGSGUCJ)
  - …/offense/hot hand (M7Q4XYQQ)
  - hoops/⭐psych/mental (72K9LVS4)
  - hoops/physical (ZQPEGZSV)
  - hoops/physical/recovery (GQPXV3E5)
  - hoops/other sports (RNWE7I8B), for non-basketball sports
- No new collections were created.

| Zotero key | Paper (DOI) | Collection(s) | Action |
|---|---|---|---|
| FITU79BR | Kinrade et al. 2015, PSE (10.1016/j.psychsport.2015.03.007) | psych/mental | created |
| WZTH4FH4 | Kinrade et al. 2010, DSRS, JSS (10.1080/02640414.2010.499439) | psych/mental | created |
| 6T2X99VS | Kinrade et al. 2010, PSE (10.1016/j.psychsport.2010.02.005) | other sports | created |
| MZH5RB84 | Masters 1992, BJP (10.1111/j.2044-8295.1992.tb02446.x) | other sports | created |
| M4M9SCEP | Masters & Maxwell 2008 (10.1080/17509840802287218) | psych/mental | created |
| 6NMFFTRA | Malhotra et al. 2015 (10.1016/j.psychsport.2014.11.008) | other sports | created |
| 9XUJRPUJ | Toner & Moran 2011 (10.1080/02640414.2011.553964) | other sports | created |
| W9WJQ8CX | Jackson et al. 2006 (10.1123/jsep.28.1.49) | other sports | created |
| IJD8QBA2 | Zhu et al. 2011 (10.1016/j.biopsycho.2011.02.004) | other sports | created |
| R3JBSWVD | van Ginneken et al. 2018 (10.1080/00222895.2017.1365045) | other sports | created |
| 29H4I5CF | Gray 2004 (10.1037/1076-898x.10.1.42) | other sports | created |
| UXGADH22 | Cooke et al. 2010 (10.1111/j.1469-8986.2010.01021.x) | other sports | created |
| AWUHXZ8R | Klämpfl et al. 2013 (10.1371/journal.pone.0082470) | other sports | created |
| ME4JJMFX | Lam et al. 2009 (10.1080/02640410802448764) | shooting | created |
| B4FT8QJ4 | Parr et al. 2023 (10.1080/1750984x.2021.1878548) | psych/mental | created |
| IRZSWU9G | Iwatsuki et al. 2018 (10.2478/hukin-2018-0042) | other sports | created |
| 86WR2S8S | Cruz et al. 2026, Sci Rep (10.1038/s41598-026-51871-7) | free throws | created |
| 7GNTN8KA | Uygur et al. 2010 (10.2478/v10078-010-0019-0) | free throws | created |
| H3WPJBPT | Button et al. 2003 (10.1080/02701367.2003.10609090) | free throws | created |
| 9PXHES4X | Mullineaux & Uhl 2010 (10.1080/02640414.2010.487872) | free throws | created |
| MVTJK42R | Mascret et al. 2016 (10.1371/journal.pone.0157215) | free throws | created |
| VJBE54ZM | Causer et al. 2011 (10.1037/a0023225) | other sports | created |
| JDM6QK3M | Pijpers et al. 2005 (10.1080/02724980343000945) | other sports | created |
| AEGQAINW | Ardigò et al. 2018 (10.3389/fphys.2018.00075) | shooting | created |
| UZKNETGQ | Erčulj & Supej (10.33607/bjshs.v4i63.567) | shooting | created |
| 9CE97W59 | Carson & Collins 2016 (10.1080/1750984x.2015.1072231) | psych/mental | created |
| 968MSP5H | Schmit et al. 2015 (10.1016/j.neuropsychologia.2015.01.006) | physical | created |
| 5SAM6MDR | Labelle et al. 2013 (10.1016/j.bandc.2012.10.001) | physical | created |
| 2GUVVM92 | Dietrich 2003 (10.1016/s1053-8100(02)00046-6) | physical | created |
| SDQAAIJM | Dietrich & Audiffren 2011 (10.1016/j.neubiorev.2011.02.001) | physical | created |
| MP9ZH6J5 | Chang et al. 2012 (10.1016/j.brainres.2012.02.068) | physical | created |
| JGV4SB89 | McMorris & Hale 2012 (10.1016/j.bandc.2012.09.001) | physical | created |
| ZN6MV7JP | Rooks et al. 2010 (10.1016/j.pneurobio.2010.06.002) | physical | created |
| 4JDH26VS | Habay et al. 2021 (10.1007/s40279-021-01429-6) | psych/mental | created |
| CFEK5ZUS | Smith et al. 2016 (10.1080/02640414.2016.1156241) | other sports | created |
| S5XB8I7S | Englert & Bertrams 2012 (10.1123/jsep.34.5.580) | free throws | created |
| IHVZAZVK | Englert et al. 2015, JSEP (10.1123/jsep.2014-0219) | other sports | created |
| R7ZM3GAM | Shaabani et al. 2020 (10.1037/spy0000201) | free throws | created |
| V693HCNS | Poolton et al. 2007 (10.1016/j.concog.2006.06.008) | other sports | created |
| PGRIUACI | Masters et al. 2008 (10.1016/j.concog.2007.03.009) | other sports | created |
| TSCM8R7E | Banihosseini et al. 2025 (10.3389/fpsyg.2025.1438313) | other sports | created |
| 3B3G4ASB | Bahrami et al. 2020 (10.29252/ijmcl.2.4.4) | shooting | created |
| 3ZD3W5EQ | Beilock & Carr 2001 (10.1037/0096-3445.130.4.701) | other sports | created |
| 48PMTJ6G | Kal et al. 2018 (10.1371/journal.pone.0203591) | psych/mental | created |
| AAQT69K4 | Cao, Price & Stone 2011 (10.1177/1527002511404785) | free throws; clutch | created |
| DHQ9VHRN | Toma 2017 (10.1177/1527002515593779) | free throws; clutch | created |
| K6C2ACJD | Steenland & Deddens 1997 (10.1093/sleep/20.5.366) | physical/recovery | created |
| BQ4BBNT7 | Morgulev & Galily 2018 (10.3389/fpsyg.2018.00979) | clutch | created |
| U45UM6YQ | Verhoeven & Newell 2016 (10.1016/j.humov.2016.07.007) | + free throws | existing: collection added |
| NBMVPIVS | Esteves et al. 2021 (10.1080/17461391.2020.1736179) | + physical/recovery | existing: collection added |
| V3JBJL69 | Arkes 2010 (10.2202/1559-0410.1198) | + hot hand, + free throws | existing: collections added |
| ALJSJCYA | Lantis & Nesson 2021 (10.1177/15270025211006889) | + hot hand | existing: collection added |
| 6REBX2D3 / QDQPA32B / BGDSL665 / WVNEJ5BP / 74QZDR69 | Rusdiana 2020 / Wilson 2009 / Englert 2015 PSE / Filipas 2021 / Sansone 2026 | (already filed) | cited, unchanged |

A rollback list of created keys is on the box at `/workspace/nightshift/2026-10-22-overtime/work/zcreated.json`. Collection patches with before/after are in `zpatch_log.json`.

## Needs Glen
1. **Zotero filing choices.** Exercise-cognition papers went to hoops/physical, and general reinvestment theory went to hoops/⭐psych/mental. Move them if you'd prefer a different home. Several key Elsevier items have no abstract, because the publisher withholds it from Crossref and OpenAlex.
2. **Data source.** The pull uses the shufinskiy/nba_data GitHub mirror of stats.nba.com (Apache-2.0), because stats.nba.com blocks my box. If the book needs the official API as provenance, the code can be re-pointed at `nba_api` from your Mac.
3. **coder-01's CSV salary-cap error** (item 1 above) should be fixed before the 23 Oct league-income chapter deadline the coder mentions. It's the researcher's call, but you may want to know.
