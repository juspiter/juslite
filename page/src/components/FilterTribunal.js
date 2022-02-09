import React from 'react';

const FilterTribunal = (props) => {
	const filterChangeHandler = event => {
    props.onChangeFilter(event.target.value)
  }
  return (
    <>
      <div className="tribunal_filter input-group mb-3">
        <div className="input-group-prepend">
          <label className="input-group-text" for="inputGroupSelect01">
            Tribunal{' '}
          </label>
        </div>
        <select
          className="custom-select"
          id="inputGroupSelect01"
          value={props.selected}
          onChange={filterChangeHandler}
        >
          <option value="todos">Todos</option>
          <option value="tjal">Tribunal de Justiça de Alagoas</option>
          <option value="tjce">Tribunal de Justiça do Ceará</option>
          <option value="tst">Tribunal Superior do Trabalho</option>
        </select>
      </div>
    </>
  )
}


export default FilterTribunal;