import "./App.css";

function App() {
  const vegetables = ["potato", "sweet potato", "cucumber", "eggplant", "corn"];
  const users = [
    { id: 1, age: 30, name: "Brad Pitt" },
    { id: 2, age: 24, name: "Tom Holland" },
    { id: 3, age: 21, name: "Zendaya" },
    { id: 4, age: 29, name: "Shah Rukh Khan" },
  ];
  return (
    <div className="style">
      {
        // vegetables.map((vegetable,index)=>{
        //   return <div className="squareStyle" key={index}>{vegetable}</div>
        // })
        users.map((user)=>{
          return <div className="squareStyle" key={user.id}>{user.name}</div>
        })
      }     
    </div>
  );
}

export default App;
