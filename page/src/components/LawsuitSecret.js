import React from 'react';

const LawsuitSecret = (props) => {
  return (
    <a style={{ "text-decoration": "none" }} target="_blank" rel="noreferrer" href={props.lawsuit.url}>
      <div className="container-list pt-4">
        <h5 style={{ "text-align": "center" }}>PROCESSO SIGILOSO</h5>
        <h5 className='mt-2' style={{ "text-align": "center" }}>{props.lawsuit.tribunal.toUpperCase()} {props.lawsuit.numero}</h5>
        <hr />
        <p style={{ "text-align": "center" }}>Caso tenha permissão para acessá-lo, clique aqui para ir ao site do tribunal.</p>
      </div>
    </a>
  );
}

export default LawsuitSecret;
