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
    """Load structure.json for given edition."""
    structure_path = Path(f"data/derived/cba/{edition}/structure.json")
    fixture_path = Path(f"data/derived/cba/{edition}/structure.fixture.json")
    
    # Try main structure first, fall back to fixture
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
    
    if is_fixture:
        lines.append("")
        lines.append("Status: needs_local_pdf")
        lines.append("(Fixture only - place PDF at data/raw/cba/{}/cba.pdf and regenerate)".format(edition))
    
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
    """Search for unit by exact ID."""
    for unit in units:
        if unit['id'] == unit_id:
            return unit
    return None


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
        
        units = structure.get('units', [])
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
