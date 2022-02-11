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
          <option value="todos">em todos os campos</option>
          <option value="parte">por nome de partes</option>
          <option value="adv">por nome de advogado</option>
          <option value="juiz">por nome de magistrado</option>
          <option value="assunto">por assunto</option>
          <option value="classe">por classe</option>
          <option value="foro">por foro</option>
          <option value="vara">por vara</option>
        </select>
      </div>
    </>
  )
}

export default FilterField;