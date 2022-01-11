import { useParams } from 'react-router-dom';
import { React, useState, useEffect } from 'react';
import Header from '../components/Header';
import LawsuitDisplay from '../components/LawsuitDisplay';

const Display = () => {
  const [requestResponse, setRequestResponse] = useState({ "response": [] });
  const [isSearching, setIsSearching] = useState(true);
  const { number } = useParams();

  async function fetchLawsuitsHandler() {
    setIsSearching(true);

    const res = await fetch("https://juslite.42sp.org.br/api/lawsuit/" + number + "?sort=");

    if (res.ok) {
      const data = await res.json();
      setRequestResponse(data);
      console.log(requestResponse.response);
    }
    setIsSearching(false);
  }
  useEffect(() => {
    fetchLawsuitsHandler();
  }, [number]);

	if (!isSearching && requestResponse.response.length > 0){
  return (
    <>
      <Header />
      <LawsuitDisplay proc={requestResponse.response[0]}/>
    </>
  )
	}
	else { return(<div><Header /><h5>Buscando...</h5></div>) }
}

export default Display;
