import React from 'react';
//import {GrDocument} from 'react-icons/cg'

const ShowDoc = (props) => {
  if (props.doc != null && props.doc == "doc_sigilo") {
    return (
      <a href={props.url}>Sigilo</a>
    );
  }
	return ( 
		<div>
			{(props.doc != null) && <a href={props.doc}>LINK </a>}
		</div>
	 );
}
 
export default ShowDoc;