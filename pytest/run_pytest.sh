#!/bin/bash
cd "$(dirname "$0")/.."

echo "========================================="
echo "Running Pytest unit tests"
echo "========================================="
echo ""

echo "Running unit tests..."

pytest unit_tests/ -v 2>&1 | tee pytest/results/report.txt

echo ""
echo "========================================="
echo "Pytest complete!"
echo "========================================="
echo ""
echo "Report saved to:"
echo "   - pytest/results/report.txt"
