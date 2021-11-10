import GetFromAPI from './components/GetFromAPI';
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
    <>
    <header>
      <h1>Juslite</h1>
    </header>
    <form onSubmit={handleSubmit}>
      <input
        class="search-container"
        type="text"
        placeholder='Digite sua busca...'
        value={searchTerm}
        onChange={handleChange}
        />
      <button type='submit'>Buscar</button>
    </form>
    {contentDisplay}
    </>
  );
}

export default App