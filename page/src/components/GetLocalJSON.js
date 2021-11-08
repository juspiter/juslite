import React, { Component } from 'react';
import process from './lawsuit.json';


const GetLocalJSON = (props) =>
{
  // console.log(props.term)
  if (props.term === "0710802-55.2018.8.02.0001")
  {

    return(
      <div>
        {process.map(proc => (
          <div>
            <div>{proc['number']}</div>
            <div>{proc['changes'][0]['date']}</div>
          </div>
        ))}

      </div>
    );
  }
  return (<div>Sem processo</div>)
}

/* class GetLocalJSON extends Component {
    constructor(props){
        super(props);
        this.state = {
            process :process
        };
    }

    render() {
        const {process} = this.state;
        return(
            <div>
                <ol className="item">
                {
                    process.map(proc => (
                        <div>
							<p className="title">{proc['changes'][i]['date']}   {proc['changes'][i]['title']}</p>
                            <p className="body">{proc['changes'][i]['content']}</p>
							<br></br>
                          </div>
                    ))
                }
                </ol>
            </div>
        );
    }
  }
*/
  export default GetLocalJSON;
