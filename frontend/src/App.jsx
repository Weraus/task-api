import { useState, useEffect } from 'react';
import TaskForm from './components/TaskForm';
import TaskList from './components/TaskList';
import './App.css';

// API URL - set VITE_API_URL in Vercel environment variables
// Example: VITE_API_URL=https://yourusername.pythonanywhere.com
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

function App() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [filter, setFilter] = useState('all');
  const [editingTask, setEditingTask] = useState(null);
  const [showForm, setShowForm] = useState(false);

  // Fetch all tasks
  const fetchTasks = async () => {
    try {
      setLoading(true);
      const response = await fetch(`${API_URL}/tasks`);
      if (!response.ok) throw new Error('Failed to fetch tasks');
      const data = await response.json();
      setTasks(data);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  // Create task
  const createTask = async (taskData) => {
    try {
      const response = await fetch(`${API_URL}/tasks`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(taskData),
      });
      if (!response.ok) throw new Error('Failed to create task');
      const newTask = await response.json();
      setTasks([...tasks, newTask]);
      setShowForm(false);
    } catch (err) {
      setError(err.message);
    }
  };

  // Update task
  const updateTask = async (taskId, taskData) => {
    try {
      const response = await fetch(`${API_URL}/tasks/${taskId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(taskData),
      });
      if (!response.ok) throw new Error('Failed to update task');
      const updatedTask = await response.json();
      setTasks(tasks.map(t => t.id === taskId ? updatedTask : t));
      setEditingTask(null);
    } catch (err) {
      setError(err.message);
    }
  };

  // Toggle task completion
  const toggleTask = async (taskId, completed) => {
    try {
      const response = await fetch(`${API_URL}/tasks/${taskId}?completed=${completed}`, {
        method: 'PATCH',
      });
      if (!response.ok) throw new Error('Failed to update task');
      const updatedTask = await response.json();
      setTasks(tasks.map(t => t.id === taskId ? updatedTask : t));
    } catch (err) {
      setError(err.message);
    }
  };

  // Delete task
  const deleteTask = async (taskId) => {
    try {
      const response = await fetch(`${API_URL}/tasks/${taskId}`, {
        method: 'DELETE',
      });
      if (!response.ok) throw new Error('Failed to delete task');
      setTasks(tasks.filter(t => t.id !== taskId));
    } catch (err) {
      setError(err.message);
    }
  };

  const handleSubmit = (taskData) => {
    if (editingTask) {
      updateTask(editingTask.id, taskData);
    } else {
      createTask(taskData);
    }
  };

  const handleEdit = (task) => {
    setEditingTask(task);
    setShowForm(true);
  };

  const handleCancelEdit = () => {
    setEditingTask(null);
    setShowForm(false);
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>📋 Task Manager</h1>
        <p className="subtitle">Stay organized, get things done</p>
      </header>

      <main className="app-main">
        {error && (
          <div className="error-banner">
            <span>⚠️ {error}</span>
            <button onClick={() => setError(null)}>✕</button>
          </div>
        )}

        <div className="add-task-section">
          {!showForm ? (
            <button 
              className="btn btn-primary btn-large"
              onClick={() => setShowForm(true)}
            >
              + Add New Task
            </button>
          ) : (
            <div className="form-container">
              <h2>{editingTask ? 'Edit Task' : 'New Task'}</h2>
              <TaskForm
                onSubmit={handleSubmit}
                onCancel={handleCancelEdit}
                initialData={editingTask}
              />
            </div>
          )}
        </div>

        {loading ? (
          <div className="loading">
            <div className="spinner"></div>
            <p>Loading tasks...</p>
          </div>
        ) : (
          <TaskList
            tasks={tasks}
            onToggle={toggleTask}
            onEdit={handleEdit}
            onDelete={deleteTask}
            filter={filter}
            onFilterChange={setFilter}
          />
        )}
      </main>

      <footer className="app-footer">
        <p>Task Manager API • FastAPI + React</p>
      </footer>
    </div>
  );
}

export default App;
