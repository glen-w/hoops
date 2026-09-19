"""PDF text extraction for CBA documents.

Uses pdftotext for extraction with page tracking and toolchain version recording.
Implements critical fix: splitlines() before stripping form-feed characters.
"""

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple, Optional


@dataclass
class ExtractedText:
    """Container for extracted CBA text with metadata."""
    
    text: str
    page_map: List[Tuple[int, int, int]]  # [(page_num, char_start, char_end)]
    toolchain_version: str
    extraction_mode: str = "layout"


def get_pdftotext_version() -> str:
    """Get pdftotext version string.
    
    Returns:
        Version string like "pdftotext version 22.02.0"
        
    Raises:
        RuntimeError: If pdftotext is not available
    """
    try:
        result = subprocess.run(
            ["pdftotext", "-v"],
            capture_output=True,
            text=True,
            check=False
        )
        # pdftotext outputs version to stderr
        version_output = result.stderr.strip().split("\n")[0]
        return version_output
    except FileNotFoundError:
        raise RuntimeError(
            "pdftotext not found. Install poppler-utils:\n"
            "  Ubuntu/Debian: sudo apt-get install poppler-utils\n"
            "  macOS: brew install poppler\n"
            "  Windows: download from https://blog.alivate.com.au/poppler-windows/"
        )


def extract_text_with_layout(pdf_path: Path) -> ExtractedText:
    """Extract text from PDF using pdftotext with layout preservation.
    
    This is the primary extraction method. Uses `-layout` flag to preserve
    spatial positioning, which helps with structural marker detection.
    
    CRITICAL FIX: splitlines() is called BEFORE stripping form-feed (\\f)
    characters to avoid merging lines that should remain separate.
    
    Args:
        pdf_path: Path to PDF file
        
    Returns:
        ExtractedText with text, page mapping, and metadata
        
    Raises:
        RuntimeError: If extraction fails
    """
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")
    
    # Get toolchain version
    toolchain_version = get_pdftotext_version()
    
    # Extract with layout preservation
    try:
        result = subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), "-"],
            capture_output=True,
            text=True,
            check=True
        )
        raw_text = result.stdout
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"pdftotext failed: {e.stderr}")
    
    # SPIKE HAZARD #2 FIX: splitlines() before stripping form-feed
    # Form-feed (\\f) often separates pages; if we strip it first,
    # we can accidentally merge lines from different pages.
    lines = raw_text.splitlines()
    
    # Now strip form-feeds from each line
    lines = [line.replace("\f", "") for line in lines]
    
    # Reconstruct with consistent line endings
    text = "\n".join(lines)
    if text and not text.endswith("\n"):
        text += "\n"
    
    # Build page map (approximate - pdftotext doesn't provide page boundaries)
    # We'll use form-feed markers in the raw text to estimate pages
    page_map = _build_page_map_from_text(raw_text, text)
    
    return ExtractedText(
        text=text,
        page_map=page_map,
        toolchain_version=toolchain_version,
        extraction_mode="layout"
    )


def extract_text_raw(pdf_path: Path) -> ExtractedText:
    """Extract text from PDF without layout preservation.
    
    Fallback extraction mode. Use when layout mode produces poor results.
    
    Args:
        pdf_path: Path to PDF file
        
    Returns:
        ExtractedText with text, page mapping, and metadata
    """
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")
    
    toolchain_version = get_pdftotext_version()
    
    try:
        result = subprocess.run(
            ["pdftotext", str(pdf_path), "-"],
            capture_output=True,
            text=True,
            check=True
        )
        raw_text = result.stdout
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"pdftotext failed: {e.stderr}")
    
    # Apply same splitlines() fix
    lines = raw_text.splitlines()
    lines = [line.replace("\f", "") for line in lines]
    text = "\n".join(lines)
    if text and not text.endswith("\n"):
        text += "\n"
    
    page_map = _build_page_map_from_text(raw_text, text)
    
    return ExtractedText(
        text=text,
        page_map=page_map,
        toolchain_version=toolchain_version,
        extraction_mode="raw"
    )


def _build_page_map_from_text(raw_text: str, processed_text: str) -> List[Tuple[int, int, int]]:
    """Build approximate page mapping from form-feed markers.
    
    pdftotext inserts form-feed (\\f) characters at page boundaries.
    We use these to estimate page ranges in the character stream.
    
    Args:
        raw_text: Original pdftotext output with form-feeds
        processed_text: Processed text with form-feeds stripped
        
    Returns:
        List of (page_num, char_start, char_end) tuples
    """
    page_map = []
    
    # Split raw text by form-feed to get pages
    raw_pages = raw_text.split("\f")
    
    char_offset = 0
    for page_num, raw_page in enumerate(raw_pages, start=1):
        # Process this page the same way we processed the full text
        page_lines = raw_page.splitlines()
        page_text = "\n".join(page_lines)
        if page_text:
            page_text += "\n"
        
        page_len = len(page_text)
        if page_len > 0:
            page_map.append((page_num, char_offset, char_offset + page_len))
            char_offset += page_len
    
    # Handle case where we have no form-feeds (single page or issue)
    if not page_map and processed_text:
        page_map.append((1, 0, len(processed_text)))
    
    return page_map


def char_offset_to_page(offset: int, page_map: List[Tuple[int, int, int]]) -> Optional[int]:
    """Convert character offset to page number.
    
    Args:
        offset: Character offset in extracted text
        page_map: Page mapping from ExtractedText
        
    Returns:
        Page number (1-indexed) or None if not found
    """
    for page_num, start, end in page_map:
        if start <= offset < end:
            return page_num
    return None
