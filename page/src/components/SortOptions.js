import React from 'react';

const SortOptions = (props) => {
  const sortChangeHandler = (event) => {
    props.onChangeSort(event.target.value);
  }
  return (
      <>
        <div>
          {/* <label>Ordenar por: </label> */}
          <select className="input-dropdown input-group input-group-text" value={props.selected} onChange={sortChangeHandler}>
            <option value='relevante'>Mais relevante</option>
            <option value='recente'>Mais recente</option>
          </select>
        </div>
      </>
    );
}

export default SortOptions;
