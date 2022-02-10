import React from 'react';

const FilterField = (props) => {
	const filterChangeHandler = event => {
    props.onChangeFilter(event.target.value)
  }
  return (
    <>
      <div className="field_filter mb-3">
        <select
          className="custom-select"
          value={props.selected}
          onChange={filterChangeHandler}
        >
          <option value="todos">Todos os campos</option>
          <option value="parte">Nome de Partes</option>
          <option value="adv">Nome de Advogado</option>
          <option value="juiz">Nome de Magistrado</option>
          <option value="foro">Foro</option>
          <option value="vara">Vara</option>
          <option value="classe">Classe</option>
          <option value="assunto">Assunto</option>
        </select>
      </div>
    </>
  )
}

export default FilterField;