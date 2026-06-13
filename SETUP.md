# Quick Start Guide

## Prerequisites
- Python 3.9 installed
- pip package manager

## Step 1: Install Pipenv
```bash
pip install pipenv
```

## Step 2: Clone/Navigate to Project
```bash
cd Instagram-
```

## Step 3: Create Python 3.9 Environment
```bash
pipenv --python 3.9
```

## Step 4: Install Dependencies
```bash
pipenv install
```

## Step 5: Activate Virtual Environment
```bash
pipenv shell
```

## Step 6: Upload Proxy List to Database
```bash
python instagram.py -px proxies.txt
```

**Output:**
```
<<< Writing proxies to the database >>>
Proxies written to the database: 10
```

## Step 7: Check Proxy Health (Optional)
```bash
python instagram.py --stats
```

**Output:**
```
Total Proxies: 10
Database's Health: Normal
Q1: 0.25 :: Avg Score: 0.65 :: Min Score: 0.1 :: Max Score: 0.95
```

## Step 8: Start Testing

### Run with sample files:
```bash
python instagram.py -u testuser -p passwords.txt
```

### Full command with all options:
```bash
python instagram.py -u <username> -p passwords.txt -px proxies.txt -m 2
```

### Available Modes:
- `-m 0` → 32 bots (fastest, most aggressive)
- `-m 1` → 16 bots
- `-m 2` → 8 bots (default, balanced)
- `-m 3` → 4 bots (slowest, stealthiest)

## Common Commands

### Prune low-performing proxies:
```bash
python instagram.py --prune 0.25
```
(Removes proxies with scores below 25%)

### View help:
```bash
python instagram.py -h
```

### Run without colors:
```bash
python instagram.py -u testuser -p passwords.txt -nc
```

## File Format Requirements

### Proxy List (proxies.txt)
```
ip:port
ip:port
ip:port
```

### Password List (passwords.txt)
```
password1
password2
password3
```

## Troubleshooting

- **ModuleNotFoundError**: Make sure you ran `pipenv install` and `pipenv shell`
- **No proxies in database**: Upload proxies first with `-px` flag
- **Invalid path**: Check that file paths are correct and files exist
- **Permission denied**: Make sure files are readable

## Tips

1. Always upload proxies before running the bruter
2. Check proxy health periodically with `--stats`
3. Prune dead proxies regularly for better performance
4. Start with mode 3 (4 bots) for testing, increase if needed
5. Use a wordlist with common passwords for faster results
