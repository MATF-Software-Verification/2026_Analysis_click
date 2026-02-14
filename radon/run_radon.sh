#!/bin/bash
cd "$(dirname "$0")/.."

echo "========================================="
echo "Running Radon complexity analysis"
echo "========================================="
echo ""

# Create results directory
mkdir -p radon/results

echo "Analyzing code complexity..."

# Cyclomatic Complexity
echo "1. Cyclomatic Complexity..." >&2
radon cc click/src/click/ -a -s > radon/results/complexity.txt 2>&1

# Maintainability Index
echo "2. Maintainability Index..." >&2
radon mi click/src/click/ -s >> radon/results/complexity.txt 2>&1

# Raw metrics
echo "3. Raw Metrics..." >&2
radon raw click/src/click/ -s >> radon/results/complexity.txt 2>&1

# Extract average complexity
AVG_COMPLEXITY=$(grep "Average complexity:" radon/results/complexity.txt | head -1 | awk '{print $3}')

echo ""
echo "========================================="
echo "Radon analysis complete!"
echo "========================================="
echo ""
echo "Average Complexity: ${AVG_COMPLEXITY:-N/A}"
echo ""
echo "Report saved to:"
echo "   - radon/results/complexity.txt"
