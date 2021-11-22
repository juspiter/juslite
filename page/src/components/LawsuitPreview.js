import React from 'react';


const LawsuitPreview = (props) => {
  return (
    <div onClick={() => props.onSelect(props.lawsuit)} className="container-list pt-4">
      <h5>{props.lawsuit.court.toUpperCase()} {props.lawsuit.number} <small>{props.lawsuit.status}<small/></small></h5>
      <p>Classe: {props.lawsuit.class}</p>
      <p>Assunto: {props.lawsuit.subject}</p>
      <p>Juíz/Juíza: {props.lawsuit.judge}</p>
    </div>
    );
}

export default LawsuitPreview;
