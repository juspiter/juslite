import { React, useState } from 'react';
import ShowDoc from './ShowDoc';
import MovesFilter from './MovesFilter.js'


const LawsuitDisplayChanges = (props) => {
  const [movesFilterOption, setMovesFilterOption] = useState("todas")

  const filterOptionHandler = selectedMovesFilter => {
    setMovesFilterOption(selectedMovesFilter);
  }

  return (
    <section>
      <h3><b>Movimentações:</b></h3>
      <MovesFilter selected={movesFilterOption} onChangeFilter={filterOptionHandler} />
      <div>
        <li className="row align-items-start">
          <div className="col-2"><i>Data</i></div>
          <div className="col-10"><i>Movimentações</i></div>
        </li>
        <hr />
      </div>
      {movesFilterOption == "todas" && props.proc['moves'].map(change => (
        <div>
          <li className="row align-items-start" key={change}>
            <div className="col-2"><b>{change['data']}</b></div>
            <div className="col-10">
              <ShowDoc doc={change['doc']} url={props.proc['url']} />
              <strong>{change['titulo']}</strong><br />{change['conteudo']}
            </div>
          </li>
          <hr />
        </div>
      ))}
      {movesFilterOption === "com_doc" && props.proc['moves'].map(change => (
        change['doc'] !== null && change['doc'] &&
          <div>
            <li className="row align-items-start" key={change}>
              <div className="col-2"><b>{change['data']}</b></div>
              <div className="col-10">
                <ShowDoc doc={change['doc']} url={props.proc['url']} />
                <strong>{change['titulo']}</strong><br />{change['conteudo']}
              </div>
            </li>
            <hr />
          </div>
      ))}
      
    </section>
  );
}

export default LawsuitDisplayChanges;
