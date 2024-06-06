import { createSlice } from "@reduxjs/toolkit";

const initialState={
    count:0
}

export const counterSlice=createSlice({
    name:"counter",
    initialState,
    reducers:{
        // these are actions
        increment:(state)=>{
            state.count++;
        },
        decrement:(state)=>{
            state.count--;
        },
        incrementByAmmount:(state,action)=>{
            state.count+=action.payload;
        },
        reset:(state)=>{
            state.count=0;
        },
    }
});

export const {increment,decrement,reset,incrementByAmmount}=counterSlice.actions;
export default counterSlice.reducer;