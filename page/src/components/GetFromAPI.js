import React, { useState, useEffect } from 'react';
import axios from "axios";


const GetFromAPI = (props) =>
{
  const [proc, setProcess] = useState("");

  useEffect(() => {
    setProcess("")
    if (props.term && props.term.length == 25 ) {
    var url = "http://localhost:3001/lawsuit/" + props.term
    console.log(url)
    axios.get(url)
      .then(res => setProcess(res.data));
    }
  }, [props])

    console.log(proc)
    if (proc)
    {
      console.log("achou processo")
      return(
        <div>
          <h3><b>Processo: {proc['number']} (TJAL)</b></h3>
          <h3><b>Movimentações:</b></h3>
          {proc['changes'].map(change => (
            <div>
              <li key={change}><i>{change['date']}:</i> {change['title']}
              <br></br>{change['content']}</li>
              <br></br>
            </div>
          ))}
        </div>
        );
    }

  console.log("sem processo")
  return (<div><br></br>Sem processo</div>)
}

export default GetFromAPI;
