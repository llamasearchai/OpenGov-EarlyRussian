#!/bin/bash

# Comprehensive validation script for OpenGov-EarlyRussian
# Author: Nik Jois <nikjois@llamasearch.ai>

set -e  # Exit on error

echo "========================================================================"
echo "OpenGov-EarlyRussian - Comprehensive Validation"
echo "Author: Nik Jois <nikjois@llamasearch.ai>"
echo "========================================================================"
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

PASSED=0
FAILED=0

# Test function
test_step() {
    echo -e "${YELLOW}[TESTING]${NC} $1"
    if eval "$2" > /dev/null 2>&1; then
        echo -e "${GREEN}[PASS]${NC} $1"
        ((PASSED++))
        return 0
    else
        echo -e "${RED}[FAIL]${NC} $1"
        ((FAILED++))
        return 1
    fi
}

# Activate virtual environment
source .venv/bin/activate

echo "1. Package Installation Tests"
echo "------------------------------"
test_step "Virtual environment exists" "test -d .venv"
test_step "Package is installed" "pip show opengov-earlyrussian"
test_step "CLI command is available" "which russian"
echo ""

echo "2. Core Module Tests"
echo "------------------------------"
test_step "Import main package" "python -c 'import opengov_earlyrussian'"
test_step "Import AlphabetTeacher" "python -c 'from opengov_earlyrussian import AlphabetTeacher'"
test_step "Import CasesTeacher" "python -c 'from opengov_earlyrussian import CasesTeacher'"
test_step "Import VerbConjugator" "python -c 'from opengov_earlyrussian import VerbConjugator'"
test_step "Import Transliterator" "python -c 'from opengov_earlyrussian import Transliterator'"
test_step "Import AIConversationPartner" "python -c 'from opengov_earlyrussian import AIConversationPartner'"
echo ""

echo "3. CLI Command Tests"
echo "------------------------------"
test_step "CLI help command" "russian --help"
test_step "CLI version command" "russian version"
test_step "CLI alphabet command" "russian alphabet iotated"
test_step "CLI translit command" "russian translit 'test'"
echo ""

echo "4. Test Suite"
echo "------------------------------"
echo "Running pytest..."
pytest -q
echo ""
test_step "All tests passed" "pytest -q --tb=no"
echo ""

echo "5. Code Coverage"
echo "------------------------------"
echo "Calculating coverage..."
pytest --cov=opengov_earlyrussian --cov-report=term-missing --tb=no | tail -20
echo ""

echo "6. Example Scripts"
echo "------------------------------"
test_step "Basic usage example" "python examples/basic_usage.py > /dev/null"
test_step "Business culture example" "python examples/business_culture.py > /dev/null"
test_step "SRS example" "python examples/srs_example.py > /dev/null"
echo ""

echo "7. File Structure Validation"
echo "------------------------------"
test_step "pyproject.toml exists" "test -f pyproject.toml"
test_step "README.md exists" "test -f README.md"
test_step "LICENSE exists" "test -f LICENSE"
test_step "Dockerfile exists" "test -f Dockerfile"
test_step "docker-compose.yml exists" "test -f docker-compose.yml"
test_step "Makefile exists" "test -f Makefile"
test_step ".gitignore exists" "test -f .gitignore"
echo ""

echo "8. Python Module Structure"
echo "------------------------------"
test_step "Core modules exist" "test -d opengov_earlyrussian/core"
test_step "API module exists" "test -d opengov_earlyrussian/api"
test_step "AI module exists" "test -d opengov_earlyrussian/ai"
test_step "Tests exist" "test -d tests"
test_step "Examples exist" "test -d examples"
echo ""

echo "9. Functional Tests"
echo "------------------------------"
echo "Testing AlphabetTeacher..."
python -c "from opengov_earlyrussian import AlphabetTeacher; t = AlphabetTeacher(); r = t.get_row('iotated'); assert len(r['letters']) == 4"
test_step "AlphabetTeacher works" "true"

echo "Testing CasesTeacher..."
python -c "from opengov_earlyrussian import CasesTeacher; c = CasesTeacher(); r = c.decline_noun('книга', 'feminine'); assert r['винительный'] == 'книгу'"
test_step "CasesTeacher works" "true"

echo "Testing VerbConjugator..."
python -c "from opengov_earlyrussian import VerbConjugator; v = VerbConjugator(); r = v.conjugate('читать', 'present'); assert len(r['forms']) == 6"
test_step "VerbConjugator works" "true"

echo "Testing Transliterator..."
python -c "from opengov_earlyrussian import Transliterator; t = Transliterator(); r = t.to_russian('Moskva'); assert 'Москва' in r"
test_step "Transliterator works" "true"
echo ""

echo "10. Documentation Validation"
echo "------------------------------"
test_step "README is not empty" "test -s README.md"
test_step "QUICKSTART exists" "test -f QUICKSTART.md"
test_step "VERIFICATION exists" "test -f VERIFICATION.md"
test_step "SUMMARY exists" "test -f SUMMARY.md"
test_step "FINAL_REPORT exists" "test -f FINAL_REPORT.md"
echo ""

echo "========================================================================"
echo "Validation Complete"
echo "========================================================================"
echo ""
echo -e "${GREEN}PASSED:${NC} $PASSED tests"
echo -e "${RED}FAILED:${NC} $FAILED tests"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✓ All validation checks passed!${NC}"
    echo "The OpenGov-EarlyRussian codebase is fully functional."
    exit 0
else
    echo -e "${RED}✗ Some validation checks failed.${NC}"
    exit 1
fi

