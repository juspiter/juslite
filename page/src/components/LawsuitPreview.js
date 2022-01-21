import React from 'react';
import { useNavigate } from 'react-router-dom';

const LawsuitPreview = (props) => {
  const navigate = useNavigate();
  return (
    <div onClick={() => navigate("/exibir/" + (props.lawsuit.numero))} className="container-list pt-4">
      <h5><b>{props.lawsuit.partes_principais.parte1} X {props.lawsuit.partes_principais.parte2}</b></h5>
      <h6>{props.lawsuit.tribunal.toUpperCase()} {props.lawsuit.numero} <small>{props.lawsuit.situacao}<small/></small></h6>
      <ul className="row align-items-start">
        <div className="col-6">
          <div>{props.lawsuit.info_header.info0.titulo}: {props.lawsuit.info_header.info0.conteudo}</div>
          <div>{props.lawsuit.info_header.info1.titulo}: {props.lawsuit.info_header.info1.conteudo}</div>
          <div>{props.lawsuit.info_header.info4.titulo}: {props.lawsuit.info_header.info4.conteudo}</div>
          <div>Última movimentação: {props.lawsuit.ultima_mov.data} - {props.lawsuit.ultima_mov.titulo}</div>
        </div>
        <div className="col-6">
        </div>
      </ul>
    </div>
    );
}

export default LawsuitPreview;
