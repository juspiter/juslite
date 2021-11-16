import GetFromAPI from './components/GetFromAPI';
import juspiter_logo from './logo192.png';
import { useState } from 'react';
import './App.css';

const App = () =>
{
  const [searchTerm, setSearchTerm] = useState("");
  const [contentDisplay, setContentDisplay] = useState("");

  const handleChange = event =>
  {
    setSearchTerm(event.target.value);
  }

  const handleSubmit = event =>
  {
    event.preventDefault();
    console.log("test");
    setContentDisplay(<GetFromAPI term={searchTerm}/>);
  }

  return (
    <main class="container">
      <header id="header_">
        <img src={juspiter_logo} class="img-thumbnail" alt="Imagem vetorial do planeta jupiter com uma lupa na parte inferior"/>
        <h1>Juslite</h1>
        <form class="input-group mb-3" onSubmit={handleSubmit}>
          <input
            class="input-group-text"
            type="text"
            placeholder='Digite sua busca...'
            value={searchTerm}
            onChange={handleChange}
            />
          <button class="input-group-text" type='submit'>Buscar</button>
        </form>
        <hr/>
      </header>
      {contentDisplay}
    </main>
  );
}

export default App