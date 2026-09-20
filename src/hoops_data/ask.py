"""One lookup for the Hoops sidecar.

Usage:
    hoops ask "home court 2024"
    hoops ask "Article VII"
    python scripts/hoops_ask.py "Boston Celtics"
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


@dataclass
class Hit:
    kind: str
    title: str
    status: str
    confidence: str
    artifact: str
    sentence: str
    score: int


_GAP = re.compile(r"\bGAP\b|NOT_FOUND", re.I)
_LEVEL = re.compile(r"\b(HIGH|MEDIUM|LOW)\b")
_RANK = {"gap": 0, "low": 1, "medium": 2, "high": 3}


def _claim_sentence(row: dict) -> str:
    notes = (row.get("resolution_notes") or "").strip()
    action = (row.get("next_action") or "").strip()
    if _GAP.search(notes):
        return notes
    return action or notes


def _claim_confidence(row: dict) -> str:
    notes = row.get("resolution_notes") or ""
    mention = row.get("mention") or ""
    if _GAP.search(notes) or _GAP.search(mention):
        return "GAP"
    if row.get("status") == "hold":
        return "hold"
    found = _LEVEL.search(notes)
    return found.group(1) if found else "unrated"


def _weakest(values: list[str]) -> str:
    cleaned = [value.strip() for value in values if value and value.strip()]
    if not cleaned:
        return "unrated"
    return min(cleaned, key=lambda value: _RANK.get(value.lower(), 1))


def _norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def _score(query: str, *parts: str) -> int:
    q = _norm(query)
    if not q:
        return 0
    blob = _norm(" ".join(p for p in parts if p))
    if q in blob:
        return 100
    tokens = [tok for tok in q.split() if len(tok) > 2]
    if not tokens:
        return 0
    hits = sum(1 for tok in tokens if tok in blob)
    return int(80 * hits / len(tokens)) if hits else 0


def _mentions(root: Path, query: str) -> list[Hit]:
    path = root / "data" / "mentions.csv"
    if not path.exists():
        return []
    hits = []
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            score = _score(query, row.get("section", ""), row.get("mention", ""), row.get("resolution_notes", ""))
            if score < 50:
                continue
            hits.append(Hit(
                kind="claim",
                title=row.get("section", ""),
                status=row.get("status", ""),
                confidence=_claim_confidence(row),
                artifact=row.get("source", ""),
                sentence=_claim_sentence(row),
                score=score,
            ))
    return hits


def _teams(root: Path, query: str) -> list[Hit]:
    path = root / "data" / "derived" / "teams" / "teams.csv"
    if not path.exists():
        return []
    hits = []
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            score = _score(query, row.get("name", ""), row.get("abbr", ""), row.get("team_id", ""), row.get("league_id", ""))
            if score < 80:
                continue
            hits.append(Hit(
                kind="team",
                title=f"{row.get('name', '')} ({row.get('league_id', '')})",
                status="ready",
                confidence=row.get("confidence") or "unrated",
                artifact=str(path.relative_to(root)),
                sentence=(
                    f"{row.get('name')} is in {row.get('league_id')}. "
                    f"Wikidata {row.get('wikidata_qid') or 'GAP'}. "
                    "Colors and logos may still be blank."
                ),
                score=score,
            ))
    return hits


def _orgs(root: Path, query: str) -> list[Hit]:
    folder = root / "data" / "derived" / "nba_orgs"
    hits = []
    for path in sorted(folder.glob("*.csv")):
        slug = path.stem.replace("-", " ")
        score = _score(query, slug, path.name)
        if score < 80:
            continue
        with path.open(encoding="utf-8", newline="") as handle:
            levels = [row.get("confidence", "") for row in csv.DictReader(handle)]
        hits.append(Hit(
            kind="org",
            title=slug,
            status="ready",
            confidence=_weakest(levels),
            artifact=str(path.relative_to(root)),
            sentence=f"Weakest row in this chart is {_weakest(levels)}. Cite a name only at its own row's confidence.",
            score=score,
        ))
    return hits


def _cba(root: Path, query: str) -> list[Hit]:
    score = _score(query, "cba article vii salary cap mid-level exception defined terms")
    if score < 50 and "article" not in query.lower() and "cba" not in query.lower():
        return []
    structure = root / "data" / "cba" / "2023" / "derived" / "structure.json"
    return [Hit(
        kind="cba",
        title="2023 CBA structure lookup",
        status="ready; quotes_need_pdf",
        confidence="quotes_blocked",
        artifact=str(structure.relative_to(root)) if structure.exists() else "docs/CBA-LOOKUP.md",
        sentence="Lookup of clause ids is ready. Verbatim quotes still need the local PDF. Try: python scripts/cba_lookup.py \"Article VII\"",
        score=max(score, 60),
    )]


def _chapter(root: Path, query: str) -> list[Hit]:
    path = root / "docs" / "CHAPTER-MAP.md"
    if not path.exists():
        return []
    hits = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or line.startswith("| Binder") or line.startswith("|---"):
            continue
        cells = [cell.strip().strip("`") for cell in line.strip("|").split("|")]
        if len(cells) < 4:
            continue
        score = _score(query, cells[0], cells[1])
        if score < 60:
            continue
        hits.append(Hit(
            kind="map",
            title=cells[0],
            status=cells[3],
            confidence="unrated",
            artifact=cells[1],
            sentence="Mapped in docs/CHAPTER-MAP.md. Prefer the artifact over the status word.",
            score=score,
        ))
    return hits


def search(query: str, root: Path | None = None) -> list[Hit]:
    root = root or repo_root()
    hits = []
    hits.extend(_mentions(root, query))
    hits.extend(_teams(root, query))
    hits.extend(_orgs(root, query))
    hits.extend(_cba(root, query))
    hits.extend(_chapter(root, query))
    hits.sort(key=lambda hit: hit.score, reverse=True)
    # Drop weaker duplicates of the same artifact.
    seen = set()
    unique = []
    for hit in hits:
        key = (hit.kind, hit.artifact, hit.title)
        if key in seen:
            continue
        seen.add(key)
        unique.append(hit)
    return unique[:5]


def format_hits(query: str, hits: list[Hit]) -> str:
    if not hits:
        return (
            f"query: {query}\n"
            "status: missing\n"
            "confidence: GAP\n"
            "safe_sentence: No desk row matched. Do not invent the number.\n"
        )
    blocks = [f"query: {query}"]
    for hit in hits:
        blocks.append(
            "\n".join([
                f"kind: {hit.kind}",
                f"title: {hit.title}",
                f"status: {hit.status}",
                f"confidence: {hit.confidence}",
                f"artifact: {hit.artifact}",
                f"safe_sentence: {hit.sentence}",
            ])
        )
    return "\n\n".join(blocks) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Look up a Hoops sidecar desk row.")
    parser.add_argument("query", nargs="*", help="Binder path, team, or short question")
    args = parser.parse_args(argv)
    query = " ".join(args.query).strip()
    if not query:
        parser.print_help()
        return 2
    sys.stdout.write(format_hits(query, search(query)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
