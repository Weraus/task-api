import TaskItem from './TaskItem';

function TaskList({ tasks, onToggle, onEdit, onDelete, filter, onFilterChange }) {
  const filteredTasks = tasks.filter(task => {
    if (filter === 'active') return !task.completed;
    if (filter === 'completed') return task.completed;
    return true;
  });

  const activeCount = tasks.filter(t => !t.completed).length;
  const completedCount = tasks.filter(t => t.completed).length;

  return (
    <div className="task-list-container">
      <div className="task-filters">
        <button 
          className={`filter-btn ${filter === 'all' ? 'active' : ''}`}
          onClick={() => onFilterChange('all')}
        >
          All ({tasks.length})
        </button>
        <button 
          className={`filter-btn ${filter === 'active' ? 'active' : ''}`}
          onClick={() => onFilterChange('active')}
        >
          Active ({activeCount})
        </button>
        <button 
          className={`filter-btn ${filter === 'completed' ? 'active' : ''}`}
          onClick={() => onFilterChange('completed')}
        >
          Completed ({completedCount})
        </button>
      </div>
      
      <div className="task-list">
        {filteredTasks.length === 0 ? (
          <div className="empty-state">
            <p>No tasks {filter !== 'all' ? `(${filter})` : ''}</p>
            <p className="empty-hint">Add a new task to get started!</p>
          </div>
        ) : (
          filteredTasks.map(task => (
            <TaskItem
              key={task.id}
              task={task}
              onToggle={onToggle}
              onEdit={onEdit}
              onDelete={onDelete}
            />
          ))
        )}
      </div>
    </div>
  );
}

export default TaskList;
