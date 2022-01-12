import { React, useState } from 'react';
import SearchBox from './SearchBox.js';

const Header = () => {
  return (
    <header id="header_">
      <div className="container">
        <div className="row">
          <div className="col-1">
            <img className="" src="/image/juspiter.png" alt="Imagem vetorial do planeta jupiter com uma lupa na parte inferior" />
          </div>
          <div className="col-11" id="searchbox">
            <SearchBox />
          </div>
        </div>
      </div>
      <hr />
    </header>
  );
}

export default Header;
