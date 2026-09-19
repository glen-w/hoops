#!/usr/bin/env python3
"""
Validate NBA org-chart CSVs in data/derived/nba_orgs/

Checks:
- Locked column schema: team,role,name,title,source_url,as_of,confidence
- Role vocabulary constraint
- Non-empty files

Exit codes:
- 0: All CSVs valid
- 1: Schema violation, role vocabulary drift, or other validation failure
"""

import sys
from pathlib import Path
import csv

LOCKED_COLUMNS = ["team", "role", "name", "title", "source_url", "as_of", "confidence"]

ROLE_VOCABULARY = {
    "ownership",
    "president",
    "gm",
    "basketball_ops",
    "analytics",
    "scouting",
    "medical",
    "business",
    "coaching",
}


def validate_csv(csv_path: Path) -> tuple[bool, list[str]]:
    """
    Validate a single CSV file.
    
    Returns:
        (is_valid, errors) tuple
    """
    errors = []
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            # Check column schema
            if reader.fieldnames != LOCKED_COLUMNS:
                errors.append(
                    f"Column mismatch. Expected {LOCKED_COLUMNS}, "
                    f"got {list(reader.fieldnames)}"
                )
                return False, errors
            
            # Check role vocabulary
            row_num = 2  # Start at 2 (1 is header)
            invalid_roles = set()
            
            for row in reader:
                role = row.get("role", "").strip()
                if role and role not in ROLE_VOCABULARY:
                    invalid_roles.add(role)
                row_num += 1
            
            if invalid_roles:
                errors.append(
                    f"Invalid role values: {sorted(invalid_roles)}. "
                    f"Allowed: {sorted(ROLE_VOCABULARY)}"
                )
                return False, errors
            
            # Check if file has at least one data row
            if row_num == 2:
                errors.append("CSV is empty (no data rows)")
                return False, errors
                
    except Exception as e:
        errors.append(f"Failed to read CSV: {e}")
        return False, errors
    
    return True, []


def main() -> int:
    """
    Validate all NBA org CSVs.
    
    Returns:
        Exit code (0 = success, 1 = validation failure)
    """
    repo_root = Path(__file__).parent.parent
    nba_orgs_dir = repo_root / "data" / "derived" / "nba_orgs"
    
    if not nba_orgs_dir.exists():
        print(f"ERROR: Directory not found: {nba_orgs_dir}", file=sys.stderr)
        return 1
    
    csv_files = sorted(nba_orgs_dir.glob("*.csv"))
    
    if not csv_files:
        print(f"WARNING: No CSV files found in {nba_orgs_dir}", file=sys.stderr)
        return 0  # Not an error, just no files to validate
    
    all_valid = True
    
    for csv_file in csv_files:
        is_valid, errors = validate_csv(csv_file)
        
        if is_valid:
            print(f"✓ {csv_file.name}")
        else:
            print(f"✗ {csv_file.name}", file=sys.stderr)
            for error in errors:
                print(f"  - {error}", file=sys.stderr)
            all_valid = False
    
    if all_valid:
        print(f"\n✓ All {len(csv_files)} CSV(s) valid")
        return 0
    else:
        print(f"\n✗ Validation failed", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
