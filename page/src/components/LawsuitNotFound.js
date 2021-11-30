import React from 'react';

const LawsuitNotFound = (props) => {
  var link = "https://www.jusbrasil.com.br/busca?q=" + props.term;
  return (
    <>
    <p>{props.proc.status}.</p>
    {[2, 4, 5].indexOf(props.proc.status_code) !== -1 && <p>Mas talvez você encontre algo no <a href={link} target="_blank">Jusbrasil</a>.</p>}
    </>
   );
}

export default LawsuitNotFound;
