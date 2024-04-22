import React from "react";
import Mother from "./Mother";
import "./grandfather.css";
function Grandfather() {
  return (
    <div className="parent">
      Grandfather,Im in Grandfather
      <br></br>
      <Mother></Mother>
    </div>
  );
}

export default Grandfather;
