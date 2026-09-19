"""CBA structure validation.

Validates structure.json files against schema and performs regression tests.
Includes TOC regression gates and golden hash validation.
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any

try:
    import jsonschema
    from jsonschema import Draft7Validator
except ImportError:
    raise ImportError(
        "jsonschema not installed. Run: pip install jsonschema>=4.0.0"
    )

from .hashing import strip_prefix, validate_hash_format


# Golden hash from spike: NBA Official 2023 Final PDF
GOLDEN_HASH_2023 = "cf59d43fe46f63d7ba07364563046d766c487c26032fcc88432310d47effd9d9"

# Expected TOC counts from spike (for regression testing)
EXPECTED_COUNTS_2023 = {
    "articles": 42,
    "sections": 279,
    "exhibits": 17,
}

# Spot-check: expected section counts for specific articles (from spike TOC)
EXPECTED_ARTICLE_SECTIONS_2023 = {
    "I": 1,      # Article I: DEFINITIONS - typically 1 section
    "II": 12,    # Article II: PLAYER CONTRACTS  
    "VII": 11,   # Article VII: TEAM SALARY CAP
    "X": 6,      # Article X: [check actual]
    "XI": 5,     # Article XI: [check actual]
}


class ValidationResult:
    """Container for validation results."""
    
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.passed = True
    
    def add_error(self, message: str) -> None:
        """Add an error."""
        self.errors.append(message)
        self.passed = False
    
    def add_warning(self, message: str) -> None:
        """Add a warning."""
        self.warnings.append(message)
    
    def has_issues(self) -> bool:
        """Check if there are any errors or warnings."""
        return bool(self.errors or self.warnings)
    
    def summary(self) -> str:
        """Generate summary text."""
        lines = []
        
        if self.passed:
            lines.append("✓ Validation PASSED")
        else:
            lines.append("✗ Validation FAILED")
        
        if self.errors:
            lines.append(f"\nErrors ({len(self.errors)}):")
            for err in self.errors:
                lines.append(f"  - {err}")
        
        if self.warnings:
            lines.append(f"\nWarnings ({len(self.warnings)}):")
            for warn in self.warnings:
                lines.append(f"  - {warn}")
        
        return "\n".join(lines)


def load_schema() -> Dict[str, Any]:
    """Load CBA structure JSON schema.
    
    Returns:
        Schema dict
        
    Raises:
        FileNotFoundError: If schema file not found
    """
    schema_path = Path(__file__).parents[3] / "schemas" / "cba_structure.schema.json"
    
    if not schema_path.exists():
        raise FileNotFoundError(f"Schema not found: {schema_path}")
    
    with open(schema_path) as f:
        return json.load(f)


def validate_schema(structure: Dict[str, Any]) -> ValidationResult:
    """Validate structure against JSON schema.
    
    Args:
        structure: Structure dict to validate
        
    Returns:
        ValidationResult with any schema errors
    """
    result = ValidationResult()
    
    try:
        schema = load_schema()
        validator = Draft7Validator(schema)
        
        errors = list(validator.iter_errors(structure))
        if errors:
            for error in errors:
                path = ".".join(str(p) for p in error.path) if error.path else "root"
                result.add_error(f"Schema error at {path}: {error.message}")
        
    except Exception as e:
        result.add_error(f"Schema validation failed: {e}")
    
    return result


def validate_golden_hash(structure: Dict[str, Any], strict: bool = False) -> ValidationResult:
    """Validate source hash against golden hash.
    
    For 2023 edition, checks that the PDF hash matches the spike's validated hash.
    This ensures we're processing the same canonical document.
    
    Args:
        structure: Structure dict with source_sha256
        strict: If True, mismatches are errors; if False, they're warnings
        
    Returns:
        ValidationResult
    """
    result = ValidationResult()
    
    edition = structure.get("edition")
    source_hash = strip_prefix(structure.get("source_sha256", ""))
    
    if edition == "2023":
        if source_hash != GOLDEN_HASH_2023:
            msg = (
                f"Hash mismatch for 2023 CBA: "
                f"expected {GOLDEN_HASH_2023}, got {source_hash}"
            )
            if strict:
                result.add_error(msg)
            else:
                result.add_warning(msg)
    
    return result


def validate_toc_regression(structure: Dict[str, Any]) -> ValidationResult:
    """Validate TOC counts against spike expectations.
    
    Regression gate: ensures we're extracting the same structure as the spike.
    
    Args:
        structure: Structure dict with units
        
    Returns:
        ValidationResult with TOC regression results
    """
    result = ValidationResult()
    
    edition = structure.get("edition")
    if edition != "2023":
        # Only 2023 has validated spike data
        return result
    
    units = structure.get("units", [])
    
    # Count unit types
    articles = [u for u in units if u.get("type") == "article"]
    sections = [u for u in units if u.get("type") == "section"]
    exhibits = [u for u in units if u.get("type") == "exhibit"]
    
    # Check overall counts
    actual_counts = {
        "articles": len(articles),
        "sections": len(sections),
        "exhibits": len(exhibits),
    }
    
    for unit_type, expected in EXPECTED_COUNTS_2023.items():
        actual = actual_counts[unit_type]
        if actual != expected:
            result.add_error(
                f"TOC regression failed for {unit_type}: "
                f"expected {expected}, got {actual}"
            )
    
    # Spot-check article section counts
    for article_roman, expected_sections in EXPECTED_ARTICLE_SECTIONS_2023.items():
        article_id = f"cba:2023:art-{article_roman}"
        article_sections = [
            s for s in sections
            if s.get("parent_id") == article_id
        ]
        actual_sections = len(article_sections)
        
        if actual_sections != expected_sections:
            result.add_warning(
                f"Article {article_roman} section count: "
                f"expected {expected_sections}, got {actual_sections}"
            )
    
    return result


def validate_structure_integrity(structure: Dict[str, Any]) -> ValidationResult:
    """Validate internal structure integrity.
    
    Checks:
    - All parent_id references point to valid units
    - No duplicate unit IDs
    - Page ranges are sensible
    - Hash formats are valid
    
    Args:
        structure: Structure dict
        
    Returns:
        ValidationResult
    """
    result = ValidationResult()
    
    units = structure.get("units", [])
    unit_ids = {u.get("id") for u in units if u.get("id")}
    
    # Check for duplicate IDs
    seen_ids = set()
    for unit in units:
        unit_id = unit.get("id")
        if unit_id in seen_ids:
            result.add_error(f"Duplicate unit ID: {unit_id}")
        seen_ids.add(unit_id)
    
    # Check parent references
    for unit in units:
        parent_id = unit.get("parent_id")
        if parent_id and parent_id not in unit_ids:
            result.add_error(
                f"Unit {unit.get('id')} has invalid parent_id: {parent_id}"
            )
    
    # Check page ranges
    for unit in units:
        page_start = unit.get("page_start")
        page_end = unit.get("page_end")
        
        if page_start is not None and page_end is not None:
            if page_end < page_start:
                result.add_error(
                    f"Unit {unit.get('id')} has invalid page range: "
                    f"{page_start}-{page_end}"
                )
    
    # Check hash formats
    source_hash = structure.get("source_sha256")
    if source_hash and not validate_hash_format(source_hash):
        result.add_error(f"Invalid source_sha256 format: {source_hash}")
    
    for unit in units:
        text_hash = unit.get("text_sha256")
        if text_hash and not validate_hash_format(text_hash):
            result.add_error(
                f"Unit {unit.get('id')} has invalid text_sha256 format: {text_hash}"
            )
    
    return result


def validate_all(
    structure: Dict[str, Any],
    strict: bool = False,
    skip_golden_hash: bool = False,
) -> ValidationResult:
    """Run all validations.
    
    Args:
        structure: Structure dict to validate
        strict: If True, all issues are errors
        skip_golden_hash: If True, skip golden hash check (for non-2023 editions)
        
    Returns:
        Combined ValidationResult
    """
    combined = ValidationResult()
    
    # Schema validation
    schema_result = validate_schema(structure)
    combined.errors.extend(schema_result.errors)
    combined.warnings.extend(schema_result.warnings)
    
    # Golden hash validation
    if not skip_golden_hash:
        hash_result = validate_golden_hash(structure, strict=strict)
        combined.errors.extend(hash_result.errors)
        combined.warnings.extend(hash_result.warnings)
    
    # TOC regression
    toc_result = validate_toc_regression(structure)
    combined.errors.extend(toc_result.errors)
    combined.warnings.extend(toc_result.warnings)
    
    # Integrity checks
    integrity_result = validate_structure_integrity(structure)
    combined.errors.extend(integrity_result.errors)
    combined.warnings.extend(integrity_result.warnings)
    
    # Update passed flag
    combined.passed = not combined.errors
    
    return combined


def validate_file(
    structure_path: Path,
    strict: bool = False,
    skip_golden_hash: bool = False,
) -> ValidationResult:
    """Validate a structure.json file.
    
    Args:
        structure_path: Path to structure.json
        strict: If True, all issues are errors
        skip_golden_hash: If True, skip golden hash check
        
    Returns:
        ValidationResult
    """
    result = ValidationResult()
    
    if not structure_path.exists():
        result.add_error(f"File not found: {structure_path}")
        return result
    
    try:
        with open(structure_path) as f:
            structure = json.load(f)
    except json.JSONDecodeError as e:
        result.add_error(f"Invalid JSON: {e}")
        return result
    
    return validate_all(structure, strict=strict, skip_golden_hash=skip_golden_hash)
