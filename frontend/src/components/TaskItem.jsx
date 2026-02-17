function TaskItem({ task, onToggle, onEdit, onDelete }) {
  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  return (
    <div className={`task-item ${task.completed ? 'completed' : ''}`}>
      <div className="task-checkbox">
        <input
          type="checkbox"
          checked={task.completed}
          onChange={() => onToggle(task.id, !task.completed)}
        />
      </div>
      <div className="task-content">
        <h3 className="task-title">{task.title}</h3>
        {task.description && (
          <p className="task-description">{task.description}</p>
        )}
        <span className="task-date">{formatDate(task.created_at)}</span>
      </div>
      <div className="task-actions">
        <button 
          className="btn-icon btn-edit" 
          onClick={() => onEdit(task)}
          title="Edit task"
        >
          ✏️
        </button>
        <button 
          className="btn-icon btn-delete" 
          onClick={() => onDelete(task.id)}
          title="Delete task"
        >
          🗑️
        </button>
      </div>
    </div>
  );
}

export default TaskItem;
