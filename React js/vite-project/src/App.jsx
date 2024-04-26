import React, { useState } from "react";
import Grandfather from "./components/Grandfather";

function Immutability() {
  const arr = ["Hello"];
  const [name, setName] = useState(arr);
  const [value, setValue] = useState("");

  const changeHandler = () => {
    arr.push(value);
    console.log(arr);
    setName([...name, value]);
    console.log(name);
  };
  const valueHandler = (e) => {
    setValue(e.target.value);
  };

  return (
    <div>
      <h1>Immutability</h1>
      <input type="text" value={value} onChange={(e) => valueHandler(e)} />
      <button onClick={() => changeHandler()}>Change</button>
      <h1>{name}</h1>
    </div>
  );
}

function App() {
  // const grandFatherName="Alex";
  const [counter, setCounter] = useState(0);
  function decrement() {
    setCounter(counter - 1);
  }
  function increment() {
    setCounter(counter + 1);
  }
  return (
    <div className="d-flex justify-content-center align-items-center flex-column">
      <h1>Counter App</h1>
      <h3 className="text-lg">{counter}</h3>
      <div className="d-flex gap-2">
        <button className="btn btn-primary" onClick={increment} style={{width:"80px"}}>
          +
        </button>
        <button className="btn btn-primary" onClick={decrement} style={{width:"80px"}}>
          -
        </button>
      </div>
    </div>
  );
}

export default App;
