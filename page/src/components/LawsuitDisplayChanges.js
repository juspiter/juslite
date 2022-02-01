import React from 'react';
import ShowDoc from './ShowDoc';


const LawsuitDisplayChanges = (props) => {
  return (
    <section>
      <h3><b>Movimentações:</b></h3>
      <div>
        <li className="row align-items-start">
          <div className="col-2"><i>Data</i></div>
          <div className="col-10"><i>Movimentações</i></div>
        </li>
        <hr />
      </div>
      {props.proc['moves'].map(change => (
        <div>
          <li className="row align-items-start" key={change}>
            <div className="col-2"><b>{change['data']}</b></div>
            <div className="col-10">
              <ShowDoc doc={change['doc']} url={props.proc['url']} />
              {change['titulo']}<br />{change['conteudo']}
            </div>
          </li>
          <hr />
        </div>
      ))}
    </section>
  );
}

export default LawsuitDisplayChanges;
