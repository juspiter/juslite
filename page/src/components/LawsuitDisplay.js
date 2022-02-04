import React, { useEffect } from 'react';
import LawsuitDisplayHeader from './LawsuitDisplayHeader';
import LawsuitDisplayParties from './LawsuitDisplayParties';
import LawsuitDisplayChanges from './LawsuitDisplayChanges';
import LawsuitSecret from './LawsuitSecret';
import ButtonTop from './ButtonTop';


const LawsuitDisplay = (props) => {
  useEffect(() => {
    window.scrollTo(0, 0)
  }, [])

  if (props.proc.sigilo === true) { return (<LawsuitSecret lawsuit={props.proc} />); }
  else {
    return (
      <>
        <LawsuitDisplayHeader proc={props.proc} />
        <br></br>
        <LawsuitDisplayParties proc={props.proc} />
        <br></br>
        <LawsuitDisplayChanges proc={props.proc} />
        <ButtonTop/>
      </>
    );
  }
}

export default LawsuitDisplay;
