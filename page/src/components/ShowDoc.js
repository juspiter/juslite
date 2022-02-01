import React from 'react';
//import {GrDocument} from 'react-icons/cg'

const ShowDoc = (props) => {
  if (props.doc == null) {
    return (null)
  }
  if (props.doc == "doc_sigilo") {
    return (
      <a href={props.url}>Sigilo</a>
    );
  }
  else {
    return ( 
      <a href={props.doc}>LINK </a>
     );
  }
}
 
export default ShowDoc;