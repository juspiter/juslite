import { React, useEffect, useState } from 'react';
// import LawsuitPreview from "../components/LawsuitPreview.js";
import LawsuitList from "../components/LawsuitList.js";
import LawsuitDisplay from '../components/LawsuitDisplay';
import fetchRequest from "../components/fetch-request";
import Header from '../components/Header.js';
import { useParams, useNavigate } from 'react-router-dom';
import SortOptions from '../components/SortOptions.js';


const Result = () => {
  const [requestResponse, setRequestResponse] = useState({ "response": [] });
  const [sortOption, setSortOption] = useState("relevante");
  const [isSearching, setIsSearching] = useState(true);
  const { term } = useParams();
  const navigate = useNavigate();

  const sortOptionHandler = selectedSort => {
    setSortOption(selectedSort);
  }

  async function fetchLawsuitsHandler() {
    setIsSearching(true);

    const res = await fetch("https://juslite.42sp.org.br/api/lawsuit/" + term + "?sort=" + sortOption);

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
      <div>
        <Header />
        <SortOptions selected={sortOption} onChangeSort={sortOptionHandler} />
        <LawsuitList list={requestResponse.response} />
      </div>
    )
  }
  else if (!isSearching && requestResponse.response.length === 1) {
    navigate("/exibir/" + requestResponse.response[0].number);//trocar por useNavigate
    return (
      <div>
        <Header />
      </div>
    )
  }
  else { return(<div><Header /><h5>Buscando...</h5></div>) }
}

export default Result;
