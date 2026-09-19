#!/bin/bash
#
# Fetch wyattowalsh/basketball NBA Database from Kaggle
#
# Prerequisites:
#   - Kaggle API credentials configured (~/.kaggle/kaggle.json)
#   - Install: pip install kaggle
#
# Usage:
#   bash scripts/fetch_wyattowalsh.sh
#
# See data/raw/LICENSES.md for dataset details and license terms.

set -euo pipefail

TARGET_DIR="data/raw/wyattowalsh-basketball"

echo "Fetching wyattowalsh/basketball NBA Database..."
echo "Target: $TARGET_DIR"
echo ""

# Check for Kaggle credentials
if [ ! -f ~/.kaggle/kaggle.json ] && [ -z "${KAGGLE_USERNAME:-}" ]; then
    echo "❌ Kaggle credentials not found"
    echo ""
    echo "To download this dataset, set up Kaggle API access:"
    echo "  1. Create a Kaggle account at https://www.kaggle.com"
    echo "  2. Go to https://www.kaggle.com/settings and click 'Create New Token'"
    echo "  3. Place the downloaded kaggle.json in ~/.kaggle/"
    echo "  4. Run: chmod 600 ~/.kaggle/kaggle.json"
    echo ""
    echo "Alternatively, set KAGGLE_USERNAME and KAGGLE_KEY environment variables."
    exit 1
fi

# Create target directory
mkdir -p "$TARGET_DIR"

# Download the dataset
echo "Downloading dataset (this may take several minutes, ~2GB+)..."
kaggle datasets download -d wyattowalsh/basketball -p "$TARGET_DIR"

# Unzip
echo "Extracting files..."
cd "$TARGET_DIR"
unzip -o basketball.zip
rm basketball.zip

echo ""
echo "✓ Successfully downloaded wyattowalsh/basketball to $TARGET_DIR"
echo ""
echo "Contents:"
ls -lh

echo ""
echo "To regenerate derived tables from this raw data, run:"
echo "  uv run python scripts/build_avg_game_by_decade.py"
