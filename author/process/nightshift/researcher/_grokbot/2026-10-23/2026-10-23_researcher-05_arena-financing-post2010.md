# Arena financing since 2010: who paid for the new NBA buildings?

**Request:** 2026-10-22-researcher-05 + 2026-10-22-coder-04 · **Status:** done (a few cells left as "not found") · **Data:** `2026-10-23_researcher-05_arena_financing.csv` · **Prepared by:** Grok Bot nightshift, 23 Oct 2026

## Bottom line (suggestions, not orders)
- The post-2010 NBA arenas split into two groups. **Privately built:** Chase Center ($1.4B) and Intuit Dome (~$1.8–2B), plus T-Mobile Arena in Vegas (NHL, no NBA team). **Heavily subsidised:** Golden 1 (~46% public), Fiserv Forum (~48%) and Little Caesars (~38%). Barclays sits in between and is the hardest to score.
- **Barclays is the main trap.** The direct city and state capital was about $200–231M on a ~$1.07B project. Most of the money ($511M) came from tax-exempt **PILOT bonds**, which are repaid from payments made *instead of* property tax. Whether you count those as "public money" changes the answer completely. The NYC Independent Budget Office itself says the subsidies are hard to compare. I'd suggest describing the instruments rather than quoting a single %.
- The research consensus is that new venues bring little or no local economic growth, so subsidies are rarely justified (Bradbury, Coates & Humphreys 2023, a review of 130+ studies). Headline public costs are also understated: once omitted items such as land, infrastructure and forgone taxes are counted, the average subsidy rises about 40% (Long 2005).
- **Corrections to the request:** Intuit Dome opened in **2024**, not 2014; 2014 is when Ballmer bought the Clippers. Little Caesars Arena was built for the Red Wings, and the Pistons moved in as tenants in 2017.

## Arena table (summary; full sourcing in CSV)
| Arena (opened) | Cost | Public $ | Public % | Main instruments | Confidence |
|---|---|---|---|---|---|
| Barclays Center (2012) | ~$1.07B (ENR) [7X265499] | $200–231M direct capital (IBO 2009 via Observer [78PQBXFC]; Institutional Investor [RKSC5KZH]) | **not found** (ambiguous) | $511M PILOT bonds [CR9JS8MU]; tax exemptions; MTA land (IBO 2023 [2EE5I66G]) | medium |
| Chase Center (2019) | $1.4B | $0 for the arena | 0 | private, team self-financed [CS3TRCH7] | medium |
| Intuit Dome (2024) | $1.8B (~$2B later press, not opened) | $0 direct; land-sale terms not found | 0 (direct) | private; city land sale; $100M team-paid community benefits [AQSPEH2K, 2ZNWH3X6] | medium |
| Golden 1 Center (2016) | $558.2M [XETIVVT4] | $255M | 45.7 | city lease-revenue bonds ($272.9M sold Sep 2015), repaid from parking, then lease and tax increment [QR37ZIBW] | medium |
| Little Caesars Arena (2017) | $862.9M | $324M | 37.5 | Detroit DDA tax-increment bonds that capture school taxes [ASQSSF2Q] | medium-high |
| Fiserv Forum (2018) | $524M | $250M | 47.7 | state $80M + county, city TIF, Wisconsin Center District bonds [ZWNMSABN] | medium |
| *Crypto.com Arena (1999; context)* | $375M [K6B6VREP] | $71.1M city [UNKX52P5] | 19.0 | city loan + reserve fund + redevelopment agency; terms reworked 2003 [N756P686] | medium |
| T-Mobile Arena (2016; NHL) | $375M | $0 | 0 | MGM–AEG private [5S7TTZZX] | medium |
| *Allegiant Stadium (2020): NON-NBA (NFL) comparator* | $1.97B | $750M | 38.1 | Clark County bonds + hotel room tax [UWDUKHR6] | high |
| *SoFi Stadium (2020): NON-NBA (NFL) comparator* | not found | not found | not found | not verified this pass | low |

Percentages are plain public ÷ total cost. They do not include forgone property taxes or the value of land unless the source does. Where cost and subsidy come from different sources, the CSV says so.

## Annotated sources (peer-reviewed)
| Citation | DOI | Design | Setting | Key result | Use in chapter |
|---|---|---|---|---|---|
| Bradbury, Coates & Humphreys (2023) *J Econ Surveys* 37(4):1389–1431 [XDMTJR8C] | 10.1111/joes.12533 | Literature review | 130+ studies, US/Canada/Europe | Consensus: very limited local economic impact; subsidies not justified by growth | The anchor citation for "economists agree" |
| Long (2005) "Full Count" *J Sports Econ* 6(2):119–143 [CB2ZQ4CG] | 10.1177/1527002504264614 | Cost accounting | 99 facilities | Counting omitted costs raises the average public subsidy from $126M to $177M (+40%) | Why headline subsidy figures are too low (pre-2010, method still standard) |
| Sroka (2024) *Social Science Quarterly* [ASQSSF2Q] | 10.1111/ssqu.13424 | Case study | Little Caesars Arena, Detroit | $324M public on $862.9M via DDA tax-increment capture during and after bankruptcy | The Detroit story |
| Propheter (2012) *J Urban Affairs* 34(4):441–459 [CGMDP7GN, existing] | 10.1111/j.1467-9906.2011.00597.x | Empirical (see paper) | NBA arenas | Tests whether arenas spur local development (result not re-read tonight; check before citing) | Basketball-specific "catalyst" question |
| Swindell & Rosentraub (1998) *Public Admin Review* 58(1):11–20 [9795GQW9, existing stub] | 10.2307/976884 | Policy analysis | US stadiums/arenas | Who benefits from teams and what that implies for public funding (details not re-read tonight) | Background (pre-2010) |

## Check of the 4 existing Zotero items (read-only; nothing edited)
- **CGMDP7GN** (Propheter 2012). Correct and relevant. Small gaps: issue field empty (should be 4), no abstract, and the URL points to consensus.app instead of the DOI.
- **FPYIXZPD** (Downs & Seifried 2023, "The 'Me' Arena: Examples of Capitalism within the NHL and NBA, 1950–1989"). No journal, DOI, URL, volume or pages, and the title has a line-break artefact ("As- sociation"). I couldn't find it in Crossref; the nearest match is Downs' LSU dissertation (10.31390/gradschool_dissertations.4989). It is history up to 1989, so not post-2010 financing. It needs Glen to confirm where it was published.
- **M7KEA87F** (Vrooman 2009, "Theory of the Perfect Game", *Rev Ind Org* 34(1):5–44, 10.1007/s11151-009-9202-7). Metadata complete. It's about league structure and competitive balance and only touches venue subsidy in passing, so it doesn't belong in this table.
- **9795GQW9**. A bare "document" with only a PDF filename, sitting in ‼️ incomplete. It is evidently Swindell & Rosentraub 1998 (DOI above) and needs full metadata. I left it alone per the rules.

## Where evidence is thin
- **Barclays %**: depends on whether PILOT bonds and exemptions count as public money. No single agreed figure was found.
- **Golden 1** cost comes from the SacBee via a Wikipedia citation; I didn't open the SacBee page.
- **Fiserv**: the split between city, county and the Wisconsin Center District is unverified, and so is any Chase Center or Intuit Dome public infrastructure spending.
- **SoFi**: nothing sourced.
- The 2022+ renovation cost for Crypto.com Arena wasn't found.

## What the book can safely say
Since 2010, NBA arenas have been paid for in very different ways. Two Bay Area and LA buildings were privately financed: Chase Center for about $1.4 billion and Intuit Dome for about $1.8–2 billion. Sacramento, Milwaukee and Detroit each put roughly 38–48% public money into their new arenas, mostly through city bonds and tax-increment schemes. Brooklyn's Barclays Center used tax-exempt bonds repaid from payments in lieu of property taxes, which makes its "public share" a matter of definition. Across 130+ studies, economists find that such venues bring little new local growth, and official subsidy totals usually leave out land, infrastructure and forgone taxes.
