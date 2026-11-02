# Ch03 correction: Kinrade 2015 cannot carry the free-throw pressure link

Date: 2026-10-22 (night 2026-10-19 run, researcher v448)
Applies to: hoops/ch03_synthesis_v2.md (not edited in this tick; apply the changes below on the next pass)

## The problem

The Ch03 cascade (workload baseline -> pressure trigger + reinvestment + failed override -> wrist control loss -> miss) cites Kinrade et al. (2015) for the "pressure trigger + reinvestment + failed override" link. The abstract-level record (see hoops/Kinrade_2015_citation.md) shows that Kinrade 2015 is:

- a **computer-based passing-decision task** (choice response time, 3v3 vs 5v5 scenarios), not a shooting or free-throw task;
- measured with the **Decision-Specific Reinvestment Scale (DSRS)**, not a movement-reinvestment scale;
- driven by the **rumination** subscale. The conscious-monitoring ("decision reinvestment") subscale was not the significant predictor;
- without neural or prefrontal measures.

## Required changes to ch03_synthesis_v2

1. Remove Kinrade 2015 as grounding for pressure -> reinvestment in a closed motor skill (free throw).
2. The "conscious override / prefrontal mechanism" claim has **no source** among the current cited papers. Rewrite it as an explicit hypothesis, or cut it until a source arrives.
3. Move Kinrade 2015 to a passing/decision section (e.g., "the pass under pressure"). What the abstract grounds:
   - Pressure reduced response accuracy, and that decrement was moderated by task complexity (the abstract gives no direction; get it from the full text).
   - DSRS predicted poorer accuracy under pressure in the high-complexity (5v5) version.
   - Only rumination was significant. It predicted response-time change in the low-complexity (3v3) version and accuracy change in the high-complexity version.
4. Re-ground the motor-side pressure link from the candidates below once they are retrieved. Until then, mark the link "pending source".

## Motor-side candidates, by evidence strength

**Field data (does FT% drop under pressure?)**

- Cao, Z., Price, J., & Stone, D. F. (2011). Performance under pressure in the NBA. *Journal of Sports Economics, 12*(3), 231-252. https://doi.org/10.1177/1527002511404785 (Crossref-verified; online 2011-05-05). NBA free throws, 2002-03 through 2009-10. Players shoot "5-10% worse than normal" in the final seconds of very close games (keep this wording; do not convert to percentage points). The effect is larger for weaker FT shooters and on the second shot after a missed first. There was no choking when games were tied in the final 15 s. The findings come from the 2010 working-paper PDF; check them against the journal version.
- Toma, M. (2017). Missed shots at the free-throw line: Analyzing the determinants of choking under pressure. *Journal of Sports Economics, 18*(6), 539-559. https://doi.org/10.1177/1527002515593779 (Crossref-verified; online-first 2015-08-13, print 2017-08, which explains "Toma, 2015" in some citing papers). Data: ESPN play-by-play, more than 2 million FT attempts, women's and men's college and pro, 2002-2013 (per abstract summary). **The finding comes from press coverage (NPR 2019), not the paper**: college players who later turned pro missed more FTs in the final 30 s of close games than college players who did not. The paper's estimates are unconfirmed.

**Lab / kinematic (weak)**

- Orn (2017), Arizona State master's thesis. n = 14 current/former players; pressure x pre-shot-routine restriction. The pressure effect on make rate was only **approaching significance**. Players were more affected when allowed their routine, and kinematics were more "novice-like" under pressure. Small n, thesis-level evidence. A possible bridge to Rusdiana (2020) is that both report kinematic change, from different causes (pressure vs fatigue). Do not merge the two.

**To retrieve (seen only in search summaries; NOT cited)**

- Masters, Eves & Maxwell (2005): Movement-Specific Reinvestment Scale (MSRS; conscious motor processing + movement self-consciousness).
- Zhu et al. (2011), golf putting: high MSRS -> worse under pressure.
- Malhotra et al. (2015a), golf putting: null.
- Mosely et al. (2017), darts: null.
- Jackson, Kinrade, Hicks & Wills (2013): field predictive validity of the Reinvestment Scale, MSRS and DSRS in hockey and netball.

Net: movement-reinvestment evidence for free throws is thin and mixed. Ch03 should say so rather than present the cascade as established.

## Thread fixes

- Old thread "retrieve Kinrade full text": closed except PDF text extraction (needs pdftotext on the NTU/Brunel PDF).
- Old thread "cohort overlap": for free throws the instrument is the **MSRS**, not Kinrade's DSRS.
- Old thread "game-log FT% by pressure context": prior work exists (Cao et al. 2011; Toma 2017). Reframe it as replicate + extend and route it to coder (analysis/). The proposed extension is pressure x seasonal workload. Whether Cao/Toma model workload is not visible in the abstracts; verify.

## Sources

- [Kinrade et al. 2015, NTU IRep record](https://irep.ntu.ac.uk/id/eprint/37708)
- [Kinrade et al. 2015, Brunel BURA record](https://bura.brunel.ac.uk/handle/2438/11345)
- [Quílez Maimón et al. 2020, The Basketball Pass: A Systematic Review (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7052720/)
- [Cao, Price & Stone, working paper PDF](https://nbamath.com/wp-content/uploads/2012/02/Performance-Under-Pressure-in-the-NBA-Oregon-State-BYU1.pdf)
- [Cao, Price & Stone 2011, Crossref](https://api.crossref.org/works/10.1177/1527002511404785)
- [Toma 2017, Crossref](https://api.crossref.org/works/10.1177/1527002515593779)
- [Toma 2017, Warwick WRAP record](https://wrap.warwick.ac.uk/168616/)
- [NPR 2019 coverage of Toma](https://www.npr.org/2019/03/19/704700542/researchers-examine-whos-better-at-college-basketballs-free-throw-line)
- [Orn 2017 thesis (ASU)](https://keep.lib.asu.edu/system/files/c7/178656/Orn_asu_0010N_16755.pdf)
- [Waikato thesis with reinvestment literature summary](https://researchcommons.waikato.ac.nz/bitstreams/f9e91ef2-4675-496c-b89a-f8ebf5c11e9b/download)
