import React, { useEffect, useState } from 'react';
import LawsuitPreview from './LawsuitPreview';
import LawsuitDisplay from './LawsuitDisplay';

const LawsuitList = (props) => {
  const [selectedLawsuit, setSelectedLawsuit] = useState(false);

  useEffect(() => {
    setSelectedLawsuit(false);
  }, [props.requestResponse]);

  const SelectLawsuitHandler = (selectedLawsuitContent) => {
    console.log(selectedLawsuitContent);
    setSelectedLawsuit(selectedLawsuitContent);
  }

  if (!selectedLawsuit) {
    return (
      <div>
        {props.list.map(lawsuit => (
        <LawsuitPreview
          onSelect={SelectLawsuitHandler}
          lawsuit={lawsuit}
        />))}
      </div>
    );
  }
  else {
    return (<LawsuitDisplay proc={selectedLawsuit} />)
  }
}

export default LawsuitList;
