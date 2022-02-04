import React from 'react';
import {IoDocumentOutline} from 'react-icons/io5'
import {RiLock2Line} from 'react-icons/ri'
import "../partials/ShowDoc.scss"

const ShowDoc = (props) => {
  if (props.doc == null) {
    return (null)
  }
  if (props.doc === "doc_sigilo") {
    return (
      <a title="Documento Sigiloso" target="_blank" rel="noreferrer" className="see-doc" href={props.url}>
        <RiLock2Line />
      </a>
    );
  }
  else {
    return (
      <a target="_blank" rel="noreferrer" className="see-doc" href={props.doc}>
        <IoDocumentOutline/>
      </a>
     );
  }
}

export default ShowDoc;
