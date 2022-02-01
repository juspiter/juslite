import React from 'react';
import { useNavigate } from 'react-router-dom';
import LawsuitSecret from './LawsuitSecret';


const LawsuitPreview = (props) => {
  const navigate = useNavigate();
  if (props.lawsuit.sigilo === true) { return (<LawsuitSecret lawsuit={props.lawsuit} />); }
  else {
    return (
      <div onClick={() => navigate("/exibir/" + (props.lawsuit.numero))} className="container-list pt-4">
        <div className="row justify-content-center align-items-center">
          <div className="col-5">
            <h5 style={{ "text-align": "right" }}><strong>{props.lawsuit.partes_principais.parte1}</strong></h5>
          </div>
          <div className="col-1">
            <h3 style={{ "text-align": "center", "color": "rgb(179, 177, 177)" }}><strong> X </strong></h3>
          </div>
          <div className="col-5">
            <h5 style={{ "text-align": "left" }}><strong>{props.lawsuit.partes_principais.parte2}</strong></h5>
          </div>
        </div>
        <h5 className='mt-2' style={{ "text-align": "center" }}>{props.lawsuit.tribunal.toUpperCase()} {props.lawsuit.numero} - <small>{props.lawsuit.situacao}</small></h5>
        <hr />
        <ul className="row align-items-start mt-3">
          <div className="col-4">
            <div className='preview_titulo'>Última movimentação</div>
            <div className='preview_cont'> {props.lawsuit.ultima_mov.data} - {props.lawsuit.ultima_mov.titulo}</div>
            <div className='preview_titulo mt-3'>{props.lawsuit.info_header.info4.titulo}</div>
            <div className='preview_cont'> {props.lawsuit.info_header.info4.conteudo}</div>
          </div>
          <div className="col-4">
            <div className='preview_titulo'>{props.lawsuit.info_header.info1.titulo}</div>
            <div className='preview_cont'> {props.lawsuit.info_header.info1.conteudo}</div>
            <div className='preview_titulo mt-3'>{props.lawsuit.info_header.info2.titulo}</div><div> {props.lawsuit.info_header.info2.conteudo}</div>
          </div>
          <div className="col-4">
            <div className='preview_titulo'>{props.lawsuit.info_header.info0.titulo}</div>
            <div className='preview_cont'> {props.lawsuit.info_header.info0.conteudo}</div>
            <div className='preview_titulo mt-3'>{props.lawsuit.info_header.info3.titulo}</div>
            <div className='preview_cont'> {props.lawsuit.info_header.info3.conteudo}</div>
          </div>
        </ul>
        <p className='atualizado_preview'>Atualizado em: {props.lawsuit.data_atualizacao}</p>
      </div>
    );
  }
}

export default LawsuitPreview;
