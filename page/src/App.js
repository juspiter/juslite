//import logo from './logo.svg';
import React, { Component } from 'react';
import GetLocalJSON from './components/GetLocalJSON';
import './App.css';

class App extends Component
{
  render()
  {
    return (
      <div className="App">
      <header className="App-header">
        <h1>JusLite</h1>
        <h2>TJAL - 0710802-55.2018.8.02.0001</h2>
        <h3>MOVIMENTAÇÕES</h3>
        <GetLocalJSON/>
      </header>
      </div>
    );
  }
}

export default App;
