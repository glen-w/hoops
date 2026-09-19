"""NBA CBA structure extraction package.

Productized tools for extracting and validating structural metadata
from NBA Collective Bargaining Agreement PDFs.

Modules:
    hashing: Canonical SHA-256 hashing for PDFs and text
    extract: PDF text extraction using pdftotext
    build_structure: Parse CBA structure (articles, sections, exhibits)
    validate: Schema and hash validation
"""

__version__ = "0.1.0"

from . import hashing, extract, build_structure, validate

__all__ = ["hashing", "extract", "build_structure", "validate"]
