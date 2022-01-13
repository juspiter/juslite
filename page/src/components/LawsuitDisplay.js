import React, { useEffect } from 'react';
import LawsuitDisplayHeader from './LawsuitDisplayHeader';
import LawsuitDisplayParties from './LawsuitDisplayParties';
import LawsuitDisplayChanges from './LawsuitDisplayChanges';


const LawsuitDisplay = (props) =>
{
  useEffect(() => {
    window.scrollTo(0, 0)
  }, [])

      return(
        <>
          <LawsuitDisplayHeader proc={props.proc} />
          <hr></hr>
          <br></br>
          <LawsuitDisplayParties proc={props.proc} />
          <br></br>
          <LawsuitDisplayChanges proc={props.proc} />
        </>
        );
    }

export default LawsuitDisplay;
