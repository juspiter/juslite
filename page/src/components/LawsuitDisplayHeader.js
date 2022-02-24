import React from 'react';

const LawsuitDisplayHeader = (props) => {
  return (
    <div className='display_header'>
      <section className="d-inline-flex p-3 bd-highlight align-items-center gap-3">
        <div>
          <div style={{"color" : "gray", "fontSize" : "16px"}}>Nº do processo</div>
            <div>
              <div className="header_number_process">
                <strong> {props.proc['numero']} ({props.proc['tribunal'].toUpperCase()})</strong>
                {props.proc['situacao'] && <span className="border-2">{props.proc['situacao']}</span>}
              </div>
              <div>
                {props.proc['numeros_alternativos'] &&
              <div>{props.proc['numeros_alternativos'].map(alter, index => (
                <div key={index}>{alter['titulo']}: {alter['numero']}</div>))}
              </div>}
            </div>
          </div>
        </div>
      </section>
      <br />
      <section className="container">
        <div className="row mb-3">
          <div className='col-4'>
            <h5 className="header_titulo ">{props.proc['info_header']['info0']['titulo']}</h5>
            <span>{props.proc['info_header']['info0']['conteudo']}</span>
          </div>
          <div className='col-4'>
            <h5 className="header_titulo">{props.proc['info_header']['info1']['titulo']}</h5>
            <span>{props.proc['info_header']['info1']['conteudo']}</span>
          </div>
          <div className='col-4'>
            <h5 className="header_titulo">{props.proc['info_header']['info4']['titulo']}</h5>
            <span>{props.proc['info_header']['info4']['conteudo']}</span>
          </div>
        </div>
        <div className='row'>
          <div className='col-4'>
            <h5 className="header_titulo">{props.proc['info_header']['info2']['titulo']}</h5>
            <span>{props.proc['info_header']['info2']['conteudo']}</span>
          </div>
          <div className='col-4'>
            <h5 className="header_titulo">{props.proc['info_header']['info3']['titulo']}</h5>
            <span className="">{props.proc['info_header']['info3']['conteudo']}</span>
          </div>
        </div>
        <p className='atualizado_display'>Atualizado em: {props.proc.data_atualizacao}</p>
      </section>
    </div>
  );
}

export default LawsuitDisplayHeader;
