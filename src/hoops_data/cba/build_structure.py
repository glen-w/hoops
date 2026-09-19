"""CBA structure parser.

Parses NBA CBA text to extract hierarchical structure:
- Articles (e.g., ARTICLE VII)
- Sections (e.g., Section 1, Section 2)  
- Exhibits (e.g., EXHIBIT A)

Generates clause IDs in the format: cba:{edition}:art-{roman}:sec-{num}
"""

import re
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone

from .extract import ExtractedText, char_offset_to_page
from .hashing import compute_text_hash, strip_prefix


@dataclass
class StructuralUnit:
    """A structural unit in the CBA."""
    
    id: str
    type: str  # "article", "section", "exhibit"
    title: str
    parent_id: Optional[str] = None
    page_start: Optional[int] = None
    page_end: Optional[int] = None
    char_offset_start: Optional[int] = None
    char_offset_end: Optional[int] = None
    text_sha256: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to JSON-serializable dict."""
        return {
            "id": self.id,
            "type": self.type,
            "title": self.title[:500],  # Truncate long titles
            "parent_id": self.parent_id,
            "page_start": self.page_start,
            "page_end": self.page_end,
            "char_offset_start": self.char_offset_start,
            "char_offset_end": self.char_offset_end,
            "text_sha256": strip_prefix(self.text_sha256) if self.text_sha256 else None,
        }


@dataclass
class CBAStructure:
    """Complete CBA structure with metadata."""
    
    edition: str
    source_sha256: str
    source_url: str
    generated_at: str
    units: List[StructuralUnit] = field(default_factory=list)
    toolchain_version: Optional[str] = None
    extraction_mode: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to JSON-serializable dict."""
        result = {
            "edition": self.edition,
            "source_sha256": strip_prefix(self.source_sha256),
            "source_url": self.source_url,
            "generated_at": self.generated_at,
            "units": [u.to_dict() for u in self.units],
        }
        
        if self.toolchain_version:
            result["_meta"] = {
                "toolchain_version": self.toolchain_version,
                "extraction_mode": self.extraction_mode,
            }
        
        return result


class CBAParser:
    """Parse CBA structure from extracted text."""
    
    # Patterns for structural markers
    ARTICLE_PATTERN = re.compile(
        r"^ARTICLE\s+([IVXLCDM]+)\s*[:\-\.\s]*(.+?)$",
        re.IGNORECASE | re.MULTILINE
    )
    
    SECTION_PATTERN = re.compile(
        r"^Section\s+(\d+)[\.:\-\s]*(.+?)$",
        re.IGNORECASE | re.MULTILINE
    )
    
    EXHIBIT_PATTERN = re.compile(
        r"^EXHIBIT\s+([A-Z0-9\-]+)\s*[:\-\.\s]*(.+?)$",
        re.IGNORECASE | re.MULTILINE
    )
    
    def __init__(self, edition: str, extracted_text: ExtractedText):
        """Initialize parser.
        
        Args:
            edition: CBA edition year (e.g., "2023")
            extracted_text: Extracted text from extract.py
        """
        self.edition = edition
        self.extracted_text = extracted_text
        self.text = extracted_text.text
        self.page_map = extracted_text.page_map
    
    def parse(self) -> List[StructuralUnit]:
        """Parse structure from text.
        
        Returns:
            List of structural units in document order
        """
        units = []
        
        # Parse articles
        article_units = self._parse_articles()
        units.extend(article_units)
        
        # Parse sections (will be assigned to parent articles)
        section_units = self._parse_sections(article_units)
        units.extend(section_units)
        
        # Parse exhibits
        exhibit_units = self._parse_exhibits()
        units.extend(exhibit_units)
        
        # Sort by position
        units.sort(key=lambda u: u.char_offset_start or 0)
        
        # Compute end positions and text hashes
        self._compute_end_positions(units)
        
        return units
    
    def _parse_articles(self) -> List[StructuralUnit]:
        """Parse article markers."""
        units = []
        
        for match in self.ARTICLE_PATTERN.finditer(self.text):
            roman_num = match.group(1)
            title_part = match.group(2).strip()
            
            # Generate clause ID: cba:2023:art-VII
            article_num = self._roman_to_int(roman_num)
            clause_id = f"cba:{self.edition}:art-{roman_num}"
            
            page_num = char_offset_to_page(match.start(), self.page_map)
            
            # Clean up title
            title = f"ARTICLE {roman_num}"
            if title_part:
                title += f": {title_part}"
            
            unit = StructuralUnit(
                id=clause_id,
                type="article",
                title=title,
                parent_id=None,
                page_start=page_num,
                char_offset_start=match.start(),
            )
            units.append(unit)
        
        return units
    
    def _parse_sections(self, articles: List[StructuralUnit]) -> List[StructuralUnit]:
        """Parse section markers and assign to parent articles."""
        units = []
        
        for match in self.SECTION_PATTERN.finditer(self.text):
            section_num = match.group(1)
            title_part = match.group(2).strip() if match.group(2) else ""
            
            # Find parent article
            parent_article = self._find_parent_article(articles, match.start())
            
            if parent_article:
                # Extract article roman numeral from parent ID: cba:2023:art-VII
                article_roman = parent_article.id.split(":")[-1].replace("art-", "")
                clause_id = f"cba:{self.edition}:art-{article_roman}:sec-{section_num}"
                parent_id = parent_article.id
            else:
                # Orphan section (shouldn't happen in well-formed CBA)
                clause_id = f"cba:{self.edition}:sec-{section_num}"
                parent_id = None
            
            page_num = char_offset_to_page(match.start(), self.page_map)
            
            title = f"Section {section_num}"
            if title_part:
                title += f": {title_part}"
            
            unit = StructuralUnit(
                id=clause_id,
                type="section",
                title=title,
                parent_id=parent_id,
                page_start=page_num,
                char_offset_start=match.start(),
            )
            units.append(unit)
        
        return units
    
    def _parse_exhibits(self) -> List[StructuralUnit]:
        """Parse exhibit markers."""
        units = []
        
        for match in self.EXHIBIT_PATTERN.finditer(self.text):
            exhibit_id_raw = match.group(1).upper()
            title_part = match.group(2).strip() if match.group(2) else ""
            
            # Generate clause ID: cba:2023:exh-A
            clause_id = f"cba:{self.edition}:exh-{exhibit_id_raw}"
            
            page_num = char_offset_to_page(match.start(), self.page_map)
            
            title = f"EXHIBIT {exhibit_id_raw}"
            if title_part:
                title += f": {title_part}"
            
            unit = StructuralUnit(
                id=clause_id,
                type="exhibit",
                title=title,
                parent_id=None,
                page_start=page_num,
                char_offset_start=match.start(),
            )
            units.append(unit)
        
        return units
    
    def _find_parent_article(
        self, articles: List[StructuralUnit], char_offset: int
    ) -> Optional[StructuralUnit]:
        """Find the article that contains the given offset."""
        candidates = [
            a for a in articles
            if a.char_offset_start is not None
            and a.char_offset_start < char_offset
        ]
        return candidates[-1] if candidates else None
    
    def _compute_end_positions(self, units: List[StructuralUnit]) -> None:
        """Compute end positions and text hashes for all units."""
        for i, unit in enumerate(units):
            # Determine end offset
            if i < len(units) - 1:
                unit.char_offset_end = units[i + 1].char_offset_start
            else:
                unit.char_offset_end = len(self.text)
            
            # Compute end page
            if unit.char_offset_end:
                end_page = char_offset_to_page(unit.char_offset_end - 1, self.page_map)
                if end_page:
                    unit.page_end = end_page
                elif unit.page_start:
                    unit.page_end = unit.page_start
            
            # Compute text hash (but don't store the text itself)
            if unit.char_offset_start is not None and unit.char_offset_end is not None:
                unit_text = self.text[unit.char_offset_start:unit.char_offset_end]
                unit.text_sha256 = compute_text_hash(unit_text)
    
    @staticmethod
    def _roman_to_int(roman: str) -> int:
        """Convert Roman numeral to integer."""
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        prev_value = 0
        
        for char in reversed(roman.upper()):
            value = values.get(char, 0)
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        
        return result


def build_structure(
    edition: str,
    extracted_text: ExtractedText,
    source_sha256: str,
    source_url: str = "https://nbpa.com/cba",
) -> CBAStructure:
    """Build complete CBA structure from extracted text.
    
    Args:
        edition: CBA edition year (e.g., "2023")
        extracted_text: Extracted text from extract.py
        source_sha256: SHA-256 hash of source PDF (with or without "sha256:" prefix)
        source_url: Official source URL
        
    Returns:
        Complete CBA structure with metadata
    """
    parser = CBAParser(edition, extracted_text)
    units = parser.parse()
    
    structure = CBAStructure(
        edition=edition,
        source_sha256=source_sha256,
        source_url=source_url,
        generated_at=datetime.now(timezone.utc).isoformat(),
        units=units,
        toolchain_version=extracted_text.toolchain_version,
        extraction_mode=extracted_text.extraction_mode,
    )
    
    return structure
