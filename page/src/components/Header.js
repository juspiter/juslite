import { React, useState } from 'react';
import SearchBox from './SearchBox.js';

const Header = () => {
  return (
    <header id="header_">
      <img src="/image/juspiter.png" className="img-thumbnail" alt="Imagem vetorial do planeta jupiter com uma lupa na parte inferior" />
      <h1>Juslite</h1>
      <SearchBox />
      <hr/>
    </header>
  );
}

export default Header;
