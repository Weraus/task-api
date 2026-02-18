# Task Manager

A full-stack task management application with FastAPI backend and React frontend.

## 🚀 Quick Start

### Option 1: Docker Compose (Recommended)

```bash
docker-compose up --build
# Open http://localhost
```

### Option 2: Local Development

**Backend:**
```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend && npm install && npm run dev
# Open http://localhost:5173
```

---

## 🌐 Free Hosting Options

> ⚠️ **Note:** Render discontinued their free web service tier (Jan 2025)

### Option 1: Railway.app (Recommended - $5 free credit/month)

1. Go to [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select `task-api` repository
5. Railway auto-detects Dockerfile
6. Add environment variable: `PYTHONUNBUFFERED=1`
7. Deploy!

**Frontend on Vercel (Free):**
1. Go to [vercel.com](https://vercel.com)
2. Import your GitHub repo
3. Set "Root Directory" to `frontend`
4. Add env var `VITE_API_URL` = your Railway backend URL
5. Deploy!

### Option 2: Fly.io (Free allowance)

```bash
# Install flyctl
curl -L https://fly.io/install.sh | sh

# Login
fly auth login

# Deploy backend
fly apps create task-api-backend
fly deploy

# Note: Free tier gives ~3 small VMs free
```

### Option 3: Koyeb (Free tier available)

1. Go to [koyeb.com](https://www.koyeb.com)
2. Sign in with GitHub
3. Create new app → Docker
4. Select your repo
5. Deploy!

### Option 4: PythonAnywhere (Free for backend)

Good for Python backends, but requires paid plan for custom domains.

---

## 🐳 Docker Commands

```bash
docker-compose up --build    # Build and start
docker-compose up -d         # Run in background
docker-compose down          # Stop services
docker-compose logs -f       # View logs
```

---

## 📁 Project Structure

```
task-api/
├── app/main.py              # FastAPI backend
├── frontend/                # React + Vite
│   ├── src/components/
│   └── Dockerfile
├── Dockerfile               # Backend container
├── docker-compose.yml
├── .github/workflows/       # CI/CD
├── railway.toml             # Railway config
├── fly.toml                 # Fly.io config
└── vercel.json              # Vercel config
```

---

## ✨ Features

- ✅ CRUD operations for tasks
- ✅ Filter by completion status
- ✅ Dark theme UI
- ✅ Docker containerization
- ✅ CI/CD with GitHub Actions
- ✅ Multiple hosting configs

---

## 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/tasks` | List all tasks |
| POST | `/tasks` | Create task |
| PUT | `/tasks/{id}` | Update task |
| DELETE | `/tasks/{id}` | Delete task |

---

## 🛠️ Tech Stack

- **Backend:** FastAPI, Pydantic v2, Uvicorn
- **Frontend:** React 19, Vite
- **DevOps:** Docker, GitHub Actions
- **Hosting:** Railway / Fly.io / Vercel
