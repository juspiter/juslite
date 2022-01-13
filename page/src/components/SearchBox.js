import { React, useRef } from 'react';
import { useNavigate } from 'react-router-dom';

// const [searchTerm, setSearchTerm] = useState("");

const SearchBox = () => {

  const navigate = useNavigate();

  const searchTermRef = useRef();

  const handleSearchSubmit = event => {
    event.preventDefault();
    const searchTermInput = searchTermRef.current.value;
    // console.log(searchTermInput);
    if (searchTermInput.length > 2) {
      navigate("/busca/" + searchTermInput);
    }
  }
  return (
    <>
      <form className="input-group" onSubmit={handleSearchSubmit}>
        <input
          className="input-text input-group-text"
          type="text"
          placeholder='Digite sua busca...'
          ref={searchTermRef}
          // value={searchTerm}
          // onChange={handleSearchChange}
        />
        <button className="input-group-text input-button" type='submit'>Buscar</button>
      </form>
    </>
  );
}

export default SearchBox;
