#!/usr/bin/env python3
"""
Fetch wyattowalsh/basketball dataset from Kaggle (OPTIONAL/FUTURE USE).

STATUS: Currently not required for derived tables. Documented for future use
when box-score level detail or per-position breakdowns are needed.

This script downloads comprehensive NBA statistics for potential future analysis.
See data/raw/LICENSES.md for license terms and redistribution constraints.

Requirements:
- Kaggle API credentials in ~/.kaggle/kaggle.json
- See scripts/README.md for setup instructions

Source: https://www.kaggle.com/datasets/wyattowalsh/basketball
License: CC BY-SA 4.0
Attribution: Wyatt Walsh
"""

import os
import sys
from pathlib import Path


def main():
    # Ensure we're in the repo root
    repo_root = Path(__file__).parent.parent
    raw_data_dir = repo_root / "data" / "raw" / "basketball"
    
    print(f"Hoops Data Fetcher")
    print(f"==================")
    print(f"Target directory: {raw_data_dir}")
    print()
    
    # Check for Kaggle credentials
    kaggle_json = Path.home() / ".kaggle" / "kaggle.json"
    if not kaggle_json.exists():
        print("ERROR: Kaggle credentials not found!")
        print()
        print("Setup instructions:")
        print("1. Visit https://www.kaggle.com/account")
        print("2. Go to Account → Settings → API")
        print("3. Click 'Create New Token'")
        print("4. Save kaggle.json to ~/.kaggle/kaggle.json")
        print("5. Run: chmod 600 ~/.kaggle/kaggle.json")
        print()
        sys.exit(1)
    
    # Create target directory
    raw_data_dir.mkdir(parents=True, exist_ok=True)
    
    # Download using kaggle CLI
    print("Downloading wyattowalsh/basketball dataset...")
    print("(This may take several minutes depending on dataset size)")
    print()
    
    try:
        import kaggle
        kaggle.api.dataset_download_files(
            'wyattowalsh/basketball',
            path=str(raw_data_dir),
            unzip=True,
            quiet=False
        )
        print()
        print("✓ Download complete!")
        print(f"✓ Data saved to: {raw_data_dir}")
        print()
        print("Next steps:")
        print("  uv run python scripts/generate_avg_game.py")
        
    except Exception as e:
        print(f"ERROR: Failed to download dataset: {e}")
        print()
        print("Manual alternative:")
        print(f"  kaggle datasets download -d wyattowalsh/basketball -p {raw_data_dir} --unzip")
        sys.exit(1)


if __name__ == "__main__":
    main()
