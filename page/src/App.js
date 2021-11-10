import GetFromAPI from './components/GetFromAPI';
import { useState } from 'react';

const App = () =>
{
  const [searchTerm, setSearchTerm] = useState("");
  const [display, setDisplay] = useState("");

  const handleChange = event =>
  {
    setSearchTerm(event.target.value);
  }

  const handleSubmit = event =>
  {
    event.preventDefault();
    console.log("test");
    setDisplay(<GetFromAPI term={searchTerm}/>);
  }

  return (
    <>
    <header>
      <h1>Juslite</h1>
    </header>
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder='Digite sua busca...'
        value={searchTerm}
        onChange={handleChange}
        />
      <button type='submit'>Buscar</button>
    </form>
    {display}
    </>
  );
}

export default App