import React, { useEffect, useState } from 'react'

function showmenu() {
  let visibility = document.getElementById('filter-menu').style.visibility

  if (visibility === 'hidden') {
    visibility = 'visible'
  } else {
    visibility = 'hidden'
  }

  document.getElementById('filter-menu').style.visibility = visibility
}

const FilterMenu = () => {
  return (
    <>
      <input type="button" onClick={showmenu} value="Filtros" />
      <div id="filter-menu">
        <label>Filtro por tribunal</label>
        <select>
          <option value="tjal">Tribunal de Justiça de Alagoas</option>
          <option value="tjce">Tribunal de Justiça do Ceará</option>
        </select>
      </div>
    </>
  )
}

export default FilterMenu
