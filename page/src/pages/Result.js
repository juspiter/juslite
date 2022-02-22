import { React, useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import LawsuitList from "../components/LawsuitList.js";
import LawsuitNotFound from "../components/LawsuitNotFound";
import SortOptions from '../components/SortOptions.js';
import Header from '../components/Header.js';
import ButtonTop from '../components/ButtonTop';
import ButtonPage from '../components/ButtonPage';


const Result = () => {
  const [requestResponse, setRequestResponse] = useState({ "response": [] });
  const {term, sort, court, field, page} = useParams();
  const [sortOption, setSortOption] = useState(sort);
  const [isSearching, setIsSearching] = useState(true);
  const navigate = useNavigate();

  const sortOptionHandler = selectedSort => {
    navigate("/busca/" + term + "/" + selectedSort + "/" + court + "/" + field + "/1");
    setSortOption(selectedSort);
  }

  async function fetchLawsuitsHandler() {
    setIsSearching(true);

    const res = await fetch("https://juslite.42sp.org.br/api/query/" + term + "?sort=" + sortOption + "&court=" + court + "&field=" + field + "&page=" + page);
    // const res = await fetch("http://localhost:80/api/query/" + term + "?sort=" + sortOption + "&court=" + court + "&field=" + field + "&page=" + page);

    if (res.ok) {
      const data = await res.json();
      setRequestResponse(data);
      //console.log(requestResponse.response);
    }
    setIsSearching(false);
  }

  useEffect(() => {
    fetchLawsuitsHandler();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [sortOption, term, court, field, page]);

  if (!isSearching && requestResponse.response.length >= 1) {
    return (
      <div className="container">
        <Header />
        <h5>{requestResponse.count} resultados</h5>
        <SortOptions selected={sortOption} onChangeSort={sortOptionHandler} />
        <LawsuitList list={requestResponse.response}/>
        <ButtonTop/>
        <ButtonPage sort={sortOption} term={term} court={court} field={field} page={page} count={requestResponse.count}/>
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
