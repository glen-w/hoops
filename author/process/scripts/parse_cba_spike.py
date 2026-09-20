#!/usr/bin/env python3
"""Spike parser: 2023 NBA CBA → derived structure (previews only)."""
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path("/workspace/hoops-cba-spike")
RAW, DERIVED = ROOT / "raw", ROOT / "derived"
PDF = RAW / "2023-NBA-CBA-Final.pdf"
TEXT_PATH = RAW / "text-nolayout.txt"
SOURCE_URL = (
    "https://ak-static.cms.nba.com/wp-content/uploads/sites/4/2024/06/"
    "2023-NBA-Collective-Bargaining-Agreement-Final.pdf"
)
PREVIEW = 500

ARTICLE_HDR = re.compile(r"^ARTICLE ([IVXLC]+)\s*$")
SECTION_HDR = re.compile(r"^Section (\d+)\.\s*(.*)$")
EXHIBIT_HDR = re.compile(r"^EXHIBIT ([A-Z](?:-\d+)?)\s*$")

SALARY_KEYWORDS = [
    (r"salary\s+cap", "salary_cap"),
    (r"basketball\s+related\s+income|\bBRI\b", "bri"),
    (r"luxury\s+tax|\btax\s+level\b", "luxury_tax"),
    (r"apron\s+level|first\s+apron|second\s+apron", "apron"),
    (r"mid-?level\s+salary\s+exception|mid-?level\s+exception", "mid_level_exception"),
    (r"bi-?annual\s+exception", "bi_annual_exception"),
    (r"mid-level\s+salary\s+exception\s+for\s+room|room\s+teams", "room_exception"),
    (r"traded\s+player\s+exception", "traded_player_exception"),
    (r"disabled\s+player\s+exception", "disabled_player_exception"),
    (r"minimum\s+team\s+salary", "minimum_team_salary"),
    (r"escrow", "escrow"),
    (r"designated\s+share", "designated_share"),
]

ROMAN_TO_INT = {r: i for i, r in enumerate([
    "I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII","XIII","XIV","XV",
    "XVI","XVII","XVIII","XIX","XX","XXI","XXII","XXIII","XXIV","XXV","XXVI","XXVII",
    "XXVIII","XXIX","XXX","XXXI","XXXII","XXXIII","XXXIV","XXXV","XXXVI","XXXVII",
    "XXXVIII","XXXIX","XL","XLI","XLII"], 1)}


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return "sha256:" + h.hexdigest()


def sha256_text(t: str) -> str:
    t = t.replace("\r\n", "\n").replace("\r", "\n")
    if not t.endswith("\n"):
        t += "\n"
    return "sha256:" + hashlib.sha256(t.encode()).hexdigest()


def preview(t: str, n: int = PREVIEW) -> str:
    t = re.sub(r"\s+", " ", t).strip()
    return t if len(t) <= n else t[:n] + "…"


def is_running_header(s: str) -> bool:
    return bool(re.fullmatch(r"Article [IVXLC]+", s) or re.fullmatch(r"\d+", s))


def is_true_section_header(s: str, prev_nonempty: str = "") -> bool:
    if s.startswith("Sections "):
        return False
    m = SECTION_HDR.match(s)
    if not m:
        return False
    if re.match(r"^Section \d+\(", s):
        return False
    rest = (m.group(2) or "").strip()
    if rest:
        if rest[0].islower() or rest[0] == "(":
            return False
        if rest.startswith(("or ", "above", "below", "of ", "to ", "and ")):
            return False
    pl = prev_nonempty.rstrip()
    if pl and not pl.endswith((".", ":", ";")) and not is_running_header(pl) and len(pl) > 20:
        if re.search(r"(Article [IVXLC]+,?|Sections?)$", pl) or pl.endswith(","):
            return False
    return True


def find_body_start(lines: list[str]) -> int:
    for i, line in enumerate(lines):
        if line.strip() == "ARTICLE I":
            return i
    raise RuntimeError("body ARTICLE I not found")


def collect_title(lines: list[str], start: int) -> tuple[str, int]:
    title_parts: list[str] = []
    i = start
    while i < len(lines) and len(title_parts) < 8:
        s = lines[i].strip()
        if not s or is_running_header(s):
            i += 1
            if title_parts and not s:
                break
            continue
        if is_true_section_header(s) or ARTICLE_HDR.match(s) or EXHIBIT_HDR.match(s):
            break
        letters = [c for c in s if c.isalpha()]
        upper_ratio = (sum(c.isupper() for c in letters) / len(letters)) if letters else 0
        if len(s) > 100 and upper_ratio < 0.6:
            break
        if s[0].islower() and title_parts:
            break
        if title_parts and upper_ratio < 0.5 and len(s) > 40:
            break
        title_parts.append(s)
        i += 1
    return " ".join(title_parts), i


def split_sections(body_lines: list[str], article_roman: str) -> list[dict]:
    candidates = []
    prev = ""
    for i, line in enumerate(body_lines):
        s = line.strip()
        if not s:
            continue
        if is_true_section_header(s, prev):
            m = SECTION_HDR.match(s)
            candidates.append((i, int(m.group(1)), m.group(1), (m.group(2) or "").strip().rstrip(".")))
        if not is_running_header(s):
            prev = s

    kept, last_n, seen = [], 0, set()
    for item in candidates:
        n = item[1]
        if n <= last_n or n in seen:
            continue
        if last_n == 0 and n != 1 and n > 3:
            continue
        kept.append(item)
        seen.add(n)
        last_n = n

    sections = []
    for j, (idx, _ni, num, inline_title) in enumerate(kept):
        end = kept[j + 1][0] if j + 1 < len(kept) else len(body_lines)
        title = inline_title
        if not title:
            k = idx + 1
            while k < end:
                s = body_lines[k].strip()
                if not s or is_running_header(s):
                    k += 1
                    continue
                if is_true_section_header(s) or ARTICLE_HDR.match(s):
                    break
                if s.startswith("(") and not re.match(r"^\([a-z]\)\s+[A-Z]", s):
                    break
                title = s.rstrip(".")
                break
        if title and title.startswith("(") and not re.match(r"^\([a-z]\)\s", title):
            title = None
        chunk = "\n".join(body_lines[idx:end])
        sections.append({
            "id": f"cba:2023:art-{article_roman}:sec-{num}",
            "number": num,
            "title": title or None,
            "char_len": len(chunk),
            "text_preview": preview(chunk),
        })
    return sections


def parse_articles(lines: list[str], body_start: int):
    art_indices = []
    for i in range(body_start, len(lines)):
        m = ARTICLE_HDR.match(lines[i].strip())
        if m:
            art_indices.append((i, m.group(1)))
    exhibit_start = len(lines)
    for i in range(art_indices[-1][0] + 10, len(lines)):
        if lines[i].strip() == "EXHIBIT A":
            exhibit_start = i
            break
    articles = []
    for j, (idx, roman) in enumerate(art_indices):
        next_idx = art_indices[j + 1][0] if j + 1 < len(art_indices) else exhibit_start
        title, _ = collect_title(lines, idx + 1)
        body_lines = lines[idx:next_idx]
        sections = split_sections(body_lines, roman)
        chunk = "\n".join(body_lines)
        articles.append({
            "id": f"cba:2023:art-{roman}",
            "number": roman,
            "number_arabic": ROMAN_TO_INT.get(roman),
            "title": title or None,
            "label": f"ARTICLE {roman}" + (f" {title}" if title else ""),
            "line_start": idx + 1,
            "line_end_exclusive": next_idx + 1 if next_idx < len(lines) else len(lines) + 1,
            "section_count": len(sections),
            "sections": sections,
            "char_len": len(chunk),
            "text_preview": preview(chunk),
        })
    return articles, exhibit_start


def parse_exhibits(lines, exhibit_start):
    indices = []
    for i in range(exhibit_start, len(lines)):
        m = EXHIBIT_HDR.match(lines[i].strip())
        if m:
            indices.append((i, m.group(1)))
    out = []
    for j, (idx, code) in enumerate(indices):
        end = indices[j + 1][0] if j + 1 < len(indices) else len(lines)
        title, _ = collect_title(lines, idx + 1)
        chunk = "\n".join(lines[idx:end])
        out.append({
            "id": f"cba:2023:ex-{code}",
            "number": code,
            "title": title or None,
            "label": f"EXHIBIT {code}" + (f" {title}" if title else ""),
            "line_start": idx + 1,
            "char_len": len(chunk),
            "text_preview": preview(chunk),
        })
    return out


def extract_defined_terms(art_i_text: str) -> list[dict]:
    fixed = re.sub(r"\(([a-z])\)\s*\n\s*[\"“]", r'(\1) "', art_i_text)
    fixed = re.sub(r'([\"”\"])\s*\n\s*(means\b)', r"\1 \2", fixed, flags=re.I)
    # curly/smart quotes mixed with straight
    fixed = fixed.replace("”", '"').replace("“", '"')
    pat = re.compile(
        r'\(([a-z])\)\s*"([^"\n]{1,120})"\s*(?:or\s*"([^"\n]{1,80})")?\s*means\b',
        re.I,
    )
    terms, seen = [], set()
    for m in pat.finditer(fixed):
        letter, term, alt = m.group(1), m.group(2).strip(), m.group(3)
        key = term.lower()
        if key in seen:
            continue
        seen.add(key)
        terms.append({
            "term": term,
            "alt": alt.strip() if alt else None,
            "article": "I",
            "locator": f"cba:2023:art-I:sec-1:({letter})",
            "definition_preview": preview(fixed[m.start():m.start() + 500], 400),
            "review_status": "unreviewed",
        })
    # Fallback: lines where quote-means survived wraps poorly — scan for "Term" means
    pat2 = re.compile(r'"([^"\n]{2,80})"\s*(?:or\s*"([^"\n]{1,60})")?\s*means\b', re.I)
    for m in pat2.finditer(fixed):
        term, alt = m.group(1).strip(), m.group(2)
        key = term.lower()
        if key in seen or not term[0].isupper():
            continue
        # skip if looks like mid-sentence
        if term.lower() in {"the", "a", "an"}:
            continue
        seen.add(key)
        terms.append({
            "term": term,
            "alt": alt.strip() if alt else None,
            "article": "I",
            "locator": "cba:2023:art-I:sec-1",
            "definition_preview": preview(fixed[m.start():m.start() + 500], 400),
            "review_status": "unreviewed",
        })
    terms.sort(key=lambda x: x["term"].lower())
    return terms


def extract_exceptions_sec6(vii_text: str) -> list[dict]:
    m6 = re.search(r"^Section 6\.\s*$", vii_text, re.M)
    m7 = re.search(r"^Section 7\.\s*$", vii_text, re.M)
    if not m6:
        return []
    end = m7.start() if m7 else len(vii_text)
    sec6 = vii_text[m6.start():end]
    # light wrap join for titles
    sec6_j = re.sub(r"\n(?=[a-z])", " ", sec6)
    out, seen = [], set()
    for m in re.finditer(
        r"\(([a-z])\)\s+((?:Non-Taxpayer |Taxpayer )?Mid-Level Salary Exception(?: for Room Teams)?"
        r"|[A-Z][^.\n]{0,80}Exception)\.",
        sec6_j,
    ):
        label = m.group(2).strip()
        # skip nested (i)/(ii) under Traded Player if label is Standard/Aggregate subtype — keep them
        key = label.lower()
        if key in seen:
            continue
        # Avoid re-matching Second Round Pick at wrong letter if duplicate
        seen.add(key)
        ll = label.lower()
        tags = []
        if "mid-level" in ll:
            tags.append("mid_level_exception")
        if "bi-annual" in ll:
            tags.append("bi_annual_exception")
        if "traded player" in ll or "standard traded" in ll or "aggregate traded" in ll:
            tags.append("traded_player_exception")
        if "disabled" in ll:
            tags.append("disabled_player_exception")
        if "room" in ll and "mid-level" in ll:
            tags.append("room_exception")
        if not tags:
            tags.append("exception")
        out.append({
            "letter": m.group(1),
            "label": label,
            "locator": f"cba:2023:art-VII:sec-6:({m.group(1)})",
            "preview": preview(sec6_j[m.start():m.start() + 400], 300),
            "tags": tags,
            "review_status": "unreviewed",
        })
    return out


def build_headings_index(articles, exhibits, exceptions):
    hits, units = [], []
    for a in articles:
        units.append(("article", a["id"], a.get("label") or a["id"], a.get("title") or ""))
        for s in a.get("sections") or []:
            units.append((
                "section",
                s["id"],
                f"{a['id']} §{s['number']} {s.get('title') or ''}".strip(),
                f"{s.get('title') or ''} {s.get('text_preview') or ''}",
            ))
    for e in exhibits:
        units.append(("exhibit", e["id"], e.get("label") or e["id"], e.get("title") or ""))
    for unit_type, uid, label, hay in units:
        matched = [tag for pat, tag in SALARY_KEYWORDS if re.search(pat, hay, re.I)]
        if matched:
            hits.append({
                "id": uid,
                "unit_type": unit_type,
                "label": label.strip(),
                "tags": sorted(set(matched)),
                "review_status": "unreviewed",
            })
    for e in exceptions:
        hits.append({
            "id": e["locator"],
            "unit_type": "subsection",
            "label": e["label"],
            "tags": e["tags"],
            "review_status": "unreviewed",
        })
    return hits


def main() -> None:
    text = TEXT_PATH.read_text(encoding="utf-8", errors="replace")
    lines = [ln.replace("\x0c", "") for ln in text.splitlines()]
    body_start = find_body_start(lines)
    articles, exhibit_start = parse_articles(lines, body_start)
    exhibits = parse_exhibits(lines, exhibit_start)

    art_i = next(a for a in articles if a["number"] == "I")
    art_vii = next(a for a in articles if a["number"] == "VII")
    # line_start is 1-based; slice end is line_start of next article (1-based) → index next-1
    art_i_text = "\n".join(lines[art_i["line_start"] - 1 : articles[1]["line_start"] - 1])
    art_vii_text = "\n".join(
        lines[art_vii["line_start"] - 1 : next(a for a in articles if a["number"] == "VIII")["line_start"] - 1]
    )

    defined_terms = extract_defined_terms(art_i_text)
    exceptions = extract_exceptions_sec6(art_vii_text)
    headings_index = build_headings_index(articles, exhibits, exceptions)
    focus = {"salary_cap", "bri", "luxury_tax", "apron", "mid_level_exception"}
    salary_cap_index = [h for h in headings_index if focus.intersection(h["tags"])]

    pdf_sha = sha256_file(PDF)
    text_sha = sha256_text(text)
    retrieved = datetime.now(ZoneInfo("Europe/Paris")).isoformat()

    toc_expected = {"I": 1, "II": 15, "VII": 12, "X": 10, "XI": 5}
    validation = {
        "toc_expected_sample": toc_expected,
        "parsed_vs_expected": {
            r: {
                "expected": exp,
                "parsed": next(a for a in articles if a["number"] == r)["section_count"],
                "ok": next(a for a in articles if a["number"] == r)["section_count"] == exp,
            }
            for r, exp in toc_expected.items()
        },
        "article_i_bounds": {
            "line_start": art_i["line_start"],
            "next_article_line": articles[1]["line_start"],
            "next_article": articles[1]["number"],
        },
    }

    structure = {
        "_derived": True,
        "_disclaimer": (
            "Derived structure from official NBA/NBPA CBA PDF for local tooling only. "
            "Not authoritative. Previews truncated; full text stays under raw/ only."
        ),
        "edition_id": "2023",
        "source_url": SOURCE_URL,
        "retrieval_date": retrieved,
        "extractor": {
            "primary": "pdftotext",
            "pdftotext_version": "25.03.0",
            "flags": "default (no -layout) → raw/text-nolayout.txt",
            "layout_variant": "raw/text.txt via pdftotext -layout",
            "pymupdf": None,
            "note": "pymupdf not installed on spike box; poppler is corpus-primary",
        },
        "source_pdf_sha256": pdf_sha,
        "source_text_sha256": text_sha,
        "pdf_pages": 686,
        "pdf_bytes": PDF.stat().st_size,
        "body_line_start": body_start + 1,
        "unit_type": "article",
        "article_count": len(articles),
        "exhibit_count": len(exhibits),
        "section_count_total": sum(a["section_count"] for a in articles),
        "validation_sample": validation,
        "articles": articles,
        "exhibits": exhibits,
        "preview_chars": PREVIEW,
        "rights_note": (
            "NBA/NBPA Collective Bargaining Agreement is copyrighted. "
            "Do NOT commit the full PDF or full extracted text to a public git repo. "
            "Safe to commit: structure metadata, clause IDs, hashes, short previews."
        ),
    }

    defined = {
        "_derived": True,
        "_disclaimer": "Locator-first defined-term index from Article I; bodies truncated.",
        "edition_id": "2023",
        "source_pdf_sha256": pdf_sha,
        "term_count": len(defined_terms),
        "defined_terms": defined_terms,
        "review_status": "unreviewed",
        "notes": [
            "PDF wraps often split '(a)' and '\"Term\" means' across lines; parser joins those.",
            "Operational Mid-Level / Tax Level / Apron definitions live in Article VII, not Article I.",
            "Art I includes a generic defined term 'Exception' pointing at VII constructs.",
        ],
    }

    headings = {
        "_derived": True,
        "_disclaimer": "Rule-based heading/tag index + Art VII §6 Exception subsections; unreviewed.",
        "edition_id": "2023",
        "source_pdf_sha256": pdf_sha,
        "keyword_rules": [{"pattern": p, "tag": t} for p, t in SALARY_KEYWORDS],
        "exception_subsection_heads": exceptions,
        "headings_index": headings_index,
        "salary_cap_index": salary_cap_index,
        "review_status": "unreviewed",
    }

    DERIVED.mkdir(parents=True, exist_ok=True)
    (DERIVED / "structure.json").write_text(json.dumps(structure, indent=2, ensure_ascii=False) + "\n")
    (DERIVED / "defined_terms.json").write_text(json.dumps(defined, indent=2, ensure_ascii=False) + "\n")
    (DERIVED / "headings_index.json").write_text(json.dumps(headings, indent=2, ensure_ascii=False) + "\n")
    (RAW / "metadata.json").write_text(json.dumps({
        "edition_id": "2023",
        "label": "2023 NBA Collective Bargaining Agreement Final",
        "source_url": SOURCE_URL,
        "retrieval_date": retrieved,
        "original_sha256": pdf_sha,
        "text_sha256": text_sha,
        "text_fidelity": "extracted_unverified",
        "extractor": "pdftotext 25.03.0 (no -layout)",
        "pdf_bytes": PDF.stat().st_size,
        "pdf_pages": 686,
        "http_status_on_fetch": 200,
        "rights_note": "Not redistributed; local raw only. Copyright NBA/NBPA.",
    }, indent=2, ensure_ascii=False) + "\n")

    print("body_start", body_start + 1)
    print("Art I", art_i["line_start"], "→", articles[1]["line_start"], articles[1]["number"])
    print("articles", len(articles), "exhibits", len(exhibits), "sections", structure["section_count_total"])
    print("defined_terms", len(defined_terms), "exceptions", len(exceptions), "salary_idx", len(salary_cap_index))
    print("validation", validation["parsed_vs_expected"])
    print("MLE:", [e["label"] for e in exceptions if "mid_level_exception" in e["tags"]])
    print("terms sample:", [t["term"] for t in defined_terms[:12]])
    print("term count detail: lettered locators", sum(1 for t in defined_terms if ":(" in t["locator"]))


if __name__ == "__main__":
    main()
