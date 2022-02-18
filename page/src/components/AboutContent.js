const AboutContent = () => {
  return (
    <div id="carousel_about" className="carousel slide" data-bs-ride="carousel">
      <div className="carousel-indicators">
        <button type="button" data-bs-target="#carousel_about" data-bs-slide-to="0" className="active" aria-current="true" aria-label="Sobre"></button>
        <button type="button" data-bs-target="#carousel_about" data-bs-slide-to="1" aria-label="Instruções"></button>
        <button type="button" data-bs-target="#carousel_about" data-bs-slide-to="2" aria-label="Autoria"></button>
      </div>
      <div className="carousel-inner">
        <div className="carousel-item active">
          <div className="_contents">
            <h5 className="text-center">Sobre</h5>
            <p>O Juslite é um site gratuito e de <a href="https://github.com/juspiter/juslite">código aberto</a> para consulta processual, que agrega informações públicas de tribunais brasileiros. É um projeto fruto de colaboração entre a <a href="https://www.42sp.org.br/">42 São Paulo</a> e o <a href="https://www.jusbrasil.com.br/">Jusbrasil</a>.</p>
          </div>
        </div>
        <div className="carousel-item">
          <div className="_contents">
            <h5 className="text-center">Instruções</h5>
            <p>Digite a sua pesquisa na caixa de busca, sendo que qualquer termo digitado será buscado entre nomes de tribunais, números de processos, partes envolvidas, magistrados, assunto, classNamee, foro e vara.</p>
            <p>Tribunais suportados: TJAL e TJCE (1º grau), TST.</p>
          </div>
        </div>
        <div className="carousel-item">
          <div className="_contents">
            <div className="container">
              <div className="row">
                  <h5 className="text-center">Autoria</h5>
                <div className="col">
                  <h6 className="text-center">Desenvolvedores:</h6>
                  <ul>
                    <li><a target="_blank" rel="noreferrer" href="https://github.com/aalcara">Anderson</a></li>
                    <li><a target="_blank" rel="noreferrer" href="https://github.com/LuccasRMedeiros">Luccas</a></li>
                    <li><a target="_blank" rel="noreferrer" href="https://github.com/natflausino">Natasha</a></li>
                    <li><a target="_blank" rel="noreferrer" href="https://github.com/rkrocha">Rafael</a></li>
                  </ul>
                </div>
                <div className="col">
                  <h6 className="text-center m-2">Agradecimentos:</h6>
                  <ul>
                    <li><a target="_blank" rel="noreferrer"href="https://github.com/vdemario">Vitor</a></li>
                    <li><a target="_blank" rel="noreferrer"href="https://twitter.com/lulacode?s=20">Lula</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <button className="carousel-control-prev" type="button" data-bs-target="#carousel_about" data-bs-slide="prev">
        <span className="carousel-control-prev-icon" aria-hidden="true"></span>
        <span className="visually-hidden">Previous</span>
      </button>
      <button className="carousel-control-next" type="button" data-bs-target="#carousel_about" data-bs-slide="next">
        <span className="carousel-control-next-icon" aria-hidden="true"></span>
        <span className="visually-hidden">Next</span>
      </button>
    </div>
  );
}

export default AboutContent;
