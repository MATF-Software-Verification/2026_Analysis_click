#!/bin/bash
cd "$(dirname "$0")/.."

echo "========================================="
echo "Running Coverage analysis"
echo "========================================="
echo ""

mkdir -p coverage/results

echo "Running tests with coverage..."

pytest click/tests/ unit_tests/ \
  --cov=click/src/click \
  --cov-report=html:coverage/results/html \
  --cov-report=term-missing \
  2>&1 | tee coverage/results/report.txt

echo ""
echo "========================================="
echo "Coverage analysis complete!"
echo "========================================="
echo ""
echo "Reports saved to:"
echo "   - coverage/results/report.txt"
echo "   - coverage/results/html/index.html"
