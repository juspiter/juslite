import React from 'react';

const LawsuitDisplayHeader = (props) => {
  return (
    <>
      <section className="d-inline-flex p-3 bd-highlight align-items-center gap-3">
        <h3>Nº do processo:<b> {props.proc['numero']} ({props.proc['tribunal'].toUpperCase()})</b></h3>
        <h5 className="m-1 info p-1 border border-2 rounded-pill">{props.proc['situacao']}</h5>
      </section>
      <br />
      <section className="container">
        <div className="row">
          <h5 className="info col">{props.proc['info_header']['info0']['titulo']}<span className="row m-0">{props.proc['info_header']['info0']['conteudo']}</span></h5>
          <h5 className="info col">{props.proc['info_header']['info1']['titulo']}<span className="row m-0">{props.proc['info_header']['info1']['conteudo']}</span></h5>
          <h5 className="info col"></h5>
        </div>
        <div className="row mt-2">
          <h5 className="info col">{props.proc['info_header']['info2']['titulo']}<span className="row m-0">{props.proc['info_header']['info2']['conteudo']}</span></h5>
          <h5 className="info col">{props.proc['info_header']['info3']['titulo']}<span className="row m-0">{props.proc['info_header']['info3']['conteudo']}</span></h5>
          <h5 className="info col">{props.proc['info_header']['info4']['titulo']}<span className="row m-0">{props.proc['info_header']['info4']['conteudo']}</span></h5>
        </div>
      </section>
    </>
  );
}

export default LawsuitDisplayHeader;
