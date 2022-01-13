import React from 'react';

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
      {props.proc['changes'].map(change => (
        <div>
          <li className="row align-items-start" key={change}>
            <div className="col-2"><b>{change['date']}</b></div>
            <div className="col-10">{change['title']}<br />{change['content']}</div>
          </li>
          <hr />
        </div>
      ))}
    </section>
  );
}

export default LawsuitDisplayChanges;
