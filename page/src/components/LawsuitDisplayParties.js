import React from 'react';

const LawsuitDisplayParties = (props) => {
  return (
    <section>
      <h3><b>Partes do Processo:</b></h3>
      {props.proc['parties'].map(party => (
        <div>
          <li className="row align-items-start" key={party}>
            <div className="col-2"><i>{party['label']}</i></div>
            <div className="col-10">{party['names'].map(names => (
              <div>{names}</div>
            ))}</div>
          </li>
          <hr />
        </div>
      ))}
    </section>
  );
}

export default LawsuitDisplayParties;
