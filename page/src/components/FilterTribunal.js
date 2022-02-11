import React from 'react';

const FilterTribunal = (props) => {
	const filterChangeHandler = event => {
    props.onChangeFilter(event.target.value)
  }
  return (
    <>
      <div className="tribunal_filter mb-3">
        <select
          className="custom-select"
          value={props.selected}
          onChange={filterChangeHandler}
        >
          <option value="todos">Em todos os tribunais</option>
          <option value="tjal">Tribunal de Justiça de Alagoas</option>
          <option value="tjce">Tribunal de Justiça do Ceará</option>
          <option value="tst">Tribunal Superior do Trabalho</option>
        </select>
      </div>
    </>
  )
}


export default FilterTribunal;