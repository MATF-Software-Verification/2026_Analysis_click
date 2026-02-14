#!/bin/bash
cd "$(dirname "$0")"

echo "========================================="
echo "Running all analysis"
echo "========================================="
echo ""

./pytest/run_pytest.sh
echo ""

./coverage/run_coverage.sh
echo ""

./pylint/run_pylint.sh
echo ""

./mypy/run_mypy.sh
echo ""

./bandit/run_bandit.sh
echo ""

./radon/run_radon.sh
echo ""

./black/run_black.sh
echo ""

echo "========================================="
echo "Analysis completed!"
echo "========================================="
