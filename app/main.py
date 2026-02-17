"""
Simple Task Management API
A FastAPI backend for managing tasks with CRUD operations.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid

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

# In-memory database
tasks_db = {}


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
    tasks = list(tasks_db.values())
    if completed is not None:
        tasks = [t for t in tasks if t["completed"] == completed]
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: str):
    """Get a specific task by ID."""
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]


@app.post("/tasks", response_model=Task, status_code=201)
async def create_task(task: TaskCreate):
    """Create a new task."""
    task_id = str(uuid.uuid4())
    now = datetime.now()
    new_task = {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
        "created_at": now,
        "updated_at": now
    }
    tasks_db[task_id] = new_task
    return new_task


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: str, task: TaskCreate):
    """Update an existing task."""
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    
    existing_task = tasks_db[task_id]
    updated_task = {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
        "created_at": existing_task["created_at"],
        "updated_at": datetime.now()
    }
    tasks_db[task_id] = updated_task
    return updated_task


@app.patch("/tasks/{task_id}", response_model=Task)
async def partial_update_task(task_id: str, completed: bool):
    """Partially update a task (toggle completion)."""
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    
    tasks_db[task_id]["completed"] = completed
    tasks_db[task_id]["updated_at"] = datetime.now()
    return tasks_db[task_id]


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    """Delete a task."""
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    
    del tasks_db[task_id]
    return {"message": "Task deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
