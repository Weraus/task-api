# Task Manager

A full-stack task management application with FastAPI backend and React frontend.

## 🚀 Quick Start

### Option 1: Docker Compose (Recommended)

```bash
# Clone the repository
git clone <your-repo-url>
cd task-api

# Start all services
docker-compose up --build

# Open http://localhost in your browser
```

### Option 2: Local Development

**Backend:**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
# Open http://localhost:5173
```

## 📁 Project Structure

```
task-api/
├── app/
│   ├── __init__.py
│   └── main.py              # FastAPI backend
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── TaskForm.jsx
│   │   │   ├── TaskItem.jsx
│   │   │   └── TaskList.jsx
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   ├── Dockerfile
│   └── nginx.conf
├── .github/workflows/
│   └── ci-cd.yml            # GitHub Actions CI/CD
├── Dockerfile               # Backend Docker
├── docker-compose.yml
├── render.yaml              # Render deployment config
└── requirements.txt
```

## ✨ Features

- ✅ Create, read, update, and delete tasks
- ✅ Toggle task completion status
- ✅ Filter tasks (All / Active / Completed)
- ✅ Responsive dark theme UI
- ✅ Docker containerization
- ✅ CI/CD with GitHub Actions
- ✅ Free cloud hosting on Render

## 🐳 Docker Commands

```bash
# Build and start
docker-compose up --build

# Run in background
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f
```

## 🚀 Deploy to Render (Free)

### Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/task-api.git
git push -u origin main
```

### Step 2: Create Render Account

1. Go to [render.com](https://render.com)
2. Sign up with your GitHub account
3. Click "New" → "Blueprint"
4. Connect your repository
5. Select the `task-api` repo
6. Render will detect `render.yaml` and create services

### Step 3: Configure Environment

1. In Render dashboard, go to your frontend service
2. Add environment variable:
   - `VITE_API_URL` = your backend URL (e.g., `https://task-api-backend.onrender.com`)

### Step 4: Update Frontend API URL

After deployment, update the frontend to use your backend URL:

```javascript
// In frontend/src/App.jsx
const API_URL = 'https://your-backend-url.onrender.com';
```

## 🔧 GitHub Actions CI/CD

The pipeline automatically:

1. **On every push/PR:**
   - Lints backend code with Ruff
   - Builds frontend
   - Runs tests

2. **On push to main:**
   - Builds Docker images
   - Pushes to GitHub Container Registry
   - Triggers Render deployment (if `RENDER_DEPLOY_HOOK` secret is set)

### Setup GitHub Secrets (Optional)

For automatic Render deployments:

1. Go to Render Dashboard → Your Service → Settings
2. Copy the "Deploy Hook" URL
3. Add to GitHub repository secrets as `RENDER_DEPLOY_HOOK`

## 🌐 Free Hosting Options

| Platform | Pros | Cons |
|----------|------|------|
| [Render](https://render.com) | Easy setup, `render.yaml`, free tier | Services sleep after inactivity |
| [Railway](https://railway.app) | Simple, good free tier | Limited free hours |
| [Fly.io](https://fly.io) | Fast, global CDN | Requires CLI setup |
| [Vercel](https://vercel.com) | Great for frontend | Backend needs separate hosting |

## 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API info |
| GET | `/health` | Health check |
| GET | `/tasks` | List all tasks |
| GET | `/tasks?completed=true` | Filter by status |
| GET | `/tasks/{id}` | Get specific task |
| POST | `/tasks` | Create task |
| PUT | `/tasks/{id}` | Update task |
| PATCH | `/tasks/{id}` | Toggle completion |
| DELETE | `/tasks/{id}` | Delete task |

## 🛠️ Tech Stack

**Backend:**
- FastAPI
- Pydantic v2
- Uvicorn

**Frontend:**
- React 19
- Vite
- Modern CSS (dark theme)

**DevOps:**
- Docker & Docker Compose
- GitHub Actions
- Render (hosting)

## 📝 License

MIT
