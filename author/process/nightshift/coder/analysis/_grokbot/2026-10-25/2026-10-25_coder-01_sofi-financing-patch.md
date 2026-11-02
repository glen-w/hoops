# SoFi Stadium financing row: patch note

**Request:** 2026-10-24-pm-coder-01 · **Status:** done (medium confidence) · Grok Bot nightshift, 25 Oct 2026 (Europe/Paris)

**File:** `2026-10-25_coder-01_sofi-financing-patch.csv`. It has one row with the same header as `prior/2026-10-23_researcher-05_arena_financing.csv` and replaces that file's SoFi row (line 11, "not found"). The prior CSV was not changed. To apply it, swap the SoFi row by `arena` key.

## What changed
| Field | 23 Oct | Patch | Source [Zotero] | Confidence |
|---|---|---|---|---|
| Cost | not found | "at least $5B"; earlier estimates were $1.86B, then $2.6B, then $4B+ (2018), then $5B | LA Times, Fenno, 4 Sep 2020 [9WIBUSNC]; StadiumDB, 18 May 2018 [CK6QA3NX] | medium (reported estimate, not audited) |
| Public money | "privately financed (not verified)" | No direct public capital. The developer fronted ~$400M of public infrastructure, to be repaid from the city's development-tax revenue above $25M/yr; the city had paid ~$20M | LAist, 12 Sep 2026 [4K63E2MT]; LA Local, 17 Sep 2026 [45XCU55W] | medium |
| Legal status | n/a | A court ruled the 2015 development agreement void on 1 Sep 2026. An appeal is possible, so the reimbursement terms are now in doubt | same | medium (read the ruling before citing) |
| Instruments | not found | Kroenke equity ~$1.6B; $2.25B construction loan from nine banks (2018); NFL owners approved $500M more borrowing (May 2020); Chargers: $200M NFL G-4 loan, rent of $1/yr; naming rights $625M for 2020–40 | StadiumDB citing SBJ (paywalled) [CK6QA3NX]; LA Times 2020 [9WIBUSNC] | medium |

## Caveats
- The parts don't add up: $1.6B + $2.25B + $0.5B = $4.35B, against "at least $5B". I couldn't find the rest (land, Hollywood Park district costs, later draws). I didn't invent a figure to fill the gap.
- The loan sizes come from SBJ via StadiumDB. The SBJ original is paywalled and I didn't read it.
- LA Local is funded by the Ballmer Group. Ballmer owns the Clippers and Intuit Dome, a neighbouring competitor, so that's a possible interest. LAist corroborates the main facts.
- The public share is left as "0 (direct)". An indirect share (forgone or redirected tax) can't be computed from public sources.
- The Zotero items for this row are in hoops/other sports (RNWE7I8B).
