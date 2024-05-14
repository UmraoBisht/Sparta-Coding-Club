import React, { useState } from "react";
import "../App.css";

function TodoForm({todos,setTodos}) {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
 
  
  const submitHandler=(e)=>{
    e.preventDefault();
    setTodos([...todos,{title,content,isDone:false}]);
  }
  return (
    <div className="flex form-container">
      <form action="" className="flex form" onSubmit={(e)=>submitHandler(e)}>
        <div className="flex">
          <div className="flex">
            <label className="form-label" htmlFor="title">
              Title
            </label>
            <input type="text" id="title" onChange={(e)=>setTitle(e.target.value)}/>
          </div>
          <div className="flex">
            <label className="form-label" htmlFor="content">
              Content
            </label>
            <input type="text" id="content" onChange={(e)=>setContent(e.target.value)}/>
          </div>
        </div>
        <div>
          <button type="submit" className="btn submit-btn">Add</button>
        </div>
      </form>
    </div>
  );
}

export default TodoForm;
