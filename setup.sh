#!/bin/bash

# Instagram Bruter - Setup Script
# This script sets up the environment with Python 3.9 and all dependencies

echo "=========================================="
echo "Instagram Bruter - Setup Script"
echo "=========================================="
echo ""

# Step 1: Install Pipenv
echo "[1/4] Installing Pipenv..."
pip install pipenv
if [ $? -eq 0 ]; then
    echo "✓ Pipenv installed successfully"
else
    echo "✗ Failed to install Pipenv"
    exit 1
fi
echo ""

# Step 2: Create Python 3.9 environment
echo "[2/4] Creating Python 3.9 virtual environment..."
pipenv --python 3.9
if [ $? -eq 0 ]; then
    echo "✓ Python 3.9 environment created successfully"
else
    echo "✗ Failed to create Python 3.9 environment"
    echo "Make sure Python 3.9 is installed on your system"
    exit 1
fi
echo ""

# Step 3: Install dependencies
echo "[3/4] Installing dependencies from Pipfile..."
pipenv install
if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "✗ Failed to install dependencies"
    exit 1
fi
echo ""

# Step 4: Verify installation
echo "[4/4] Verifying installation..."
pipenv run python --version
echo ""
echo "=========================================="
echo "✓ Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Activate the environment: pipenv shell"
echo "2. Upload proxies: python instagram.py -px proxies.txt"
echo "3. Check proxy stats: python instagram.py --stats"
echo "4. Start testing: python instagram.py -u <username> -p passwords.txt"
echo ""
