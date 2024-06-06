import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import {
  increment,
  decrement,
  reset,
  incrementByAmmount,
} from "./counterSlice";

function Counter() {
  const count = useSelector((state) => state.counter.count);
  const dispatch = useDispatch();
  const [incrementAmount, setIncrementAmount] = useState(0);
  const addValue = Number(incrementAmount) || 0;

  const resetAll = () => {
    dispatch(reset());
    setIncrementAmount(0);
  };
  return (
    <div>
      <h1>Counter</h1>
      <div>
        <h3>{count}</h3>
        <button onClick={() => dispatch(increment())}>+</button>
        <button onClick={() => dispatch(decrement())}>-</button>
      </div>
      <div>
        <input
          type="number"
          value={incrementAmount}
          onChange={(e) => dispatch(setIncrementAmount(e.target.value))}
        />
        <button onClick={() => dispatch(incrementByAmmount(addValue))}>Add</button>
        <button onClick={() => resetAll()}>Reset</button>
      </div>
    </div>
  );
}

export default Counter;
