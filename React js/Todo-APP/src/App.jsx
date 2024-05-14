import { useState } from "react";
import "./App.css";
import TodoForm from "./components/TodoForm";
import TodoHeader from "./components/TodoHeader";
import TodoList from "./components/TodoList";

function App() {
  const [todos, setTodos] = useState([]);
  const todoDoneHandler = (id) => {
    const updatedTodos = todos.map((todo,index) =>
      index === id ? { ...todo, isDone: true } : todo
    );
    setTodos(updatedTodos);
  };
  const todoUndoHandler = (id) => {
    const updatedTodos = todos.map((todo,index) =>
      index === id ? { ...todo, isDone: false } : todo
    );
    setTodos(updatedTodos);
  };

  const todoDeleteHandler=(id)=>{
    setTodos(todos.filter((todo,index)=>index!=id));
  }
  return (
    <>
      <TodoHeader />
      <TodoForm setTodos={setTodos} todos={todos}/>
      <TodoList todos={todos} todoDoneHandler={todoDoneHandler} todoUndoHandler={todoUndoHandler} todoDeleteHandler={todoDeleteHandler} />
    </>
  );
}

export default App;
