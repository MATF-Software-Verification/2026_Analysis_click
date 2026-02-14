#!/bin/bash
cd "$(dirname "$0")/.."

echo "========================================="
echo "Running Pylint analysis"
echo "========================================="
echo ""

# Create results directory
mkdir -p pylint/results
echo "Analyzing Click source code..."

pylint click/src/click/ \
  --output-format=text \
  --reports=y \
  > pylint/results/report.txt 2>&1

# Extract score
SCORE=$(grep "Your code has been rated at" pylint/results/report.txt | awk '{print $7}')

echo ""
echo "========================================="
echo "Pylint analysis complete!"
echo "========================================="
echo ""
echo "Pylint Score: $SCORE"
echo ""
echo "Report saved to:"
echo "   - pylint/results/report.txt"
