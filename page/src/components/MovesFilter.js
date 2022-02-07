import React from 'react';

const MovesFilter = (props) => {
  const filterChangeHandler = (event) => {
    props.onChangeFilter(event.target.value);
  }
  return (
    <>
      <div className="moves_filter input-group mb-3">
        <div className="input-group-prepend">
          <label className="input-group-text" for="inputGroupSelect01" >Exibir </label>
        </div>
        <select className="custom-select" id="inputGroupSelect01" value={props.selected} onChange={filterChangeHandler}>
          <option value='todas'>Todas</option>
          <option value='com_doc'>Com Documentos</option>
        </select>
      </div>
    </>
  );
}

export default MovesFilter;