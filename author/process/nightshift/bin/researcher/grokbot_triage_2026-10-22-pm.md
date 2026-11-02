# Grokbot drop triage: 2026-10-22-pm (researcher, tick r482)

Drop box: `hoops/_grokbot/2026-10-22-pm/` (n=14, pend=14). INDEX.md is Grokbot's file and is left untouched.

**Basis:** the tick payload previews only (about the first 250 characters of 8 of the 14 files). The researcher lane has no file-read tool, so INDEX.md and 6 files are unread. Nothing below goes into chapter text yet.

Tags: A = checked against the primary source, S = summary-level, ? = unverified / outside-agent claim.

## Visible files

### 1. `2026-10-22_nightshift-log.md` (11.7 kB)
- Grokbot says it processed 6 requests from `requests.json` (sha256 `502f50ac…8b26b18ed`, updated 09:24 UTC) and finished around 12:20 Paris time. **?**
- **Mismatch:** the log header has night_id `2026-10-22-overtime`, but the drop box is `2026-10-22-pm`. This is recorded here, not resolved.
- Only researcher-01 and researcher-02 are visible. The other 4 processed requests are either coder items or in the unseen files.
- **Route:** reconcile against `hoops/nightshift_requests.json` and the 11-item pending file. This needs a file read or a human. Blind overwrite is unsafe.

### 2. `2026-10-22_researcher-01_kinematic-variance-x-reinvestment.md` (9.7 kB)
- Request `2026-10-22-overtime-researcher-01` (paper, high). Status: done.
- Headline claim: "nobody has tested this in basketball", meaning Rusdiana-style kinematic variance has not been linked to Kinrade-style reinvestment.
- This is a **negative-existence claim from an outside agent**, so it is tagged **?**.
- **Route:** verify with paperful_ask (sent this tick).
  - If the library confirms it: at most a Ch03 sidebar ("open question").
  - If the library contradicts it: drop it.

### 3. `researcher-02`: NBA FT pressure × workload (data, high)
Files:
- `2026-10-22_researcher-02_ft-pressure-workload-nba.md` (9.4 kB)
- `…_code_1_build_ft.py`, `…_code_2_enrich.py`, `…_code_3_analyze.py`, `…_code_4_robustness_and_proxies.py`
- `2026-10-22_researcher-02_ft_attempts_2015-2024.csv.gz` (12.2 MB)

What the previews show:
- **Source** (from the code_1 docstring): `shufinskiy/nba_data`, a third-party mirror of stats.nba.com play-by-play and shotdetail data, seasons 2015-16 to 2023-24.
- **Size:** the md preview says "about 520k attempts" and that it "tests the Hore → Rusdiana" chain. **?** No results or effect sizes are visible in the previews.
- **Model:** code_4's base formula uses `MADE ~ BASE_LOGIT + SECOND_OF_PAIR + TECHNICAL + C(SEASON) + LATE_CLOSE + CLUTCH + P…` (truncated). Workload comes from `minutes_intervals` (code_2).

Route: **coder `analysis/`. Waiting for coder pickup; not handed off yet.**
- The coder has its own `analysis/_grokbot/2026-10-22-pm/` folder, but it is unconfirmed whether that folder holds these researcher-02 files.
- The researcher cannot write into the coder's root.
- Location for the coder or Glen (factory-relative): `sandbox/researcher/hoops/_grokbot/2026-10-22-pm/2026-10-22_researcher-02_*`
- The researcher quotes **no numbers** from this until the coder has re-run code_1–4 and checked:
  - the LATE_CLOSE / CLUTCH / workload definitions;
  - the attempt count;
  - the data terms of use for book use.
- The researcher thread "game-log pressure × workload → coder" stays open until the coder confirms pickup.

## Unseen (6 files + INDEX.md)
Contents unknown. Not guessed. Open thread.

## Next
- paperful_ask on reinvestment × movement variability (grounds R01). Sent as hr[0].
- Reconcile the REQ list (6 Grokbot-done + 11 pending vs `nightshift_requests.json`). Needs read access or Glen.
