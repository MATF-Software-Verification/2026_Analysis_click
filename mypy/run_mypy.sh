#!/bin/bash

echo "========================================="
echo "🔍 Running MyPy type checking"
echo "========================================="
echo ""

echo "Analyzing Click source code..."

# Run MyPy
mypy ../click/src/click/  \
  --show-error-codes \
  --show-column-numbers \
  --pretty \
  --html-report reports/ \
  --txt-report reports/ \
  > reports/report.txt 2>&1

# Count errors
ERROR_COUNT=$(grep -c "error:" reports/report.txt 2>/dev/null || echo "0")

echo ""
echo "========================================="
echo "✅ MyPy analysis complete!"
echo "========================================="
echo ""
echo "📊 Type Errors Found: $ERROR_COUNT"
echo ""
echo "📄 Reports saved to:"
echo "   - mypy/reports/report.txt (text)"
echo "   - mypy/reports/index.html (HTML)"
echo ""
echo "View report:"
echo "   cat mypy/reports/report.txt"
echo "   open mypy/reports/index.html"