async function fetchRequest(searchTerm, sortOption) {
  // setIsSearching(true);
  const res = await fetch("https://juslite.42sp.org.br/api/lawsuit/" + searchTerm + "?sort=" + sortOption);
  if (res.ok) {
    const data = await res.json();
    console.log(data.response);
    return (data);
  }
  // setIsSearching(false);
}

export default fetchRequest;
