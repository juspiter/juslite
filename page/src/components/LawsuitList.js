import React from 'react';
import LawsuitPreview from './LawsuitPreview';

const LawsuitList = (props) => {

    return (
      <div>
        {props.list.map(lawsuit => (
        <LawsuitPreview
          key={lawsuit.numero}
          lawsuit={lawsuit}
        />))}
      </div>
    );
}

export default LawsuitList;
