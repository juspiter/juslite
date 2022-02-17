import { React, useRef, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import FilterTribunal from './FilterTribunal';
import FilterField from './FilterField';


const SearchBox = () => {

  let {term, sort, court, field} = useParams()
  const [searchTerm, setSearchTerm] = useState(term);

  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value)
  }

  if (court === undefined) {
    court = "todos"
  }

  if (field === undefined) {
    field = "todos"
  }

  if (sort === undefined) {
    sort = "relevante"
  }

  const [courtFilterOption, setCourtFilterOption] = useState(court)
  const [fieldFilterOption, setFieldFilterOption] = useState(field)

  const filterOptionHandler = selectedCourtFilter => {
    setCourtFilterOption(selectedCourtFilter)
  }

  const filterFilterOptionHandler = selectedFieldFilter => {
    setFieldFilterOption(selectedFieldFilter)
  }

  const navigate = useNavigate();

  const handleSearchSubmit = event => {
    event.preventDefault();

    if (searchTerm.replace(/[\s\?\*\#\/\%\\]/g, '').length < 2) {
      setSearchTerm("");
      return ;
    }

    if (searchTerm.length > 1 ) {
      navigate("/busca/" + searchTerm + "/" + sort + "/" + courtFilterOption + "/" + fieldFilterOption + "/" + "1");
    }
  }
  return (
    <>
      <form className="input-group search-box" onSubmit={handleSearchSubmit}>
        <input
          className="input-text input-group-text"
          type="text"
          placeholder='Busque por um processo...'
          value={searchTerm}
          onChange={handleSearchChange}
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
