# Task Manager

A full-stack task management application with FastAPI backend and React frontend.

## 🚀 Quick Start (Docker)

```bash
cd repos/task-api
docker-compose up --build
# Open http://localhost
```

---

## 🌐 Free Deployment (No Credit Card)

### Architecture

```
Frontend (Vercel) ──→ Backend (PythonAnywhere)
     Free                    Free
   No card                 No card
```

---

## 📦 Deploy Backend to PythonAnywhere

### 1. Create Account
- Go to [pythonanywhere.com](https://www.pythonanywhere.com)
- Sign up for **Beginner** (free) account

### 2. Upload Code via Git
In PythonAnywhere **Bash console**:
```bash
git clone https://github.com/YOUR_USERNAME/task-api.git
cd task-api
```

### 3. Create Virtual Environment
```bash
mkvirtualenv --python=/usr/bin/python3.12 venv
pip install -r requirements.txt
```

### 4. Create Web App
1. Go to **Web** tab
2. Click **Add a new web app**
3. Choose your domain: `yourusername.pythonanywhere.com`
4. Select **Manual configuration** → **Python 3.12**

### 5. Configure Web App

**Virtual environment:**
```
/home/yourusername/task-api/venv
```

**WSGI configuration file** (click to edit):
```python
import sys
import os

project_home = '/home/yourusername/task-api'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

from wsgi import application
```

### 6. Reload
Click **Reload** button

### 7. Test
Your API: `https://yourusername.pythonanywhere.com`
- `GET /tasks` - List tasks
- `POST /tasks` - Create task
- `GET /docs` - API documentation

---

## 🎨 Deploy Frontend to Vercel

### 1. Import Project
1. Go to [vercel.com](https://vercel.com)
2. Sign in with GitHub
3. Click **Add New** → **Project**
4. Import `task-api` repository

### 2. Configure
- **Root Directory**: `frontend`
- **Framework Preset**: Vite (auto-detected)

### 3. Add Environment Variable
- **Name**: `VITE_API_URL`
- **Value**: `https://yourusername.pythonanywhere.com`

### 4. Deploy
Click **Deploy**

Your frontend: `https://task-api.vercel.app`

---

## 🔄 CI/CD Pipeline

GitHub Actions automatically:
- Lints code on every push/PR
- Builds frontend
- Tests Docker container

Both PythonAnywhere and Vercel auto-deploy on push:
- **Vercel**: Automatic
- **PythonAnywhere**: Enable "Always on" or manual reload

---

## 📁 Project Structure

```
task-api/
├── app/
│   └── main.py              # FastAPI backend (SQLite)
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── App.jsx
│   │   └── App.css
│   ├── vercel.json
│   └── package.json
├── wsgi.py                  # WSGI entry (PythonAnywhere)
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .github/workflows/
```

---

## ✨ Features

- ✅ CRUD operations for tasks
- ✅ SQLite storage (persistent)
- ✅ Dark theme UI
- ✅ Filter: All / Active / Completed
- ✅ Mobile responsive
- ✅ Docker support
- ✅ CI/CD included

---

## 🛠️ Tech Stack

| Backend | Frontend |
|---------|----------|
| FastAPI | React 19 |
| SQLite | Vite |
| Pydantic | Modern CSS |
| a2wsgi | Vercel |

---

## 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API info |
| GET | `/health` | Health check |
| GET | `/tasks` | List all tasks |
| GET | `/tasks?completed=true` | Filter tasks |
| POST | `/tasks` | Create task |
| PUT | `/tasks/{id}` | Update task |
| PATCH | `/tasks/{id}` | Toggle completion |
| DELETE | `/tasks/{id}` | Delete task |

---

## ⚠️ PythonAnywhere Free Tier Limits

- 512 MB storage
- 2,000 CPU seconds/day
- One web app
- Sleeps after inactivity (wake up on request)

---

## 🔧 Local Development

```bash
# Backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# Frontend
cd frontend && npm install && npm run dev
```
