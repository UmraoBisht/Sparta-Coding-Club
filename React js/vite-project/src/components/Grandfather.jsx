import React from "react";
import Mother from "./Mother";
import "./grandfather.css";
function Grandfather({grandFatherName}) {
  return (
    <div className="parent">
      Grandfather,I'm {grandFatherName} 
      <br></br>
      <Mother></Mother>
    </div>
  );
}

export default Grandfather;
