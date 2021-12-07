import React, { useEffect } from 'react';


const LawsuitDisplay = (props) =>
{
  useEffect(() => {
    window.scrollTo(0, 0)
  }, [])

      return(
        <>
          <section className="d-inline-flex p-3 bd-highlight align-items-center gap-3">
            <h3>Nº do processo:<b> {props.proc['number']} ({props.proc['court'].toUpperCase()})</b></h3>
            <h5 className="m-1 info p-1 border border-2 rounded-pill">{props.proc['status']}</h5>
          </section>
          <br/>
          <section className="container">
            <div className="row">
              <h5 className="info col">Classe:<span className="row m-0">{props.proc['class']}</span></h5>
              <h5 className="info col">Assunto:<span className="row m-0">{props.proc['subject']}</span></h5>
              <h5 className="info col"></h5>
            </div>
            <div className="row mt-2">
              <h5 className="info col">Foro:<span className="row m-0">{props.proc['foro']}</span></h5>
              <h5 className="info col">Vara:<span className="row m-0">{props.proc['vara']}</span></h5>
              <h5 className="info col">Juiz/Juíza:<span className="row m-0">{props.proc['judge']}</span></h5>
            </div>
          </section>
          <hr></hr>
          <br></br>
          <section>
            <h3><b>Partes do Processo:</b></h3>
            {props.proc['parties'].map(party => (
              <div>
                <li className="row align-items-start" key={party}>
                  <div className="col-2"><i>{party['label']}</i></div>
                  <div className="col-10">{party['names'].map(names => (
                    <div>{names}</div>
                  ))}</div>
                </li>
                <hr/>
              </div>
            ))}
          </section>
          <br></br>
          <section>
            <h3><b>Movimentações:</b></h3>
            <div>
                <li className="row align-items-start">
                  <div className="col-2"><i>Data</i></div>
                  <div className="col-10"><i>Movimentações</i></div>
                </li>
                <hr/>
              </div>
            {props.proc['changes'].map(change => (
              <div>
                <li className="row align-items-start" key={change}>
                  <div className="col-2"><b>{change['date']}</b></div>
                  <div className="col-10">{change['title']}<br/>{change['content']}</div>
                </li>
                <hr/>
              </div>
              ))}
          </section>
        </>
        );
    }

export default LawsuitDisplay;
