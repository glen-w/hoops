# Spike report: 2017 NBA CBA parse (extension)

**Access / run date:** 2026-09-19 (Europe/Paris, UTC+2)  
**Parent:** `SPIKE-REPORT.md` (2023) · Feasibility: `/workspace/hoops-cba-parser-feasibility-2026-09-19.md`  
**Compare:** `derived/COMPARE-2017-2023.md`  
**Spike root:** `/workspace/hoops-cba-spike/`

---

## 1. What we did

| Step | Result |
|------|--------|
| Download official 2017 PDF | **HTTP 200** from NBA ak-static |
| Size | **2 176 412** bytes (matches feasibility table) |
| SHA-256 | `sha256:66d620ebf682e2ffc55698394fb4635d738bf0e0250aad34f9cc137a25bf051a` |
| Extract | **pdftotext 25.03.0**; `text.txt` (`-layout`) + `text-nolayout.txt` under `raw/2017/` |
| Structure | Prefer **layout** text for 2017 headers (see §4) |
| Derived | `derived/2017/{structure,defined_terms,headings_index}.json` — previews ≤500 chars |

**Source URL:**  
`https://ak-static.cms.nba.com/wp-content/uploads/sites/4/2017/10/2017-NBA-Collective-Bargaining-Agreement.pdf`

**Not used this pass:** NBPA imgix twin (feasibility size 2 186 284 — hash whichever edition you ingest).

---

## 2. Artifact layout (2017 addition)

```
hoops-cba-spike/
  SPIKE-REPORT.md
  SPIKE-2017.md                 ← this file
  scripts/parse_cba_spike.py    ← --edition {2017,2023}
  raw/2017/                     ← LOCAL ONLY (gitignored PDF + text)
    2017-NBA-CBA.pdf
    text.txt / text-nolayout.txt
    metadata.json / original.sha256
  derived/2017/                 ← structure + short previews only
    structure.json
    defined_terms.json
    headings_index.json
  derived/COMPARE-2017-2023.md
```

---

## 3. Numbers (2017)

| Metric | Value |
|--------|------:|
| HTTP | 200 |
| PDF bytes | 2 176 412 |
| PDF pages | 633 |
| Articles | **42** (I–XLII) |
| Exhibits | **19** |
| Sections parsed | **257** |
| Defined terms (spike) | 83 |
| Salary-cap index hits | 28 |
| Art VII §6 exception heads | 9 (MLE ×3 at e/f/g) |
| TOC sample I/II/VII/X/XI | all OK |

**Article VII title:**  
`BASKETBALL RELATED INCOME, SALARY CAP, MINIMUM TEAM SALARY, AND ESCROW ARRANGEMENT`

**MLE:** still **Art VII §6 (e)(f)(g)** — same letters as 2023.

Stable ID shape: `cba:2017:art-VII:sec-6` (and lettered children).

---

## 4. 2017-specific hazard

**No-layout running header on p.200:** a bare `Section 6.` is injected into the middle of VII §5(e)(4)(ii), so a naive no-layout split assigns the Exceptions body a prose title (“From February 1…”).  
**Mitigation:** parse structure from **`pdftotext -layout`** for 2017 (`structure_from: layout`). 2023 remains no-layout (279-section golden).

Other hazards (form-feed/`splitlines`, cross-ref `Section N.`, copyright) match `SPIKE-REPORT.md` §4.

---

## 5. Copyright

Same rule as 2023: **do not commit** PDF or full `text*.txt`. Derived JSON = metadata + clause IDs + ≤500-char previews only.

---

## 6. Parser

```bash
python3 scripts/parse_cba_spike.py --edition 2017
python3 scripts/parse_cba_spike.py --edition 2023
```

*End of 2017 spike note.*
