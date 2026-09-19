#!/usr/bin/env python3
"""
Validate comparable books CSV.

Validates data/derived/books/comparable.csv against locked schema and business rules.

Exit codes:
- 0: All validations pass
- 1: One or more validations fail
"""

import csv
import re
import sys
from pathlib import Path
from typing import List, Optional


# Locked schema columns (order matters)
EXPECTED_COLUMNS = [
    "title",
    "author",
    "publisher",
    "year",
    "amazon_url",
    "amazon_rating",
    "amazon_reviews_count",
    "goodreads_url",
    "goodreads_rating",
    "goodreads_ratings_count",
    "price_band",
    "price_as_of",
    "lane",
    "why_comparable",
    "isbn13",
    "format_notes",
    "source_urls",
    "confidence",
]

# Valid lane values
VALID_LANES = {"narrative", "analytics", "how_to_watch", "history", "memoir"}

# Valid confidence values (case-insensitive)
VALID_CONFIDENCE = {"HIGH", "MEDIUM", "LOW", "GAP"}

# ISO date pattern YYYY-MM-DD
ISO_DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class ValidationError(Exception):
    """Raised when validation fails."""
    pass


def get_csv_path() -> Path:
    """Get path to comparable.csv."""
    repo_root = Path(__file__).parent.parent.parent
    return repo_root / "data" / "derived" / "books" / "comparable.csv"


def load_csv() -> tuple[List[str], List[dict[str, str]]]:
    """Load CSV and return (headers, rows).
    
    Returns:
        (headers, rows) tuple
        
    Raises:
        ValidationError: If CSV cannot be loaded
    """
    csv_path = get_csv_path()
    
    if not csv_path.exists():
        raise ValidationError(f"CSV not found: {csv_path}")
    
    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames
            rows = list(reader)
            
        if not headers:
            raise ValidationError("CSV has no headers")
            
        return list(headers), rows
        
    except Exception as e:
        raise ValidationError(f"Failed to read CSV: {e}")


def validate_schema(headers: List[str]) -> None:
    """Validate CSV headers match locked schema exactly.
    
    Args:
        headers: CSV column headers
        
    Raises:
        ValidationError: If schema doesn't match
    """
    if headers != EXPECTED_COLUMNS:
        raise ValidationError(
            f"Schema mismatch.\n"
            f"Expected: {EXPECTED_COLUMNS}\n"
            f"Got:      {headers}"
        )
    
    print(f"✓ Schema locked ({len(EXPECTED_COLUMNS)} columns)")


def validate_row_count(rows: List[dict[str, str]]) -> None:
    """Validate at least 1 data row exists.
    
    Args:
        rows: CSV rows
        
    Raises:
        ValidationError: If no rows exist
    """
    if not rows:
        raise ValidationError("CSV has no data rows")
    
    print(f"✓ Row count ({len(rows)} rows)")


def validate_required_fields(rows: List[dict[str, str]]) -> None:
    """Validate required fields are non-empty.
    
    Args:
        rows: CSV rows
        
    Raises:
        ValidationError: If required fields are empty
    """
    errors = []
    
    for idx, row in enumerate(rows, start=2):  # Line 2 is first data row
        row_id = f"Row {idx}"
        
        # Title must be non-empty
        if not row.get("title", "").strip():
            errors.append(f"{row_id}: title is empty")
        
        # Author must be non-empty
        if not row.get("author", "").strip():
            errors.append(f"{row_id}: author is empty")
        
        # why_comparable must be non-empty
        if not row.get("why_comparable", "").strip():
            errors.append(f"{row_id}: why_comparable is empty")
    
    if errors:
        raise ValidationError(
            f"Required field validation failed:\n" + "\n".join(f"  - {e}" for e in errors)
        )
    
    print("✓ Required fields (title, author, why_comparable)")


def validate_lanes(rows: List[dict[str, str]]) -> None:
    """Validate lane values are from allowed set.
    
    Args:
        rows: CSV rows
        
    Raises:
        ValidationError: If lane values are invalid
    """
    errors = []
    
    for idx, row in enumerate(rows, start=2):
        lane = row.get("lane", "").strip()
        row_id = f"Row {idx} ({row.get('title', 'unknown')})"
        
        if not lane:
            errors.append(f"{row_id}: lane is empty")
        elif lane not in VALID_LANES:
            errors.append(
                f"{row_id}: invalid lane '{lane}' "
                f"(must be one of: {', '.join(sorted(VALID_LANES))})"
            )
    
    if errors:
        raise ValidationError(
            f"Lane validation failed:\n" + "\n".join(f"  - {e}" for e in errors)
        )
    
    print(f"✓ Lane values (∈ {{{', '.join(sorted(VALID_LANES))}}})")


def validate_price_as_of(rows: List[dict[str, str]]) -> None:
    """Validate price_as_of is empty or ISO date YYYY-MM-DD.
    
    Args:
        rows: CSV rows
        
    Raises:
        ValidationError: If price_as_of format is invalid
    """
    errors = []
    
    for idx, row in enumerate(rows, start=2):
        price_as_of = row.get("price_as_of", "").strip()
        row_id = f"Row {idx} ({row.get('title', 'unknown')})"
        
        # Empty is OK
        if not price_as_of:
            continue
        
        # Must match ISO date pattern
        if not ISO_DATE_PATTERN.match(price_as_of):
            errors.append(
                f"{row_id}: price_as_of '{price_as_of}' "
                f"must be empty or ISO date (YYYY-MM-DD)"
            )
    
    if errors:
        raise ValidationError(
            f"price_as_of validation failed:\n" + "\n".join(f"  - {e}" for e in errors)
        )
    
    print("✓ price_as_of format (empty or YYYY-MM-DD)")


def validate_confidence(rows: List[dict[str, str]]) -> None:
    """Validate confidence values are from allowed set.
    
    Args:
        rows: CSV rows
        
    Raises:
        ValidationError: If confidence values are invalid
    """
    errors = []
    
    for idx, row in enumerate(rows, start=2):
        confidence = row.get("confidence", "").strip().upper()
        row_id = f"Row {idx} ({row.get('title', 'unknown')})"
        
        if not confidence:
            errors.append(f"{row_id}: confidence is empty")
        elif confidence not in VALID_CONFIDENCE:
            errors.append(
                f"{row_id}: invalid confidence '{row.get('confidence')}' "
                f"(must be one of: {', '.join(sorted(VALID_CONFIDENCE))})"
            )
    
    if errors:
        raise ValidationError(
            f"Confidence validation failed:\n" + "\n".join(f"  - {e}" for e in errors)
        )
    
    print(f"✓ Confidence values (∈ {{{', '.join(sorted(VALID_CONFIDENCE))}}})")


def validate_amazon_gap_handling(rows: List[dict[str, str]]) -> None:
    """Validate Amazon fields allow GAP or numeric values.
    
    Args:
        rows: CSV rows
        
    Raises:
        ValidationError: If Amazon field values are invalid
    """
    errors = []
    
    for idx, row in enumerate(rows, start=2):
        row_id = f"Row {idx} ({row.get('title', 'unknown')})"
        
        # amazon_rating: empty, GAP, or numeric
        amazon_rating = row.get("amazon_rating", "").strip()
        if amazon_rating and amazon_rating != "GAP":
            try:
                float(amazon_rating)
            except ValueError:
                errors.append(
                    f"{row_id}: amazon_rating '{amazon_rating}' "
                    f"must be empty, 'GAP', or numeric"
                )
        
        # amazon_reviews_count: empty, GAP, or numeric
        amazon_reviews = row.get("amazon_reviews_count", "").strip()
        if amazon_reviews and amazon_reviews != "GAP":
            try:
                int(amazon_reviews)
            except ValueError:
                errors.append(
                    f"{row_id}: amazon_reviews_count '{amazon_reviews}' "
                    f"must be empty, 'GAP', or numeric"
                )
    
    if errors:
        raise ValidationError(
            f"Amazon field validation failed:\n" + "\n".join(f"  - {e}" for e in errors)
        )
    
    print("✓ Amazon fields (GAP or numeric)")


def main() -> int:
    """Run all validations.
    
    Returns:
        0 if all validations pass, 1 otherwise
    """
    print("Validating comparable books CSV...\n")
    
    try:
        # Load CSV
        headers, rows = load_csv()
        
        # Run validations
        validate_schema(headers)
        validate_row_count(rows)
        validate_required_fields(rows)
        validate_lanes(rows)
        validate_price_as_of(rows)
        validate_confidence(rows)
        validate_amazon_gap_handling(rows)
        
        print("\n✓ All validations passed!")
        return 0
        
    except ValidationError as e:
        print(f"\n✗ Validation failed: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
