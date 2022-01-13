import React from 'react';

const LawsuitDisplayHeader = (props) => {
  return (
    <>
      <section className="d-inline-flex p-3 bd-highlight align-items-center gap-3">
        <h3>Nº do processo:<b> {props.proc['number']} ({props.proc['court'].toUpperCase()})</b></h3>
        <h5 className="m-1 info p-1 border border-2 rounded-pill">{props.proc['status']}</h5>
      </section>
      <br />
      <section className="container">
        <div className="row">
          <h5 className="info col">Classe:<span className="row m-0">{props.proc['class']}</span></h5>
          <h5 className="info col">Assunto:<span className="row m-0">{props.proc['subject']}</span></h5>
          <h5 className="info col"></h5>
        </div>
        <div className="row mt-2">
          <h5 className="info col">Foro:<span className="row m-0">{props.proc['foro']}</span></h5>
          <h5 className="info col">Vara:<span className="row m-0">{props.proc['vara']}</span></h5>
          <h5 className="info col">Juiz/Juíza:<span className="row m-0">{props.proc['judge']}</span></h5>
        </div>
      </section>
    </>
  );
}

export default LawsuitDisplayHeader;
