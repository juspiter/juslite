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
        <>
          <section class="d-inline-flex p-3 bd-highlight align-items-center gap-3">
            <h3>Nº do processo:<b> {proc['number']} (TJAL)</b></h3>
            <h5 class="m-1 info p-1 border border-2 rounded-pill">{proc['status']}</h5>
          </section>
          <br/>
          <section class="container">
            <div class="row">
              <h5 class="info col">Classe<span class="row m-0">{proc['class']}</span></h5>
              <h5 class="info col">Assunto<span class="row m-0">{proc['subject']}</span></h5>
              <h5 class="info col">Juiz/Juíza<span class="row m-0">{proc['judge']}</span></h5>
            </div>
          </section>
          <hr></hr>
          <br></br>
          <section>
            <h3><b>Partes do Processo:</b></h3>
            <ul>
              {proc['parties'].map(part =>
                <li>{part}</li>)}
            </ul>
          </section>
          <br></br>
          <section>
            <h3><b>Movimentações:</b></h3>
            <div>
                <li class="row align-items-start">
                  <div class="col-2"><i>Data</i></div>
                  <div class="col-10"><i>Movimentações</i></div>
                </li>
                <hr/>
              </div>
            {proc['changes'].map(change => (
              <div>
                <li class="row align-items-start" key={change}>
                  <div class="col-2"><i>{change['date']}</i></div>
                  <div class="col-10">{change['title']}<br/>{change['content']}</div>
                </li>
                <hr/>
              </div>
              ))}
          </section>
        </>
        );
    }

  console.log("sem processo")
  return (<section><br></br>Sem processo</section>)
}

export default GetFromAPI;
