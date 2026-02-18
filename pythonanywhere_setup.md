# PythonAnywhere Setup Instructions

## Step 1: Create Account
1. Go to [pythonanywhere.com](https://www.pythonanywhere.com)
2. Sign up for **Beginner** (free) account

## Step 2: Create Web App
1. Go to **Web** tab
2. Click **Add a new web app**
3. Choose your domain: `yourusername.pythonanywhere.com`
4. Select **Manual configuration**
5. Choose **Python 3.12**

## Step 3: Upload Code
Option A: Upload files manually
- Go to **Files** tab
- Create folder: `task-api`
- Upload all project files

Option B: Clone from GitHub
- Go to **Consoles** tab → Bash
- Run: `git clone https://github.com/YOUR_USERNAME/task-api.git`

## Step 4: Setup Virtual Environment
In Bash console:
```bash
cd task-api
mkvirtualenv --python=/usr/bin/python3.12 venv
pip install -r requirements.txt
```

## Step 5: Configure Web App
Go to **Web** tab, edit your app:

### Virtual environment:
```
/home/yourusername/task-api/venv
```

### WSGI configuration file:
Edit the WSGI file and replace with:
```python
import sys
import os

# Add project to path
project_home = '/home/yourusername/task-api'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Import WSGI application
from wsgi import application
```

### Static files (optional):
- URL: `/static` → Directory: `/home/yourusername/task-api/static`

## Step 6: Reload
Click **Reload** button in Web tab

## Step 7: Test
Your API will be at: `https://yourusername.pythonanywhere.com`

## Important Notes
- Free tier: 512MB storage, 2,000 CPU-seconds/day
- Tasks are stored in memory (reset on reload)
- For persistent storage, consider adding SQLite
