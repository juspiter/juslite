import { React, useRef, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import FilterTribunal from './FilterTribunal';
import FilterField from './FilterField';

// const [searchTerm, setSearchTerm] = useState("");

const SearchBox = () => {

  const [courtFilterOption, setCourtFilterOption] = useState('todos')

  const [fieldFilterOption, setFieldFilterOption] = useState('todos')

  const filterOptionHandler = selectedCourtFilter => {
    setCourtFilterOption(selectedCourtFilter)
  }

  const filterFilterOptionHandler = selectedFieldFilter => {
    setFieldFilterOption(selectedFieldFilter)
  }

  const navigate = useNavigate();

  const searchTermRef = useRef();

  const handleSearchSubmit = event => {
    event.preventDefault();
    const searchTermInput = searchTermRef.current.value;
    // console.log(searchTermInput);
    if (searchTermInput.length > 2) {
      navigate("/busca/" + searchTermInput + "/" + courtFilterOption + "/" + fieldFilterOption);
    }
  }
  return (
    <>
      <form className="input-group mb-3 search-box" onSubmit={handleSearchSubmit}>
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
      <div className="filters_container">
        <FilterTribunal
                selected={courtFilterOption}
                onChangeFilter={filterOptionHandler}
              />
        <FilterField
                selected={fieldFilterOption}
                onChangeFilter={filterFilterOptionHandler}
              />
      </div>
    </>
  );
}

export default SearchBox;
