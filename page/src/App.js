
import { useState } from 'react';

import Welcome from './components/Welcome';
import SearchingProgressBar from './components/SearchingProgressBar';
import NotProcess from './components/NotProcess';
import LawsuitList from './components/LawsuitList';
import LawsuitDisplay from './components/LawsuitDisplay';

import './App.scss';

const App = () =>
{
  const [isWelcome, setIsWelcome] = useState(true);
  const [isSearching, setIsSearching] = useState(false);
  const [searchTerm, setSearchTerm] = useState("");
  const [requestResponse, setRequestResponse] = useState([]);

  async function fetchLawsuitsHandler() {
    setIsSearching(true);

    const res = await fetch("http://localhost:3001/lawsuit/" + searchTerm);

    if (res.ok) {
      const data = await res.json();
      setRequestResponse(data.response)
    }

    setIsSearching(false);
    // console.log(data.response);
  }

  const handleSearchChange = event => {
    setSearchTerm(event.target.value);
  }

  const handleSearchSubmit = event => {
    event.preventDefault();
    setIsWelcome(false);

    if (searchTerm.length > 2) {
      fetchLawsuitsHandler();
    }
  }

  return (
    <main className="container">
      <header id="header_">
        <img src={require('./jupiter_planet.png')} className="img-thumbnail" alt="Imagem vetorial do planeta jupiter com uma lupa na parte inferior"/>
        <h1>Juslite</h1>
        <form className="input-group mb-3" onSubmit={handleSearchSubmit}>
          <input
            className="input-text input-group-text"
            type="text"
            placeholder='Digite sua busca...'
            value={searchTerm}
            onChange={handleSearchChange}
            />
          <button className="input-group-text input-button" type='submit'>Buscar</button>
        </form>
        <hr/>
      </header>
      {isWelcome && <Welcome />}
      {isSearching && <SearchingProgressBar />}
      {requestResponse.length === 0 && !isWelcome && !isSearching && <NotProcess />}
      {requestResponse.length === 1 && !isSearching && <LawsuitDisplay proc={requestResponse[0]}/>}
      {requestResponse.length > 1 && !isSearching && <LawsuitList list={requestResponse} />}
    </main>
  );
}

export default App;
