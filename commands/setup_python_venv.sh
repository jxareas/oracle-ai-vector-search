#!/bin/bash
# ===============================================================
# Setup a Python Virtual Environment
# ===============================================================
# Check the Python version, create a virtual environment at
# .venv/oraivect if it doesn't exist, and instruct the user on
# how to activate and use it.
#
# Requirements:
#   • Python 3.8 or higher
#
# After activation:
#   • Install module dependencies with:
#       pip install -r path/to/module/requirements.txt
#   • Exit the environment with:
#       deactivate
# ===============================================================

# Minimum required Python version
REQUIRED_PYTHON=3.8
VENV_DIR=".venv/oraivect"

# ---------------------------------------------------------------
# Step 1: Verify Python version
# ---------------------------------------------------------------
echo "Checking Python version..."
PYTHON_VERSION=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:3])))' 2>/dev/null)

if [ $? -ne 0 ]; then
    echo "❌ Python is not installed or not in PATH."
    exit 1
fi

if [ "$(printf '%s\n' "$REQUIRED_PYTHON" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_PYTHON" ]; then
    echo "❌ Python $REQUIRED_PYTHON or higher is required (found $PYTHON_VERSION)."
    exit 1
fi
echo "✅ Python version $PYTHON_VERSION is sufficient."

# ---------------------------------------------------------------
# Step 2: Create virtual environment
# ---------------------------------------------------------------
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment at $VENV_DIR ..."
    python -m venv "$VENV_DIR"
    echo "✅ Virtual environment created."
else
    echo "✅ Virtual environment already exists at $VENV_DIR."
fi

# ---------------------------------------------------------------
# Step 3: Instruct user to activate environment
# ---------------------------------------------------------------
echo ""
echo "---------------------------------------------------------------"
echo "👉 ACTIVATE THE VIRTUAL ENVIRONMENT:"
echo "   • macOS / Linux:"
echo "       source $VENV_DIR/bin/activate"
echo ""
echo "   • Windows PowerShell:"
echo "       .venv\\oraivect\\Scripts\\Activate.ps1"
echo ""
echo "Once activated, install module dependencies:"
echo "   pip install -r requirements.txt"
echo ""
echo "To exit the environment:"
echo "   deactivate"
echo "---------------------------------------------------------------"
