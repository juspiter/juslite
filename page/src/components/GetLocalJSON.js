import React, { Component } from 'react';

import process from './lawsuit.json'; // RENAME VAR
class GetLocalJSON extends Component {
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
							<p className="title">{proc['changes'][0]['date']}   {proc['changes'][0]['title']}</p>
                            <p className="body">{proc['changes'][0]['content']}</p>
							<br></br>
                            <p className="title">{proc['changes'][1]['date']}   {proc['changes'][1]['title']}</p>
                            <p className="body">{proc['changes'][1]['content']}</p>
                          </div>
                    ))
                }
                </ol>
            </div>
        );
    }
  }

  export default GetLocalJSON;
