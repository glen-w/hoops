#!/usr/bin/env bash
# CI validation for CBA structure
# - If PDF present: regenerate and diff
# - If PDF absent: validate fixture only

set -e

EDITIONS=("2023" "2017")

echo "=== CBA Structure CI Validation ==="
echo

for edition in "${EDITIONS[@]}"; do
    echo "Checking edition: $edition"
    
    pdf_path="data/raw/cba/$edition/cba.pdf"
    structure_path="data/derived/cba/$edition/structure.json"
    fixture_path="data/derived/cba/$edition/structure.fixture.json"
    
    if [ -f "$pdf_path" ]; then
        echo "  PDF found: $pdf_path"
        echo "  Regenerating structure..."
        
        python scripts/cba/extract_cba.py \
            --edition "$edition" \
            --pdf "$pdf_path" \
            --output "$structure_path.ci"
        
        if [ -f "$structure_path" ]; then
            echo "  Comparing with committed structure..."
            
            # Compare structure (ignoring generated_at timestamp)
            diff_output=$(diff \
                <(jq 'del(.generated_at)' "$structure_path") \
                <(jq 'del(.generated_at)' "$structure_path.ci") \
                || true)
            
            if [ -n "$diff_output" ]; then
                echo "  ⚠️  Structure mismatch detected!"
                echo "$diff_output"
                echo "  Run: python scripts/cba/extract_cba.py --edition $edition --pdf $pdf_path"
                exit 1
            else
                echo "  ✓ Structure matches committed version"
            fi
            
            rm "$structure_path.ci"
        else
            echo "  ⚠️  No committed structure found, moving generated to main"
            mv "$structure_path.ci" "$structure_path"
        fi
        
        echo "  Validating structure..."
        python scripts/cba/validate_cba_structure.py "$structure_path" --strict
        
    else
        echo "  PDF not found: $pdf_path (skipped)"
        
        # Validate fixture if it exists
        if [ -f "$fixture_path" ]; then
            echo "  Validating fixture..."
            python scripts/cba/validate_cba_structure.py "$fixture_path" --strict --skip-golden-hash
        fi
        
        # Validate committed structure if it exists
        if [ -f "$structure_path" ]; then
            echo "  Validating committed structure..."
            python scripts/cba/validate_cba_structure.py "$structure_path" --strict
        else
            echo "  ℹ️  No structure or fixture to validate"
        fi
    fi
    
    echo
done

echo "=== All validations passed ==="
