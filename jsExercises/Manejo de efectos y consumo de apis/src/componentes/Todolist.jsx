import React, { useState, useEffect } from 'react';

function TodoList() {
  const [todos, setTodos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('https://jsonplaceholder.typicode.com/todos');
        if (!response.ok) {
          throw new Error('Failed to fetch data');
        }
        const data = await response.json();
        setTodos(data);
        setLoading(false);
      } catch (error) {
        setError(error.message);
        setLoading(false);
      }
    };

    fetchData();
  }, []);



  return (
    <div>
      <h1>Todo List</h1>
      <ul>
        {todos
          .filter(todo => todo.completed === true)
          .map(todo => (
            <li key={todo.id}>{todo.title}</li>
          ))}
      </ul>
    </div>
  );
}
export default TodoList