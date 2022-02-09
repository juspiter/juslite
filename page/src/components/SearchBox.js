import { React, useRef, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import FilterTribunal from './FilterTribunal';

// const [searchTerm, setSearchTerm] = useState("");

const SearchBox = () => {

  const [courtFilterOption, setCourtFilterOption] = useState('todos')

  const filterOptionHandler = selectedCourtFilter => {
    setCourtFilterOption(selectedCourtFilter)
  }

  const navigate = useNavigate();

  const searchTermRef = useRef();

  const handleSearchSubmit = event => {
    event.preventDefault();
    const searchTermInput = searchTermRef.current.value;
    // console.log(searchTermInput);
    if (searchTermInput.length > 2) {
      navigate("/busca/" + searchTermInput + "/" + courtFilterOption);
    }
  }
  return (
    <>
      <form className="input-group" onSubmit={handleSearchSubmit}>
        <input
          className="input-text input-group-text"
          type="text"
          placeholder='Busque por um processo...'
          ref={searchTermRef}
          // value={searchTerm}
          // onChange={handleSearchChange}
        />
        <button className="input-group-text input-button" type='submit'>Buscar</button>
      </form>
      <div>
      <FilterTribunal
              selected={courtFilterOption}
              onChangeFilter={filterOptionHandler}
            />
      </div>
    </>
  );
}

export default SearchBox;
