import React from 'react';

const SortOptions = (props) => {
  const sortChangeHandler = (event) => {
    props.onChangeSort(event.target.value);
  }
  return (
      <>
        <div>
          <label>Ordenar por: </label>
          <select value={props.selected} onChange={sortChangeHandler}>
            <option value='relevante'>Relevante</option>
            <option value='recente'>Recente</option>
          </select>
        </div>
      </>
    );
}

export default SortOptions;
