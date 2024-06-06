import { nanoid } from "@reduxjs/toolkit";
import React from "react";
import { useSelector } from "react-redux";
import styled from "styled-components";

function Todo() {
  const todos = useSelector((state) => state.todo.todos);
  return (
    <>
      <H2>Todos</H2>
      <TodoContainer>
        {todos.map((todo) => (
          <Card key={nanoid()} className="todoCard">
            <h3>{todo.title}</h3>
            <p>{todo.description}</p>
          </Card>
        ))}
      </TodoContainer>
    </>
  );
}

const H2 = styled.h2`
  padding-top: 2rem;
  font-weight: bold;
`;

const TodoContainer = styled.div`
  display: flex;
  align-items: center;
  gap: 0.6rem;
  flex-wrap: wrap;
`;

const Card = styled.div`
  background-color: aliceblue;
  padding: 1rem;
  margin-bottom: 0.8rem;
  border-radius: 0.5rem;
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.2);
  width: 15rem;
`;

export default Todo;
