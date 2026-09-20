#!/usr/bin/env python3
"""Validate NBA CBA structure JSON files.

Uses the hoops_data.cba.validate module for comprehensive validation including:
- JSON schema validation
- TOC regression tests (2023 edition)
- Golden hash validation (2023 edition)
- Structure integrity checks

Usage:
    python scripts/cba/validate_cba_structure.py data/derived/cba/2023/structure.fixture.json
    python scripts/cba/validate_cba_structure.py data/derived/cba/2023/structure.fixture.json --strict
"""

import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parents[2] / "src"))

from hoops_data.cba import validate


def main():
    parser = argparse.ArgumentParser(
        description="Validate NBA CBA structure JSON files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    parser.add_argument(
        "files",
        nargs="+",
        type=Path,
        help="Path(s) to structure.json file(s)"
    )
    
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with non-zero code on any validation failure (warnings become errors)"
    )
    
    parser.add_argument(
        "--skip-golden-hash",
        action="store_true",
        help="Skip golden hash validation"
    )
    
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed validation output"
    )

    args = parser.parse_args()

    # Validate all files
    results = []
    
    for file_path in args.files:
        print(f"\nValidating {file_path}...")
        
        result = validate.validate_file(
            file_path,
            strict=args.strict,
            skip_golden_hash=args.skip_golden_hash,
        )
        
        if args.verbose or result.has_issues():
            print(result.summary())
        elif result.passed:
            print("✓ Validation passed")
        
        results.append(result.passed)

    # Summary
    total = len(results)
    passed = sum(results)
    failed = total - passed

    print(f"\n{'='*60}")
    print(f"Summary: {passed}/{total} files passed")
    
    if failed > 0:
        print(f"  {failed} file(s) failed validation")
        sys.exit(1)
    else:
        print("  All validations passed!")
        sys.exit(0)


if __name__ == "__main__":
    main()
