#!/bin/bash
cd "$(dirname "$0")/.."

echo "========================================="
echo "Running Bandit security analysis"
echo "========================================="
echo ""

# Create results directory
mkdir -p bandit/results
echo "Scanning Click source code for security issues..."

# Run Bandit - text format
bandit -r click/src/click/ \
  -f txt \
  -o bandit/results/report.txt

# Also generate JSON format
bandit -r click/src/click/ \
  -f json \
  -o bandit/results/report.json \
  2>/dev/null

# Extract summary
ISSUES=$(grep -c ">> Issue:" bandit/results/report.txt 2>/dev/null || echo "0")
SEVERITY_HIGH=$(grep "Severity: High" bandit/results/report.txt | wc -l | tr -d ' ')
SEVERITY_MEDIUM=$(grep "Severity: Medium" bandit/results/report.txt | wc -l | tr -d ' ')
SEVERITY_LOW=$(grep "Severity: Low" bandit/results/report.txt | wc -l | tr -d ' ')

echo ""
echo "========================================="
echo "Bandit analysis complete!"
echo "========================================="
echo ""
echo "Security Issues Found: $ISSUES"
echo "   - High:   $SEVERITY_HIGH"
echo "   - Medium: $SEVERITY_MEDIUM"
echo "   - Low:    $SEVERITY_LOW"
echo ""
echo "Reports saved to:"
echo "   - bandit/results/report.txt"
echo "   - bandit/results/report.json"
