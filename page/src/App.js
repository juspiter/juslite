//import logo from './logo.svg';
import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import { useState } from "react";
import display from "./pages/display";
// import GetLocalJSON from './components/GetLocalJSON';
// import './App.css';

//class SearchBox extends Component
//{
//  prop_process_id;
//}

// class SearchBox extends Component
// {
//   constructor(props)
//   {
//     super(props);
//     this.state = {number_process: ''}
//     //const[number, print_number] = useState('')
//   }
//   function print_number(params) {
//     return(
//       <div>number_process</div>
//       <button type="submit" onClick={print_number}>Buscar</button>
//     );
//   }
//   render()
//   {
//     return (
//       <div>
//         <input placeholder="Digite o numero do processo"/>
//       </div>
//     );
//   }
// }
// <div>
// <input
//    type="text"
//    placeholder="Search here"
//    onChange={handleChange}
//    value={searchInput} />

function App()
{
  const [name, setName] = useState("");

  const handleSubmit = (event) => {
    // event.preventDefault();
    // alert(`The name you entered was: ${name}`)
      <Route path="/display">
          <display />
        </Route>
  }
  {
    return (
      <div className="App">
        <header>
          <h1>Juslite</h1>
        </header>
        <form onSubmit={handleSubmit}>
            <input
              type="text"
              placeholder="Search here"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          <input type="submit" />
        </form>
      </div>
    );
  }
}

export default App;
