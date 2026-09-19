#!/usr/bin/env python3
"""
NBA CBA Lookup Desk — Query committed structure metadata.

Quick reference tool for Scrivener mid-draft: look up article IDs, sections,
or defined terms from committed structure.json (no fulltext access from git).

Usage:
    python scripts/cba_lookup.py "Article VII"
    python scripts/cba_lookup.py --edition 2023 "Section 1"
    python scripts/cba_lookup.py --id article_7
    python scripts/cba_lookup.py --term "Salary Cap"
    python scripts/cba_lookup.py --list-articles

Examples:
    # Look up by article name
    $ python scripts/cba_lookup.py "Article VII"
    
    # Look up by unit ID
    $ python scripts/cba_lookup.py --id article_7_section_1
    
    # List all top-level articles
    $ python scripts/cba_lookup.py --list-articles
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import List, Dict, Optional


def load_structure(edition: str) -> Optional[Dict]:
    """Load structure.json for given edition.
    
    Prefers canonical path from Infra #13: data/cba/{edition}/derived/structure.json
    Falls back to legacy paths for compatibility.
    """
    # Try canonical Infra #13 path first
    canonical_path = Path(f"data/cba/{edition}/derived/structure.json")
    if canonical_path.exists():
        with open(canonical_path) as f:
            return json.load(f)
    
    # Fall back to legacy productization paths
    structure_path = Path(f"data/derived/cba/{edition}/structure.json")
    fixture_path = Path(f"data/derived/cba/{edition}/structure.fixture.json")
    
    if structure_path.exists():
        with open(structure_path) as f:
            return json.load(f)
    elif fixture_path.exists():
        with open(fixture_path) as f:
            data = json.load(f)
            data["_is_fixture"] = True
            return data
    else:
        return None


def format_unit(unit: Dict, edition: str, is_fixture: bool = False) -> str:
    """Format a structural unit for display."""
    lines = []
    lines.append(f"Edition: {edition}")
    lines.append(f"ID: {unit['id']}")
    lines.append(f"Type: {unit['type']}")
    lines.append(f"Title: {unit['title']}")
    
    if unit.get('parent_id'):
        lines.append(f"Parent: {unit['parent_id']}")
    
    if unit.get('page_start') is not None:
        page_range = f"{unit['page_start']}"
        if unit.get('page_end') and unit['page_end'] != unit['page_start']:
            page_range += f"-{unit['page_end']}"
        lines.append(f"Pages: {page_range}")
    elif is_fixture:
        lines.append(f"Pages: [fixture - needs_local_pdf]")
    
    if unit.get('char_offset_start') is not None and unit.get('char_offset_end') is not None:
        span_len = unit['char_offset_end'] - unit['char_offset_start']
        lines.append(f"Character span: {unit['char_offset_start']}-{unit['char_offset_end']} ({span_len:,} chars)")
    
    # Show text hash if present
    if unit.get('text_sha256'):
        lines.append(f"Content hash: sha256:{unit['text_sha256'][:16]}...")
    
    if is_fixture:
        lines.append("")
        lines.append("Status: quotes_need_pdf")
        lines.append("(Fixture — lookup ready, quotes need PDF at data/raw/cba/{}/cba.pdf)".format(edition))
    
    return "\n".join(lines)


def search_by_title(units: List[Dict], query: str) -> List[Dict]:
    """Search units by title (case-insensitive partial match)."""
    query_lower = query.lower()
    results = []
    
    for unit in units:
        title_lower = unit['title'].lower()
        if query_lower in title_lower:
            results.append(unit)
    
    return results


def search_by_id(units: List[Dict], unit_id: str) -> Optional[Dict]:
    """Search for unit by exact ID.
    
    Supports both new clause ID format (cba:2023:art-VII:sec-1) and
    legacy format (article_7_section_1) for backward compatibility.
    """
    # Direct match
    for unit in units:
        if unit['id'] == unit_id:
            return unit
    
    # Try legacy format conversion (article_7 -> cba:EDITION:art-VII)
    # This handles structure.fixture.json which may use old IDs
    if not unit_id.startswith("cba:"):
        # Extract edition from first unit if available
        edition = units[0].get('id', '').split(':')[1] if units and ':' in units[0].get('id', '') else '2023'
        
        # Convert legacy ID to new format
        if unit_id.startswith("article_"):
            # article_7 -> cba:2023:art-VII
            num = unit_id.replace("article_", "")
            if num.isdigit():
                roman = _int_to_roman(int(num))
                new_id = f"cba:{edition}:art-{roman}"
                for unit in units:
                    if unit['id'] == new_id:
                        return unit
        elif "section_" in unit_id:
            # article_7_section_1 -> cba:2023:art-VII:sec-1
            parts = unit_id.split("_section_")
            if len(parts) == 2:
                article_part = parts[0].replace("article_", "")
                section_num = parts[1]
                if article_part.isdigit() and section_num.isdigit():
                    roman = _int_to_roman(int(article_part))
                    new_id = f"cba:{edition}:art-{roman}:sec-{section_num}"
                    for unit in units:
                        if unit['id'] == new_id:
                            return unit
    
    return None


def _int_to_roman(num: int) -> str:
    """Convert integer to Roman numeral."""
    values = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = []
    for value, numeral in values:
        count = num // value
        if count:
            result.append(numeral * count)
            num -= value * count
    return ''.join(result)


def search_by_term(units: List[Dict], term: str) -> List[Dict]:
    """Search for defined term in article titles (limited to DEFINITIONS articles)."""
    # Look in Article I (DEFINITIONS) and related units
    term_lower = term.lower()
    results = []
    
    for unit in units:
        # Check if this is a definitions-related unit
        title_lower = unit['title'].lower()
        if 'definition' in title_lower and term_lower in title_lower:
            results.append(unit)
    
    return results


def list_articles(units: List[Dict]) -> List[Dict]:
    """List all top-level articles."""
    return [u for u in units if u['type'] == 'article' and u.get('parent_id') is None]


def main():
    parser = argparse.ArgumentParser(
        description="NBA CBA Lookup Desk - Query committed structure metadata",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "Article VII"              Look up by article name
  %(prog)s --id article_7             Look up by unit ID
  %(prog)s --term "Salary Cap"        Search for defined term
  %(prog)s --list-articles            List all articles
  %(prog)s --edition 2017 "Section 1" Look up in 2017 CBA

Note: This tool queries committed structure.json metadata only.
      No fulltext is stored in git. For body text, see local PDF.
        """
    )
    
    parser.add_argument(
        "query",
        nargs="?",
        help="Search query (article name, section, etc.)"
    )
    parser.add_argument(
        "--edition",
        choices=["2017", "2023"],
        default="2023",
        help="CBA edition to query (default: 2023)"
    )
    parser.add_argument(
        "--id",
        dest="unit_id",
        help="Look up by exact unit ID"
    )
    parser.add_argument(
        "--term",
        help="Search for defined term"
    )
    parser.add_argument(
        "--list-articles",
        action="store_true",
        help="List all top-level articles"
    )
    parser.add_argument(
        "--all-editions",
        action="store_true",
        help="Search across all available editions"
    )
    
    args = parser.parse_args()
    
    # Determine editions to search
    editions = ["2017", "2023"] if args.all_editions else [args.edition]
    
    # Validate arguments
    if not any([args.query, args.unit_id, args.term, args.list_articles]):
        parser.print_help()
        sys.exit(1)
    
    found_any = False
    
    for edition in editions:
        structure = load_structure(edition)
        
        if not structure:
            if len(editions) == 1:
                print(f"Error: No structure found for {edition} CBA", file=sys.stderr)
                print(f"Expected: data/derived/cba/{edition}/structure.json", file=sys.stderr)
                sys.exit(1)
            continue
        
        # Support both Infra #13 format (articles/exhibits arrays) and package format (units array)
        units = structure.get('units', [])
        if not units:
            # Infra #13 format: flatten articles and exhibits, normalize to package format
            units = []
            for article in structure.get('articles', []):
                # Normalize article to package format
                article_unit = {
                    'id': article['id'],
                    'type': 'article',
                    'title': article.get('label') or f"ARTICLE {article['number']}: {article['title']}",
                    'parent_id': None,
                    'page_start': None,  # #13 format doesn't have page numbers
                    'page_end': None,
                }
                units.append(article_unit)
                
                # Add sections
                for section in article.get('sections', []):
                    # Handle null titles in source data
                    section_title = section.get('title') or ''
                    if section_title:
                        full_title = f"Section {section['number']}: {section_title}"
                    else:
                        full_title = f"Section {section['number']}"
                    
                    section_unit = {
                        'id': section['id'],
                        'type': 'section',
                        'title': full_title,
                        'parent_id': article['id'],
                        'page_start': None,
                        'page_end': None,
                    }
                    units.append(section_unit)
            
            # Add exhibits
            for exhibit in structure.get('exhibits', []):
                exhibit_unit = {
                    'id': exhibit['id'],
                    'type': 'exhibit',
                    'title': exhibit.get('label') or f"EXHIBIT {exhibit['number']}: {exhibit['title']}",
                    'parent_id': None,
                    'page_start': None,
                    'page_end': None,
                }
                units.append(exhibit_unit)
        is_fixture = structure.get('_is_fixture', False)
        
        results = []
        
        # Execute search
        if args.list_articles:
            results = list_articles(units)
        elif args.unit_id:
            unit = search_by_id(units, args.unit_id)
            if unit:
                results = [unit]
        elif args.term:
            results = search_by_term(units, args.term)
        elif args.query:
            results = search_by_title(units, args.query)
        
        # Display results
        if results:
            found_any = True
            
            if len(editions) > 1:
                print(f"\n{'='*60}")
                print(f"Edition: {edition}")
                print(f"{'='*60}")
            
            for i, unit in enumerate(results):
                if i > 0:
                    print("\n" + "-" * 60 + "\n")
                print(format_unit(unit, edition, is_fixture))
            
            if args.list_articles:
                print(f"\nTotal articles: {len(results)}")
    
    if not found_any:
        print("No results found.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
