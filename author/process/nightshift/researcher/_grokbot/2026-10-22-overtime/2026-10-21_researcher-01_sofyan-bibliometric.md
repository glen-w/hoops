# Sofyan et al. 2022: A bibliometric review of basketball publication trends

**Request:** 2026-10-21-researcher-01 (high). Map the research landscape: publication volume, themes and gaps over 50 years.
**Status:** done
**Sources used:** Zotero item `2BNAQFDH` (metadata, the Paperful summary note and the full-text index of the attached PDF), OpenAlex W4312064312 and Crossref. Key numbers were checked against the full text.

## Citation
Sofyan, D., Abdullah, K. H., & Gazali, N. (2022). A bibliometric review of basketball game: Publication trends over the past five decades. *ASM Science Journal*, 17, 1–12. https://doi.org/10.32802/asmscj.2022.1277

## Core argument
Basketball research has grown sharply since about 2011, but the field has never been mapped bibliometrically. A Scopus snapshot of volume, countries, authors, institutions and keywords can show where the field's knowledge sits and where the gaps are.

## Methods
- Descriptive bibliometric analysis with a PRISMA-style selection flow. The Scopus search was run on 26 Dec 2021 for "basketball" in title, abstract and keywords, with no language limit.
- The search returned 12,865 records. Of these, **584 were retained "based on topic"**, and the paper does not clearly say how that topic screen worked.
- The analysis used Excel, Publish or Perish and VOSviewer (author-keyword co-occurrence, full counting, minimum two occurrences).

## Key findings (checked against the full text)
- There were 584 publications from 1969 to 2021. Output first reached double digits in 2006 (11 papers) and rose steeply after 2011. There were 66 papers in 2020 and 74 in 2021, 140 across the two years.
- The USA was the most productive country, with 210 works. J. Sampaio and J. Yanci were the most prolific authors and Universidad de Granada the most productive institution.
- *Lecture Notes in Computer Science* was the top source, with 11 papers.
- "Basketball" clusters with "coach" and "collegiate athletes" in the keyword map.
- The authors list their own limitations: a single database and an under-specified way of finding and categorising records.

## Critical read
- **584 out of 12,865 is a very narrow cut.** The headline "five decades of basketball research" describes a topic-filtered subset under 5% of the hits, and the filter can't be reproduced from the paper. Use it as an illustrative snapshot, not a census.
- The study is descriptive only. It reports no citation-impact analysis, no thematic evolution over time and no content review. Any "themes and gaps" claims in the chapter need other sources (see below).
- It appears in a modest venue. OpenAlex shows about 9 citations as of Oct 2026.

## Fit with the chapter
- Chapter 10, "Five Decades of Basketball Research", and the 06 bibliometric drafts in `researcher/hoops/` are one-paragraph stubs. Their claims ("from biomechanics to analytics, from coaching pedagogy to sports science") are **not findings of this paper**. Sofyan reports volume, geography, authors and keyword co-occurrence, not a shift in disciplines over time.
- Chapter 10 cites the path `hoops/_reading list/Sofyan ...`. The note in the sandbox sits at `hoops/Sofyan ...`, so the path should be checked.
- Best use: a framing paragraph ("the field is young, US- and Iberian-centred, and accelerating since 2011"), followed by systematic reviews that actually describe the content.

## Related works (DOIs verified via Crossref)
1. Courel-Ibáñez, J., McRobert, A. P., Toro, E. O., & Vélez, D. C. (2017). Collective behaviour in basketball: A systematic review. *International Journal of Performance Analysis in Sport*, 17(1–2), 44–64. https://doi.org/10.1080/24748668.2017.1303982. This is a content-level map of the tactical and performance-analysis strand.
2. Stojanović, E., Stojiljković, N., Scanlan, A. T., Dalbo, V. J., et al. (2018). The activity demands and physiological responses encountered during basketball match-play: A systematic review. *Sports Medicine*, 48(1), 111–135. https://doi.org/10.1007/s40279-017-0794-z. This is the physiology strand.
3. Donthu, N., Kumar, S., Mukherjee, D., Pandey, N., & Lim, W. M. (2021). How to conduct a bibliometric analysis: An overview and guidelines. *Journal of Business Research*, 133, 285–296. https://doi.org/10.1016/j.jbusres.2021.04.070. Useful as a methods yardstick for what Sofyan omits (citation and co-citation analysis, thematic evolution).
4. van Eck, N. J., & Waltman, L. (2010). Software survey: VOSviewer, a computer program for bibliometric mapping. *Scientometrics*, 84(2), 523–538. https://doi.org/10.1007/s11192-009-0146-3. This is the tool Sofyan used.

## Suggested next step (not done)
A quick OpenAlex count of "basketball" works by year and concept would give the chapter a reproducible volume curve. It would also show how far Sofyan's 584 understates the field. This is about an hour of coder work, if Glen wants it.
