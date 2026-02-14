#!/bin/bash


echo "========================================="
echo "🔍 Running Pylint analysis"
echo "========================================="
echo ""

# Run Pylint
echo "Analyzing Click source code..."
pylint ../click/src/click/ \
  --output-format=text \
  --reports=y \
  > reports/report.txt 2>&1

# Extract score
SCORE=$(grep "Your code has been rated at" reports/report.txt | awk '{print $7}')

echo ""
echo "========================================="
echo "✅ Pylint analysis complete!"
echo "========================================="
echo ""
echo "📊 Pylint Score: $SCORE"
echo ""
echo "📄 Reports saved to:"
echo "   - pylint/reports/report.txt"
echo ""
