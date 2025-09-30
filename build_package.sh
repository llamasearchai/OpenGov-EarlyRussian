#!/bin/bash

# Package build script for OpenGov-EarlyRussian
# Author: Nik Jois <nikjois@llamasearch.ai>

set -e

echo "========================================"
echo "OpenGov-EarlyRussian Package Builder"
echo "Author: Nik Jois"
echo "========================================"
echo ""

# Activate virtual environment
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

source .venv/bin/activate

# Install build tools
echo "[1/7] Installing build dependencies..."
pip install --upgrade pip build twine >&/dev/null

# Clean previous builds
echo "[2/7] Cleaning previous builds..."
rm -rf build/ dist/ *.egg-info/

# Run tests
echo "[3/7] Running test suite..."
pytest -q

# Format code
echo "[4/7] Formatting code..."
black opengov_earlyrussian tests examples >&/dev/null

# Build package
echo "[5/7] Building distribution packages..."
python -m build

# Check package
echo "[6/7] Checking package..."
twine check dist/*

# Display build info
echo "[7/7] Build complete!"
echo ""
echo "Built packages:"
ls -lh dist/
echo ""

echo "========================================"
echo "Build successful!"
echo "========================================"
echo ""
echo "To install locally:"
echo "  pip install dist/opengov_earlyrussian-*.whl"
echo ""
echo "To upload to PyPI (with proper credentials):"
echo "  twine upload dist/*"
echo ""

