import React from 'react';


const LawsuitPreview = (props) => {
  return (
    <div onClick={() => props.onSelect(props.lawsuit)} className="container-list pt-4">
      <h5>{props.lawsuit.court.toUpperCase()} {props.lawsuit.number} <small>{props.lawsuit.status}<small/></small></h5>
      <ul class="row align-items-start">
        <div class="col-6">
          <div>Classe: {props.lawsuit.class}</div>
          <div>Assunto: {props.lawsuit.subject}</div>
          <div>Juíz/Juíza: {props.lawsuit.judge}</div>
          <div>Movimentação mais relevante: {props.lawsuit.mov_relevante.data} - {props.lawsuit.mov_relevante.titulo}</div>
        </div>
        <div class="col-6"><b>Partes principais:</b>
          {props.lawsuit.parties.map(party => (
                  <div>{party['names'][0]}</div>
              ))}
        </div>
      </ul>
    </div>
    );
}

export default LawsuitPreview;
