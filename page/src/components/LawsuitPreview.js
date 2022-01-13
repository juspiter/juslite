import React from 'react';
import { useNavigate } from 'react-router-dom';

const LawsuitPreview = (props) => {
  const navigate = useNavigate();
  return (
    <div onClick={() => navigate("/exibir/" + (props.lawsuit.number))} className="container-list pt-4">
      <h5>{props.lawsuit.court.toUpperCase()} {props.lawsuit.number} <small>{props.lawsuit.status}<small/></small></h5>
      <ul className="row align-items-start">
        <div className="col-6">
          <div>Classe: {props.lawsuit.class}</div>
          <div>Assunto: {props.lawsuit.subject}</div>
          <div>Juíz/Juíza: {props.lawsuit.judge}</div>
          <div>Movimentação mais relevante: {props.lawsuit.mov_relevante.data} - {props.lawsuit.mov_relevante.titulo}</div>
        </div>
        <div className="col-6"><b>Partes principais:</b>
          {props.lawsuit.parties.map(party => (
                  <div>{party['names'][0]}</div>
              ))}
        </div>
      </ul>
    </div>
    );
}

export default LawsuitPreview;
