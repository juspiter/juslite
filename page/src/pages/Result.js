import { React, useState } from 'react';
import fetchRequest from "../components/fetch-request";
import { useParams } from 'react-router-dom';

const Result = () => {
  const [searchData, setSearchData] = useState();
  const term = useParams();
  setSearchData(fetchRequest(term, ""));
  console.log(searchData.response);
  return (
    <>
      { searchData.response }
    </>
  );
}

export default Result;


// function Pagina() {
//   const { id } = useParams()

//   return (
//     <div>
//       <h1>Pagina {id} </h1>
//     </div>
//   )
// }

// export default Pagina
