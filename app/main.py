"""
Simple Task Management API
A FastAPI backend for managing tasks with CRUD operations.
Uses SQLite for persistent storage (works on PythonAnywhere).
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid
import sqlite3
import json
import os

# Database path - works locally and on PythonAnywhere
DB_PATH = os.environ.get('DB_PATH', 'tasks.db')

app = FastAPI(
    title="Task Management API",
    description="A simple API for managing tasks",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Database helpers
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize database on startup."""
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            completed INTEGER DEFAULT 0,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# Initialize DB on module load
init_db()


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


def row_to_dict(row):
    """Convert SQLite row to dict with proper types."""
    return {
        "id": row["id"],
        "title": row["title"],
        "description": row["description"],
        "completed": bool(row["completed"]),
        "created_at": row["created_at"],
        "updated_at": row["updated_at"]
    }


@app.get("/")
async def root():
    """Root endpoint returning API info."""
    return {
        "message": "Task Management API",
        "version": "1.0.0",
        "endpoints": {
            "tasks": "/tasks",
            "docs": "/docs",
            "health": "/health"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


@app.get("/tasks", response_model=list[Task])
async def get_tasks(completed: Optional[bool] = None):
    """Get all tasks, optionally filtered by completion status."""
    conn = get_db()
    if completed is not None:
        rows = conn.execute(
            "SELECT * FROM tasks WHERE completed = ?",
            (1 if completed else 0,)
        ).fetchall()
    else:
        rows = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return [row_to_dict(row) for row in rows]


@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: str):
    """Get a specific task by ID."""
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()
    conn.close()
    
    if not row:
        raise HTTPException(status_code=404, detail="Task not found")
    return row_to_dict(row)


@app.post("/tasks", response_model=Task, status_code=201)
async def create_task(task: TaskCreate):
    """Create a new task."""
    task_id = str(uuid.uuid4())
    now = datetime.now().isoformat()
    
    conn = get_db()
    conn.execute(
        "INSERT INTO tasks (id, title, description, completed, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
        (task_id, task.title, task.description, 1 if task.completed else 0, now, now)
    )
    conn.commit()
    conn.close()
    
    return {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
        "created_at": now,
        "updated_at": now
    }


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: str, task: TaskCreate):
    """Update an existing task."""
    conn = get_db()
    row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    
    if not row:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")
    
    now = datetime.now().isoformat()
    conn.execute(
        "UPDATE tasks SET title = ?, description = ?, completed = ?, updated_at = ? WHERE id = ?",
        (task.title, task.description, 1 if task.completed else 0, now, task_id)
    )
    conn.commit()
    conn.close()
    
    return {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
        "created_at": row["created_at"],
        "updated_at": now
    }


@app.patch("/tasks/{task_id}", response_model=Task)
async def partial_update_task(task_id: str, completed: bool):
    """Partially update a task (toggle completion)."""
    conn = get_db()
    row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    
    if not row:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")
    
    now = datetime.now().isoformat()
    conn.execute(
        "UPDATE tasks SET completed = ?, updated_at = ? WHERE id = ?",
        (1 if completed else 0, now, task_id)
    )
    conn.commit()
    conn.close()
    
    return {
        "id": task_id,
        "title": row["title"],
        "description": row["description"],
        "completed": completed,
        "created_at": row["created_at"],
        "updated_at": now
    }


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    """Delete a task."""
    conn = get_db()
    row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    
    if not row:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")
    
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    
    return {"message": "Task deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
