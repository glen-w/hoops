"""
Test suite for comparable books CSV validation.

Validates:
- CSV schema locks
- Data integrity
- Required fields
- Lane and confidence values
- Date formats
- Amazon GAP handling
"""

import csv
import sys
from pathlib import Path

import pytest


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

# Valid values
VALID_LANES = {"narrative", "analytics", "how_to_watch", "history", "memoir"}
VALID_CONFIDENCE = {"HIGH", "MEDIUM", "LOW", "GAP"}


@pytest.fixture
def csv_path():
    """Get path to comparable.csv."""
    repo_root = Path(__file__).parent.parent.parent
    return repo_root / "data" / "derived" / "books" / "comparable.csv"


@pytest.fixture
def csv_data(csv_path):
    """Load CSV data."""
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        rows = list(reader)
    return list(headers), rows


def test_csv_exists(csv_path):
    """Test that comparable.csv exists."""
    assert csv_path.exists(), f"comparable.csv not found at {csv_path}"


def test_schema_locked(csv_data):
    """Test that CSV headers match locked schema exactly."""
    headers, _ = csv_data
    assert headers == EXPECTED_COLUMNS, (
        f"Schema mismatch.\n"
        f"Expected: {EXPECTED_COLUMNS}\n"
        f"Got:      {headers}"
    )


def test_has_data_rows(csv_data):
    """Test that CSV has at least one data row."""
    _, rows = csv_data
    assert len(rows) >= 1, "CSV must have at least 1 data row"


def test_required_fields_non_empty(csv_data):
    """Test that required fields are non-empty."""
    _, rows = csv_data
    
    for idx, row in enumerate(rows, start=1):
        assert row["title"].strip(), f"Row {idx}: title is empty"
        assert row["author"].strip(), f"Row {idx}: author is empty"
        assert row["why_comparable"].strip(), f"Row {idx}: why_comparable is empty"


def test_lane_values(csv_data):
    """Test that lane values are from allowed set."""
    _, rows = csv_data
    
    for idx, row in enumerate(rows, start=1):
        lane = row["lane"].strip()
        assert lane in VALID_LANES, (
            f"Row {idx} ({row['title']}): invalid lane '{lane}' "
            f"(must be one of: {', '.join(sorted(VALID_LANES))})"
        )


def test_confidence_values(csv_data):
    """Test that confidence values are from allowed set."""
    _, rows = csv_data
    
    for idx, row in enumerate(rows, start=1):
        confidence = row["confidence"].strip().upper()
        assert confidence in VALID_CONFIDENCE, (
            f"Row {idx} ({row['title']}): invalid confidence '{row['confidence']}' "
            f"(must be one of: {', '.join(sorted(VALID_CONFIDENCE))})"
        )


def test_price_as_of_format(csv_data):
    """Test that price_as_of is empty or ISO date YYYY-MM-DD."""
    import re
    
    _, rows = csv_data
    iso_date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    
    for idx, row in enumerate(rows, start=1):
        price_as_of = row["price_as_of"].strip()
        
        # Empty is OK
        if not price_as_of:
            continue
        
        # Must match ISO date pattern
        assert iso_date_pattern.match(price_as_of), (
            f"Row {idx} ({row['title']}): price_as_of '{price_as_of}' "
            f"must be empty or ISO date (YYYY-MM-DD)"
        )


def test_amazon_rating_format(csv_data):
    """Test that amazon_rating is empty, GAP, or numeric."""
    _, rows = csv_data
    
    for idx, row in enumerate(rows, start=1):
        amazon_rating = row["amazon_rating"].strip()
        
        # Empty or GAP is OK
        if not amazon_rating or amazon_rating == "GAP":
            continue
        
        # Must be numeric
        try:
            float(amazon_rating)
        except ValueError:
            pytest.fail(
                f"Row {idx} ({row['title']}): amazon_rating '{amazon_rating}' "
                f"must be empty, 'GAP', or numeric"
            )


def test_amazon_reviews_count_format(csv_data):
    """Test that amazon_reviews_count is empty, GAP, or numeric."""
    _, rows = csv_data
    
    for idx, row in enumerate(rows, start=1):
        amazon_reviews = row["amazon_reviews_count"].strip()
        
        # Empty or GAP is OK
        if not amazon_reviews or amazon_reviews == "GAP":
            continue
        
        # Must be numeric
        try:
            int(amazon_reviews)
        except ValueError:
            pytest.fail(
                f"Row {idx} ({row['title']}): amazon_reviews_count '{amazon_reviews}' "
                f"must be empty, 'GAP', or numeric"
            )


def test_validator_script_passes():
    """Test that the validator script passes against the committed CSV."""
    import subprocess
    
    repo_root = Path(__file__).parent.parent.parent
    script_path = repo_root / "scripts" / "books" / "validate_comparable.py"
    
    assert script_path.exists(), f"Validator script not found at {script_path}"
    
    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=repo_root,
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0, (
        f"Validator script failed:\n"
        f"stdout: {result.stdout}\n"
        f"stderr: {result.stderr}"
    )


# Negative test: bad lane value
def test_bad_lane_rejection(tmp_path):
    """Test that invalid lane values are rejected."""
    from scripts.books.validate_comparable import validate_lanes, ValidationError
    
    bad_rows = [
        {"title": "Test Book", "lane": "invalid_lane"}
    ]
    
    with pytest.raises(ValidationError, match="invalid lane"):
        validate_lanes(bad_rows)
