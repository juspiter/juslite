import { React, useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import LawsuitList from "../components/LawsuitList.js";
import LawsuitNotFound from "../components/LawsuitNotFound";
import SortOptions from '../components/SortOptions.js';
import Header from '../components/Header.js';
import ButtonTop from '../components/ButtonTop';


const Result = () => {
  const [requestResponse, setRequestResponse] = useState({ "response": [] });
  const [sortOption, setSortOption] = useState("relevante");
  const [isSearching, setIsSearching] = useState(true);
  const { term, court } = useParams();
  const navigate = useNavigate();

  const sortOptionHandler = selectedSort => {
    setSortOption(selectedSort);
  }

  async function fetchLawsuitsHandler() {
    setIsSearching(true);

    // const res = await fetch("https://juslite.42sp.org.br/api/lawsuit/" + term + "?sort=" + sortOption + "?court=" + court);
    const res = await fetch("https://juslite_api:3001/lawsuit/" + term + "?sort=" + sortOption + "?court=" + court);

    if (res.ok) {
      const data = await res.json();
      setRequestResponse(data);
      console.log(requestResponse.response);
    }
    setIsSearching(false);
  }

  useEffect(() => {
    fetchLawsuitsHandler();
  }, [term, sortOption]);

  if (!isSearching && requestResponse.response.length > 1) {
    return (
      <div className="container">
        <Header />
        <SortOptions selected={sortOption} onChangeSort={sortOptionHandler} />
        <LawsuitList list={requestResponse.response} />
        <ButtonTop/>
      </div>
    )
  }
  else if (!isSearching && requestResponse.response.length === 1) {
    navigate("/exibir/" + requestResponse.response[0].numero);//trocar por useNavigate
    return (
      <div className="container">
        <Header />
      </div>
    )
  }
  else if (!isSearching && requestResponse.response.length === 0) {
    return (
      <div className="container">
        <Header />
        <LawsuitNotFound proc={requestResponse} term={term}/>
      </div>
    )
  }
  else { return(<div className="container"><Header /><h5>Buscando...</h5></div>) }
}

export default Result;
