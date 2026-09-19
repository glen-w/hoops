#!/usr/bin/env python3
"""
Build NBA CBA structure metadata from local PDF.

Extracts article/section/exhibit hierarchy from an NBA Collective Bargaining
Agreement PDF and emits structure.json with metadata only (no fulltext committed).

Usage:
    python scripts/cba/build_cba_structure.py --edition 2023 --pdf data/raw/cba/2023/cba.pdf
    python scripts/cba/build_cba_structure.py --edition 2017 --pdf data/raw/cba/2017/cba.pdf
"""

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional

try:
    import pymupdf as fitz
except ImportError:
    print("Error: pymupdf not installed. Run: pip install pymupdf", file=sys.stderr)
    sys.exit(1)


@dataclass
class StructuralUnit:
    """A structural unit in the CBA (article, section, exhibit)."""
    id: str
    type: str
    title: str
    parent_id: Optional[str] = None
    page_start: Optional[int] = None
    page_end: Optional[int] = None
    char_offset_start: Optional[int] = None
    char_offset_end: Optional[int] = None
    text_sha256: Optional[str] = None

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "title": self.title,
            "parent_id": self.parent_id,
            "page_start": self.page_start,
            "page_end": self.page_end,
            "char_offset_start": self.char_offset_start,
            "char_offset_end": self.char_offset_end,
            "text_sha256": self.text_sha256,
        }


class CBAParser:
    """Parse NBA CBA PDF structure."""

    # Regex patterns for CBA structural markers
    ARTICLE_PATTERN = re.compile(
        r"^ARTICLE\s+([IVXLCDM]+)(?:\s*[:\-\.\s]+(.+))?$",
        re.IGNORECASE | re.MULTILINE
    )
    SECTION_PATTERN = re.compile(
        r"^Section\s+(\d+)(?:\.|\s*[:\-]+\s*)(.+)?$",
        re.IGNORECASE | re.MULTILINE
    )
    EXHIBIT_PATTERN = re.compile(
        r"^EXHIBIT\s+([A-Z\d]+)(?:\s*[:\-\.\s]+(.+))?$",
        re.IGNORECASE | re.MULTILINE
    )

    def __init__(self, pdf_path: Path):
        self.pdf_path = pdf_path
        self.doc = None
        self.fulltext = ""
        self.page_map = []  # [(page_num, char_start, char_end)]

    def extract_text(self) -> str:
        """Extract fulltext from PDF with page tracking."""
        self.doc = fitz.open(str(self.pdf_path))
        text_parts = []
        char_offset = 0

        for page_num, page in enumerate(self.doc, start=1):
            page_text = page.get_text()
            text_parts.append(page_text)
            page_start = char_offset
            char_offset += len(page_text)
            self.page_map.append((page_num, page_start, char_offset))

        self.fulltext = "".join(text_parts)
        return self.fulltext

    def compute_sha256(self, text: str) -> str:
        """Compute SHA-256 hash of text."""
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    def parse_structure(self) -> List[StructuralUnit]:
        """Parse CBA structure from extracted text."""
        units = []
        current_article = None

        # Find all articles
        for match in self.ARTICLE_PATTERN.finditer(self.fulltext):
            article_num = match.group(1)
            article_title = match.group(2).strip() if match.group(2) else ""
            article_id = f"article_{self._roman_to_int(article_num)}"
            
            page_num = self._char_offset_to_page(match.start())
            
            unit = StructuralUnit(
                id=article_id,
                type="article",
                title=f"Article {article_num}: {article_title}"[:200],  # Truncate long titles
                parent_id=None,
                page_start=page_num,
                char_offset_start=match.start(),
            )
            units.append(unit)
            current_article = unit

        # Find all sections
        for match in self.SECTION_PATTERN.finditer(self.fulltext):
            section_num = match.group(1)
            section_title = match.group(2).strip() if match.group(2) else ""
            
            # Find parent article by looking backwards
            parent_article = self._find_parent_article(units, match.start())
            parent_id = parent_article.id if parent_article else None
            
            section_id = f"section_{section_num}"
            if parent_id:
                section_id = f"{parent_id}_section_{section_num}"
            
            page_num = self._char_offset_to_page(match.start())
            
            unit = StructuralUnit(
                id=section_id,
                type="section",
                title=f"Section {section_num}: {section_title}"[:200],
                parent_id=parent_id,
                page_start=page_num,
                char_offset_start=match.start(),
            )
            units.append(unit)

        # Find all exhibits
        for match in self.EXHIBIT_PATTERN.finditer(self.fulltext):
            exhibit_id_raw = match.group(1)
            exhibit_title = match.group(2).strip() if match.group(2) else ""
            exhibit_id = f"exhibit_{exhibit_id_raw.lower()}"
            
            page_num = self._char_offset_to_page(match.start())
            
            unit = StructuralUnit(
                id=exhibit_id,
                type="exhibit",
                title=f"Exhibit {exhibit_id_raw}: {exhibit_title}"[:200],
                parent_id=None,
                page_start=page_num,
                char_offset_start=match.start(),
            )
            units.append(unit)

        # Compute end positions and text hashes
        units = sorted(units, key=lambda u: u.char_offset_start or 0)
        for i, unit in enumerate(units):
            if i < len(units) - 1:
                unit.char_offset_end = units[i + 1].char_offset_start
                unit.page_end = self._char_offset_to_page(unit.char_offset_end - 1)
            else:
                unit.char_offset_end = len(self.fulltext)
                unit.page_end = self.page_map[-1][0] if self.page_map else None
            
            # Compute hash of unit's text content
            if unit.char_offset_start is not None and unit.char_offset_end is not None:
                unit_text = self.fulltext[unit.char_offset_start:unit.char_offset_end]
                unit.text_sha256 = self.compute_sha256(unit_text)

        return units

    def _char_offset_to_page(self, offset: int) -> Optional[int]:
        """Convert character offset to page number."""
        for page_num, start, end in self.page_map:
            if start <= offset < end:
                return page_num
        return None

    def _find_parent_article(self, units: List[StructuralUnit], char_offset: int) -> Optional[StructuralUnit]:
        """Find the most recent article before the given offset."""
        articles = [u for u in units if u.type == "article" and (u.char_offset_start or 0) < char_offset]
        return articles[-1] if articles else None

    @staticmethod
    def _roman_to_int(roman: str) -> int:
        """Convert Roman numeral to integer."""
        roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        prev_value = 0
        for char in reversed(roman.upper()):
            value = roman_values.get(char, 0)
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result


def main():
    parser = argparse.ArgumentParser(
        description="Extract NBA CBA structure metadata from PDF"
    )
    parser.add_argument(
        "--edition",
        required=True,
        choices=["2017", "2023"],
        help="CBA edition year"
    )
    parser.add_argument(
        "--pdf",
        required=True,
        type=Path,
        help="Path to CBA PDF file"
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output path for structure.json (default: data/derived/cba/{edition}/structure.json)"
    )
    parser.add_argument(
        "--source-url",
        default="https://nbpa.com/cba",
        help="Official source URL"
    )

    args = parser.parse_args()

    if not args.pdf.exists():
        print(f"Error: PDF not found: {args.pdf}", file=sys.stderr)
        print(f"Place the {args.edition} CBA PDF at {args.pdf}", file=sys.stderr)
        sys.exit(1)

    # Compute PDF SHA-256
    print(f"Computing SHA-256 of {args.pdf}...", file=sys.stderr)
    with open(args.pdf, "rb") as f:
        pdf_sha256 = hashlib.sha256(f.read()).hexdigest()
    print(f"PDF SHA-256: {pdf_sha256}", file=sys.stderr)

    # Extract and parse
    print(f"Extracting text from {args.pdf}...", file=sys.stderr)
    cba_parser = CBAParser(args.pdf)
    cba_parser.extract_text()
    
    print("Parsing structure...", file=sys.stderr)
    units = cba_parser.parse_structure()
    print(f"Found {len(units)} structural units", file=sys.stderr)

    # Build output structure
    structure = {
        "edition": args.edition,
        "source_sha256": pdf_sha256,
        "source_url": args.source_url,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "units": [u.to_dict() for u in units],
    }

    # Write output
    output_path = args.output or Path(f"data/derived/cba/{args.edition}/structure.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w") as f:
        json.dump(structure, f, indent=2)
    
    print(f"Structure written to {output_path}", file=sys.stderr)
    print(f"  Edition: {args.edition}", file=sys.stderr)
    print(f"  Units: {len(units)}", file=sys.stderr)
    print(f"  PDF hash: {pdf_sha256}", file=sys.stderr)


if __name__ == "__main__":
    main()
