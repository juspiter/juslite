import React from 'react';

const LawsuitDisplayParties = (props) => {
  return (
    <section>
      <h3><b>Partes do Processo:</b></h3>
      {props.proc['partes_todas'].map((party, index) => (
        <div key={index}>
          <li className="row align-items-start">
            <div className="col-2"><i>{party['titulo']}</i></div>
            <div className="col-10">
              {party['nomes'].map((nome, index) => (<div key={index}>{nome}</div>))}
              {party['outros'].map((outros, index) => (<div key={index}>{outros}</div>))}
            </div>
          </li>
          <hr />
        </div>
      ))}
    </section>
  );
}

export default LawsuitDisplayParties;
