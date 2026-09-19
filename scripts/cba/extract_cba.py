#!/usr/bin/env python3
"""Extract NBA CBA structure from PDF.

Main CLI tool for extracting structure metadata from CBA PDFs.
Uses the hoops_data.cba package for extraction, parsing, and validation.

Usage:
    python scripts/cba/extract_cba.py --edition 2023 --pdf data/raw/cba/2023/cba.pdf
"""

import argparse
import json
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parents[2] / "src"))

from hoops_data.cba import hashing, extract, build_structure, validate


def main():
    parser = argparse.ArgumentParser(
        description="Extract NBA CBA structure metadata from PDF",
        formatter_class=argparse.RawDescriptionHelpFormatter,
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
        help="Official source URL (default: https://nbpa.com/cba)"
    )
    
    parser.add_argument(
        "--skip-validation",
        action="store_true",
        help="Skip validation after extraction"
    )
    
    parser.add_argument(
        "--validate-hash",
        action="store_true",
        help="Validate against golden hash (strict mode)"
    )
    
    args = parser.parse_args()
    
    # Check PDF exists
    if not args.pdf.exists():
        print(f"Error: PDF not found: {args.pdf}", file=sys.stderr)
        print(f"Download from {args.source_url}", file=sys.stderr)
        sys.exit(1)
    
    # Compute PDF hash
    print(f"Computing SHA-256 of {args.pdf}...", file=sys.stderr)
    pdf_hash = hashing.compute_file_hash(args.pdf)
    print(f"PDF hash: {pdf_hash}", file=sys.stderr)
    
    # Check golden hash if 2023
    if args.edition == "2023":
        raw_hash = hashing.strip_prefix(pdf_hash)
        if raw_hash == validate.GOLDEN_HASH_2023:
            print("✓ Golden hash match (NBA Official 2023 Final)", file=sys.stderr)
        else:
            print(f"⚠ Hash does not match golden hash", file=sys.stderr)
            print(f"  Expected: {validate.GOLDEN_HASH_2023}", file=sys.stderr)
            print(f"  Got:      {raw_hash}", file=sys.stderr)
            if args.validate_hash:
                print("  Aborting due to --validate-hash", file=sys.stderr)
                sys.exit(1)
    
    # Extract text
    print(f"Extracting text from {args.pdf}...", file=sys.stderr)
    try:
        extracted = extract.extract_text_with_layout(args.pdf)
        print(f"Toolchain: {extracted.toolchain_version}", file=sys.stderr)
        print(f"Text length: {len(extracted.text):,} chars", file=sys.stderr)
        print(f"Pages: {len(extracted.page_map)}", file=sys.stderr)
    except Exception as e:
        print(f"Error extracting text: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Parse structure
    print("Parsing structure...", file=sys.stderr)
    try:
        structure = build_structure.build_structure(
            edition=args.edition,
            extracted_text=extracted,
            source_sha256=pdf_hash,
            source_url=args.source_url,
        )
    except Exception as e:
        print(f"Error parsing structure: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Report stats
    articles = [u for u in structure.units if u.type == "article"]
    sections = [u for u in structure.units if u.type == "section"]
    exhibits = [u for u in structure.units if u.type == "exhibit"]
    
    print(f"\nStructure extracted:", file=sys.stderr)
    print(f"  Articles: {len(articles)}", file=sys.stderr)
    print(f"  Sections: {len(sections)}", file=sys.stderr)
    print(f"  Exhibits: {len(exhibits)}", file=sys.stderr)
    print(f"  Total units: {len(structure.units)}", file=sys.stderr)
    
    # Validate
    if not args.skip_validation:
        print("\nValidating structure...", file=sys.stderr)
        validation = validate.validate_all(
            structure.to_dict(),
            strict=args.validate_hash,
            skip_golden_hash=False,
        )
        
        if validation.has_issues():
            print(validation.summary(), file=sys.stderr)
            if not validation.passed:
                print("\nValidation failed. Use --skip-validation to write anyway.", file=sys.stderr)
                sys.exit(1)
        else:
            print("✓ All validations passed", file=sys.stderr)
    
    # Write output
    output_path = args.output or Path(f"data/derived/cba/{args.edition}/structure.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w") as f:
        json.dump(structure.to_dict(), f, indent=2)
        f.write("\n")
    
    print(f"\n✓ Structure written to {output_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
