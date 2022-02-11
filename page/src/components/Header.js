import { React } from 'react'
import SearchBox from './SearchBox.js'
import { Link } from 'react-router-dom'


const Header = () => {
  return (
    <header id="header_">
      <div className="container">
        <div className="row">
          <div className="col-1">
            <Link to="/">
              <img
                className=""
                src="/image/logo.svg"
                alt="Imagem vetorial do planeta jupiter com uma lupa na parte inferior"
              />
            </Link>
          </div>
          <div className="col-11 mt-4" id="searchbox">
            <SearchBox />
          </div>
        </div>
      </div>
      <hr />
    </header>
  )
}

export default Header
