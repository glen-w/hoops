"""Canonical hashing for CBA files.

Provides deterministic SHA-256 hashing with standardized text normalization.
All hashes use "sha256:" prefix for consistency.
"""

import hashlib
from pathlib import Path
from typing import Union


def compute_file_hash(path: Union[str, Path]) -> str:
    """Compute SHA-256 hash of file (binary mode).
    
    Args:
        path: Path to file
        
    Returns:
        Hash string with "sha256:" prefix
        
    Example:
        >>> compute_file_hash("data/raw/cba/2023/cba.pdf")
        "sha256:cf59d43fe46f63d7ba07364563046d766c487c26032fcc88432310d47effd9d9"
    """
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return f"sha256:{h.hexdigest()}"


def compute_text_hash(text: str) -> str:
    """Compute SHA-256 hash of text with canonical normalization.
    
    Text is normalized to UTF-8 with LF line endings and a trailing newline
    before hashing to ensure consistency across platforms.
    
    Args:
        text: Text content to hash
        
    Returns:
        Hash string with "sha256:" prefix
        
    Example:
        >>> compute_text_hash("Sample CBA text\\n")
        "sha256:..."
    """
    # Normalize to canonical form: UTF-8, LF line endings, trailing newline
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    if not normalized.endswith("\n"):
        normalized += "\n"
    
    h = hashlib.sha256(normalized.encode("utf-8"))
    return f"sha256:{h.hexdigest()}"


def strip_prefix(hash_string: str) -> str:
    """Strip 'sha256:' prefix from hash string if present.
    
    Args:
        hash_string: Hash string with or without prefix
        
    Returns:
        Raw hex digest without prefix
    """
    if hash_string.startswith("sha256:"):
        return hash_string[7:]
    return hash_string


def validate_hash_format(hash_string: str) -> bool:
    """Validate hash string format.
    
    Args:
        hash_string: Hash string to validate
        
    Returns:
        True if valid format (64 hex chars with optional "sha256:" prefix)
    """
    raw = strip_prefix(hash_string)
    return len(raw) == 64 and all(c in "0123456789abcdef" for c in raw)
