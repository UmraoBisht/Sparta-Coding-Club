import React from "react";

function TodoList({ todos, todoDoneHandler,todoUndoHandler,todoDeleteHandler }) {
  const incompleteTodos = todos.filter((todo) => !todo.isDone);
  const doneTodos = todos.filter((todo) => todo.isDone);

  return (
    <div className="list-container">
      <h2 className="list-title">Working.. 🔥</h2>
      <div className="list-wrapper">
        {incompleteTodos.map((todo, index) => {
          todo.isDone === false;
          return (
            <div className="todo-container" key={index}>
              <div>
                <h2 className="todo-title">{todo.title}</h2>
                <div>{todo.content}</div>
              </div>
              <div className="button-set">
                <button className="todo-delete-button btn" onClick={()=>todoDeleteHandler(index)}>Delete</button>
                <button
                  className="todo-complete-button btn"
                  onClick={() => todoDoneHandler(index)}
                >
                  Done
                </button>
              </div>
            </div>
          );
        })}
      </div>
      <h2 className="list-title">Done..! 🎉</h2>
      <div className="list-wrapper">
        {doneTodos.map((todo, index) => {
          return (
            <div className="todo-container" key={index}>
              <div>
                <h2 className="todo-title">{todo.title}</h2>
                <div>{todo.content}</div>
              </div>
              <div className="button-set">
                <button className="todo-delete-button btn" onClick={()=>todoDeleteHandler(index)}>Delete</button>
              <button className="todo-complete-button btn" onClick={()=>todoUndoHandler(index)}>Cancel</button>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default TodoList;
