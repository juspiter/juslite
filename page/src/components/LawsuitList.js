import React, { useEffect, useState } from 'react';
import LawsuitPreview from './LawsuitPreview';
import LawsuitDisplay from './LawsuitDisplay';

const LawsuitList = (props) => {

    return (
      <div>
        {props.list.map(lawsuit => (
        <LawsuitPreview
          lawsuit={lawsuit}
        />))}
      </div>
    );
}

export default LawsuitList;
