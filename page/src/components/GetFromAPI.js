import React, { Component } from 'react';
import { useState, useEffect } from 'react';
// import process from './lawsuit.json';
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
          <br></br>
          <h2><b>{proc['number']}</b></h2>
          <br></br>
          {proc['changes'].map(change => (
            <div>
              <li key={change}><i>{change['date']}</i> {change['title']}
              <br></br>{change['content']}</li>
              <br></br>
            </div>
          ))}
        </div>
        );
    }

  console.log("sem processo")
  return (<div>Sem processo</div>)
}

export default GetFromAPI;
