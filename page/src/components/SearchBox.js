import { React, useRef } from 'react';
import { useNavigate } from 'react-router-dom';

// const [searchTerm, setSearchTerm] = useState("");

const SearchBox = () => {

  const navigate = useNavigate();

  const searchTermRef = useRef();

  const handleSearchSubmit = event => {
    event.preventDefault();
    const searchTermInput = searchTermRef.current.value;
    console.log(searchTermInput);
    navigate("/busca/" + searchTermInput);
  }
  return (
    <>
      <form className="input-group mb-3 justify-content-center" onSubmit={handleSearchSubmit}>
        <input
          className="input-text input-group-text w-25"
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
