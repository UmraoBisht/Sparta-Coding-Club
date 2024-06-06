import React from "react";
import styled from "styled-components";
function Header() {
  return (
    <Navbar>
      <Logo>Logo.</Logo>
      <nav>
        <NavLinks>
          <NavLink>Home</NavLink>
          <NavLink>About</NavLink>
          <NavLink>Contact</NavLink>
        </NavLinks>
      </nav>
    </Navbar>
  );
}

const Logo = styled.h1`
  color: blueviolet;
  font-weight: bold;
  cursor: pointer;
`;

const Navbar = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.6rem 1rem;
  background-color: aliceblue;
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.2);
  height: 3rem;
`;

const NavLinks = styled.ul`
  display: flex;
  align-items: center;
  gap: 0.8rem;
`;

const NavLink = styled.li`
  list-style: none;
  cursor: pointer;
  color: blue;
`;

export default Header;
