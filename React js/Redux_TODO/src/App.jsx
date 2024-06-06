import AddTodo from "./components/AddTodo";
import Header from "./components/Header";
import Todo from "./components/Todo";

import styled from "styled-components";

function App() {
  return (
    <Wrapper>
      <Header />
      <AddTodo />
      <Todo />
    </Wrapper>
  );
}

const Wrapper = styled.div`
  padding: 0rem 2rem;
`;

export default App;
