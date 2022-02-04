import React from 'react';
import {IoIosArrowDropup} from 'react-icons/io'
import "../partials/ButtonTop.scss"

const ButtonTop = () => {
	return (
  <IoIosArrowDropup onClick={() => window.scrollTo(0, 0)} className="to_top" title="Voltar ao Topo">
  </IoIosArrowDropup>);
}

export default ButtonTop;