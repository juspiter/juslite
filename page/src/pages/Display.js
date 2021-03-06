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

    const res = await fetch(process.env.REACT_APP_HOST_ADDR + "/api/lawsuit/" + number);

    if (res.ok) {
      const data = await res.json();
      setRequestResponse(data);
    }
    setIsSearching(false);
  }
  useEffect(() => {
    fetchLawsuitsHandler();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [number]);

	if (!isSearching && requestResponse.response.length > 0){
  return (
    <div className="container">
      <Header />
      <LawsuitDisplay proc={requestResponse.response[0]}/>
    </div>
  )
	}
	else { return(<div className="container"><Header /><h5>Buscando...</h5></div>) }
}

export default Display;
