import React, { useState } from "react";
import styled from "styled-components";
import { useDispatch } from "react-redux";

import { addTodo } from "../features/todoSlice";

function AddTodo() {
  const dispatch = useDispatch();
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const addTodoHandler = (e) => {
    e.preventDefault();
    dispatch(addTodo({ title, description }));
    setTitle("");
    setDescription("");
  };
  return (
    <>
      <H2>Add Todo</H2>
      <Form>
        <Title htmlFor="todoTitle">Title :</Title>
        <TitleInput
          type="text"
          id="todoTitle"
          placeholder="Add Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <Title htmlFor="todoInput">TODO :</Title>
        <TodoInput
          type="text"
          id="todoInput"
          placeholder="Add Todo"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
        <Button type="button" onClick={(e) => addTodoHandler(e)}>
          Add
        </Button>
      </Form>
    </>
  );
}

const H2 = styled.h2`
  padding-top: 2rem;
  font-weight: bold;
`;

const Form = styled.form`
  display: flex;
  gap: 2rem;
  align-items: center;
`;


const Title = styled.label`
  padding: 0.4;
  font-weight: semibold;
  font-size: 1.3rem;
  text-align: center;
`;
const TitleInput=styled.input`
  padding: 0.6rem;
  font-size: 1rem;
  border: 1px solid black;
  border-radius: 5px;
  margin-bottom: 1rem;
  width: 10%;
  outline: none;
  background-color: white;
  color: black;
  box-sizing: border-box;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  transition: all 0.2s ease-in-out;
`;

const TodoInput = styled.input`
  padding: 0.6rem;
  font-size: 1rem;
  border: 1px solid black;
  border-radius: 5px;
  margin-bottom: 1rem;
  width: 30%;
  outline: none;
  background-color: white;
  color: black;
  box-sizing: border-box;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  transition: all 0.2s ease-in-out;
`;

const Button = styled.button`
  padding: 0.6rem 1rem;
  font-size: 0.8rem;
  border: 1px solid black;
  border-radius: 5px;
  margin-bottom: 1rem;
  width: 10%;
  outline: none;
  background-color: white;
  color: black;
  box-sizing: border-box;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  transition: all 0.2s ease-in-out;
  cursor: pointer;
  &:hover {
    background-color: black;
    color: white;
  }
`;

export default AddTodo;
