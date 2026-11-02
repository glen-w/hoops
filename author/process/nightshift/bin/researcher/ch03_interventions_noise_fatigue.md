# Ch03 section draft: what helps under pressure, plus noise and fatigue (2026-10-22)

Status: new draft section for Ch03. It does NOT replace ch03_synthesis_v2 or ch03_pressure_sources.md. Merge by hand.

Grounding tags:
- [A] = abstract or Crossref metadata checked on the web this tick
- [S] = local paperful-summary only (qwen3.8 machine summary). Full text not read.
- [?] = inconsistent or unverified. Do not print as fact.

## 1. The intervention map: Gröpel & Mesagno

Gröpel, P., & Mesagno, C. (2019). Choking interventions in sports: A systematic review. *International Review of Sport and Exercise Psychology*, 12(1), 176-201. https://doi.org/10.1080/1750984X.2017.1408134 (online 19 Dec 2017; print Jan 2019) [A]

If a shooter can choke, the practical question is what helps. The broadest answer in our stack is this review. It includes 47 empirical studies with athletes, published up to April 2017, using experimental, quasi-experimental and single-case designs [A]. Its 13 interventions fall into three families [A]:

- **Distraction-based**: keep attention off task-irrelevant cues. Examples from the summary: pre-performance routines, cue words, deep breathing [S].
- **Self-focus-based**: keep conscious, step-by-step control out of a skilled movement. Examples from the summary: dual-task strategies, analogy learning [S].
- **Acclimatisation**: get used to the pressure itself. Examples from the summary: practice under mild anxiety, videotaping, pressure simulation [S].

What the abstract reports [A]:
- Interventions from both choking models, and acclimatisation, generally improved performance under pressure.
- Most often reported as effective: pre-performance routines, quiet eye training, left-hand contractions, acclimatisation training.
- Dual-task: helped when used under pressure, but harmful when built into training.
- Analogy learning: mixed evidence.
- Goal setting, neurofeedback training, reappraisal cues: null effects.

Field-guide reading: this is a count of studies, not a ranking by effect size. We have no per-intervention effect sizes, and we do not know how many of the 47 studies were about basketball or free throws [?]. The machine summary also says the authors recommend a multi-component approach matched to each performer's mechanism. The abstract does not show that, so keep it out of the chapter until the full text is read [?].

## 2. A dose test in basketball: Arthur-Cameselle & Keeler

Arthur-Cameselle & Keeler, *Journal of Clinical Sport Psychology* 19(4):357-374 (per Crossref, prior tick). The local file says 2024 but the issue is 2025, possibly online-first vs issue year. Check before printing the year [?].

Grounding is abstract level. The summary says its source text was only the title, abstract and introduction [S].

- Design: randomized controlled trial of dose at Western Washington University. 46 participants (78% men) with competitive basketball experience [S].
- Pretest day: mindfulness and anxiety surveys, then free throws under low pressure. Participants were matched on that performance and randomly assigned to 6-minute mindfulness training, 15-minute mindfulness training, or control audio [S].
- Test day: assigned audio, then free throws under high pressure [S].
- Results: under high pressure, no group differences in state anxiety, state mindfulness or average free-throw percentage [S].
- One sub-result: only the control group dropped on the second shot under high pressure compared with its low-pressure baseline. The authors say brief training *may* protect against pressure-related drops [S].

Field-guide reading: the headline result is null. The second-shot detail is a sub-result and we have none of its statistics, so do not call it a "second-shot effect". This is an intervention test, not evidence about mechanism. The earlier 15-minute work it builds on is probably Wolch et al. 2021. That paper is requested, not read [?].

## 3. Noise: Galvanovskis 2022

Grounding: [S] only. The paper has two parts.

**League numbers.** The authors compared the five most accurate free-throw teams in seasons with and without spectators: Euroleague 2016-17 through 2020-21, and NBA 2017-18 vs 2019-20 [S].
- Euroleague: top-5 accuracy rose 3.37% from 2016-17 to 2020-21. In 2020-21 all five topped 80%, which the summary says happened only twice in 20 years of league data [S]. It does not say whether 3.37 is percentage points or a relative change [?].
- NBA: all five top teams in 2019-20 beat the top five of 2017-18. Best team: 83.4% vs 81.5% [S]. The summary does not say what share of 2019-20 was played without fans [?].

Limits: top-5 teams only, few seasons, and nothing to separate crowd absence from other year-to-year change. Treat this as a suggestive anecdote, not evidence that crowds lower free-throw accuracy.

**Pilot.** March-April 2021 at the basketball school Ridzene, Latvia. 10 junior female players aged 15-20, mixed skill levels [S].
- At rest: 68.4% [S].
- With fatigue (two full-court sprints every 10 throws): 70.0%. The authors say the smaller throw count may inflate this [S]. Fatigue did not lower accuracy here.
- With noise (5 players shooting while about 20 peers made noise, cheered and distracted): accuracy dropped. The summary gives no number [?].
- Players said the psychological part was harder than the noise itself [S].

The shot counts in the summary do not add up across tasks. Do not quote them [?].

## 4. Fatigue and the wrist: Rusdiana 2020

Rusdiana, A., Ray, H.R.D., Syahid, A.M., & Putra, Y.S.D. (2020). The effect of fatigue on free throw kinematic movement in basketball. 4th International Conference on Sport Science, Health, and Physical Education (ICSSHPE 2019), Atlantis Press. Universitas Pendidikan Indonesia [A].

- Sample: 10 players from the Garuda Bandung academy, aged 15-17 [S].
- Method: high-speed video with Kinovea motion analysis, heart-rate monitoring, and 10 free throws before and 10 after a sprint-based fatigue test. The summary calls the test RAST; we have not checked what that stands for [S].
- Result: of 8 kinematic indicators, only wrist angular velocity was significantly related to the free-throw result. R² = 0.409, p = 0.047 before fatigue; R² = 0.452, p = 0.033 after [S].
- The other 7 indicators were not significant: centre of mass, elbow angle and velocity, wrist angle, release height, ball release angle, upper-arm release angle [S].
- Players kept most indicators steady under fatigue [S].

Our check: those R²/p pairs match a one-predictor regression on 10 data points. The analysis was probably per player (n = 10), so the result is fragile. This is our calculation, not the paper's.

Not in the summary: whether faster wrist velocity went with more or fewer makes, and how much free-throw percentage changed after fatigue. Do not write "faster wrist = better" [?].

What it is not: a pressure study, or a source for central fatigue reducing inhibitory control. That source is still missing.

Lead, not read: Uygur et al. (2010), The effect of fatigue on the kinematics of free throw shooting in basketball, *Journal of Human Kinetics*. Web results say Rusdiana cites it for no fatigue effect on free-throw kinematics [?].

## 5. Where these go in Ch03

- Interventions: Gröpel & Mesagno is the map. Arthur-Cameselle is the basketball dose test, with a null headline.
- Crowds and noise: Galvanovskis as pilot and anecdote. Sors 2019 (2PBTRNY6) studied referees, not shooters, so it goes in a sidebar. Summary pending.
- Fatigue: Rusdiana for kinematics only.
- Kinrade stays in decision making and passing (see hoops/ch03_kinrade_abstract_check.md).

## Sources
- Gröpel & Mesagno: https://doi.org/10.1080/1750984X.2017.1408134 | [Crossref](https://api.crossref.org/works/10.1080/1750984X.2017.1408134) | [LIDA record](https://lida.sport-iat.de/ta/Record/4055257) | [VU record](https://vuir.vu.edu.au/45121/)
- Local summaries: hoops/Gropel - 2019 - Choking interventions in sports A systematic review -- WVVXT7M7 ; hoops/Arthur-Cameselle - 2024 - Effects of Brief Mindfulness Training on Basketball Free-Throw Shooting Performance Under -- SN6FE6IH ; hoops/Agris Galvanovskis - 2022 - Impact of Sound on the Performance of Basketball Free Throw -- 2B7NSKJT ; hoops/Rusdiana - 2020 - The Effect of Fatigue on Free Throw Kinematic Movement in Basketball -- 6REBX2D3
- Rusdiana PDF (not parsed): https://www.atlantis-press.com/article/125934749.pdf | related UPI thesis: [record](https://oalib-perpustakaan.upi.edu/Record/repoupi_38403/Details?print=1)
- Uygur 2010 lead: https://johk.pl/?p=1780
