#!/bin/bash
cd "$(dirname "$0")/.."

echo "========================================="
echo "Running MyPy type checking"
echo "========================================="
echo ""

mkdir -p mypy/results
echo "Analyzing Click source code..."

# Run MyPy
mypy click/src/click/ \
  --show-error-codes \
  --show-column-numbers \
  --pretty \
  --html-report mypy/results \
  --txt-report mypy/results \
  > mypy/results/report.txt 2>&1

# Count errors
ERROR_COUNT=$(grep -c "error:" mypy/results/report.txt 2>/dev/null || echo "0")

echo ""
echo "========================================="
echo "MyPy analysis complete!"
echo "========================================="
echo ""
echo "Type Errors Found: $ERROR_COUNT"
echo ""
echo "Reports saved to:"
echo "   - mypy/results/report.txt (text)"
echo "   - mypy/results/index.html (HTML)"
echo ""
echo "View HTML report:"
echo "   open mypy/results/index.html"
