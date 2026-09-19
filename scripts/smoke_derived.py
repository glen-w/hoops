#!/usr/bin/env python3
"""
Smoke test for the hoops-data pipeline.

Generates a minimal placeholder CSV in data/derived/ to verify that:
- The uv environment is correctly configured
- pandas can be imported and used
- The data/derived/ directory is writable
- The pipeline can produce reproducible output

Methodology: Creates synthetic basketball statistics with two example rows
(one historic, one modern) to demonstrate the expected schema for future
per-decade average game statistics.
"""

import pandas as pd
from pathlib import Path


def main():
    # Define output path
    output_path = Path(__file__).parent.parent / "data" / "derived" / "smoke_placeholder.csv"
    
    # Create minimal example data
    data = {
        "decade": ["1960s", "2020s"],
        "avg_points_per_game": [110.4, 114.7],
        "avg_fga_per_game": [88.5, 88.9],
        "avg_fg_pct": [0.423, 0.470],
        "avg_3pa_per_game": [0.0, 35.1],
        "note": ["Pre-3pt era", "Modern pace-and-space"]
    }
    
    df = pd.DataFrame(data)
    
    # Write to CSV
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    
    print(f"✓ Smoke test passed: {output_path}")
    print(f"  Generated {len(df)} placeholder rows")


if __name__ == "__main__":
    main()
