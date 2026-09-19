#!/usr/bin/env python3
"""
Validate NBA CBA structure JSON against schema.

Usage:
    python scripts/cba/validate_cba_structure.py data/derived/cba/2023/structure.json
    python scripts/cba/validate_cba_structure.py data/derived/cba/*/structure.json
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("Error: jsonschema not installed. Run: pip install jsonschema", file=sys.stderr)
    sys.exit(1)


def load_schema() -> dict:
    """Load CBA structure JSON schema."""
    schema_path = Path(__file__).parent.parent.parent / "schemas" / "cba_structure.schema.json"
    with open(schema_path) as f:
        return json.load(f)


def validate_structure(structure_path: Path, schema: dict) -> bool:
    """Validate a single structure.json file."""
    print(f"Validating {structure_path}...", end=" ")
    
    try:
        with open(structure_path) as f:
            structure = json.load(f)
    except json.JSONDecodeError as e:
        print(f"FAIL: Invalid JSON - {e}")
        return False
    except FileNotFoundError:
        print(f"FAIL: File not found")
        return False

    try:
        jsonschema.validate(instance=structure, schema=schema)
    except jsonschema.ValidationError as e:
        print(f"FAIL: Schema validation error")
        print(f"  {e.message}", file=sys.stderr)
        print(f"  At: {'.'.join(str(p) for p in e.path)}", file=sys.stderr)
        return False
    except jsonschema.SchemaError as e:
        print(f"FAIL: Schema error - {e}")
        return False

    # Additional checks
    edition = structure.get("edition")
    units = structure.get("units", [])
    
    # Check unit ID uniqueness
    unit_ids = [u["id"] for u in units]
    if len(unit_ids) != len(set(unit_ids)):
        print(f"FAIL: Duplicate unit IDs found")
        duplicates = [uid for uid in unit_ids if unit_ids.count(uid) > 1]
        print(f"  Duplicates: {set(duplicates)}", file=sys.stderr)
        return False

    # Check parent_id references
    for unit in units:
        parent_id = unit.get("parent_id")
        if parent_id and parent_id not in unit_ids:
            print(f"FAIL: Invalid parent_id '{parent_id}' in unit '{unit['id']}'")
            return False

    print(f"OK ({len(units)} units, edition {edition})")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Validate NBA CBA structure JSON files"
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
        help="Exit with non-zero code on any validation failure"
    )

    args = parser.parse_args()

    # Load schema once
    try:
        schema = load_schema()
    except Exception as e:
        print(f"Error loading schema: {e}", file=sys.stderr)
        sys.exit(1)

    # Validate all files
    results = []
    for file_path in args.files:
        result = validate_structure(file_path, schema)
        results.append(result)

    # Summary
    total = len(results)
    passed = sum(results)
    failed = total - passed

    print(f"\n{passed}/{total} files passed")
    
    if failed > 0 and args.strict:
        sys.exit(1)


if __name__ == "__main__":
    main()
