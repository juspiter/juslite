import GetLocalJSON from './components/GetLocalJSON';
import { useState } from 'react';

const App = () =>
{
  const [searchTerm, setSearchTerm] = useState("");
  const handleChange = event =>
  {
    setSearchTerm(event.target.value);
  }

  return (
    <>
    <header>
      <h1>Juslite</h1>
    </header>
    <input
      type="text"
      placeholder='Digite sua busca...'
      value={searchTerm}
      onChange={handleChange}
      />
    <button>Buscar</button>
    <GetLocalJSON term={searchTerm}/>
    </>
  );
}

export default App