#!/bin/bash
cd "$(dirname "$0")/.."

echo "========================================="
echo "Running Black code formatting check"
echo "========================================="
echo ""

# Create results directory
mkdir -p black/results

echo "Checking code formatting..."

# Run Black in check mode (doesn't modify files)
black --check --diff click/src/click/ > black/results/report.txt 2>&1

# Get exit code
EXIT_CODE=$?

# Count files that would be reformatted
FILES_TO_FORMAT=$(grep "would reformat" black/results/report.txt | wc -l | tr -d ' ')
FILES_OK=$(grep "would be left unchanged" black/results/report.txt | wc -l | tr -d ' ')

echo ""
echo "========================================="
echo "Black analysis complete!"
echo "========================================="
echo ""

if [ $EXIT_CODE -eq 0 ]; then
    echo "All files are properly formatted!"
    echo "   Files checked: $FILES_OK"
else
    echo "Formatting issues found"
    echo "   Files needing formatting: $FILES_TO_FORMAT"
    echo "   Files already formatted: $FILES_OK"
fi

echo ""
echo "Report saved to:"
echo "   - black/results/report.txt"
echo ""
echo "To auto-format files:"
echo "   black click/src/click/"
