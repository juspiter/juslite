const AboutContent = () => {
  return (
    <div id="carousel_about" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carousel_about" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Sobre"></button>
        <button type="button" data-bs-target="#carousel_about" data-bs-slide-to="1" aria-label="Instruções"></button>
        <button type="button" data-bs-target="#carousel_about" data-bs-slide-to="2" aria-label="Autoria"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <div class="_contents">
            <h5 class="text-center">Sobre</h5>
            <p>O Juslite é um site gratuito e open-source que agrega informações públicas de tribunais brasileiros. É um projeto fruto de colaboração entre a <a href="https://www.42sp.org.br/">42 São Paulo</a> e o <a href="https://www.jusbrasil.com.br/">Jusbrasil</a>.</p>
          </div>
        </div>
        <div class="carousel-item">
          <div class="_contents">
            <h5 class="text-center">Instruções</h5>
            <p>Digite a sua pesquisa na caixa de busca, sendo que qualquer termo digitado será buscado entre nomes de tribunais, números de processos, partes envolvidas, magistrados, assunto, classe, foro e vara.</p>
            <p>Tribunais suportados: TJAL, TJCE, TST.</p>
          </div>
        </div>
        <div class="carousel-item">
          <div class="_contents">
            <div class="container">
              <div class="row">
                  <h5 class="text-center">Autoria</h5>
                <div class="col">
                  <h6 class="text-center">Desenvolvedores:</h6>
                  <ul>
                    <li><a target="_blank" rel="noreferrer" href="https://github.com/aalcara">Anderson</a></li>
                    <li><a target="_blank" rel="noreferrer" href="https://github.com/LuccasRMedeiros">Luccas</a></li>
                    <li><a target="_blank" rel="noreferrer" href="https://github.com/natflausino">Natasha</a></li>
                    <li><a target="_blank" href="https://github.com/rkrocha">Rafael</a></li>
                  </ul>
                </div>
                <div class="col">
                  <h6 class="text-center m-2">Agradecimentos:</h6>
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
      <button class="carousel-control-prev" type="button" data-bs-target="#carousel_about" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carousel_about" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  );
}

export default AboutContent;

{/* <div className="container">
      <div className="row align-items-start">
        <div className="col-3 m-4 card">
          <h5>Sobre</h5>
          <p>O Juslite é um site gratuito e open-source que agrega informações públicas de tribunais brasileiros. É um projeto fruto de colaboração entre a <a href="https://www.42sp.org.br/">42 São Paulo</a> e o <a href="https://www.jusbrasil.com.br/">Jusbrasil</a>.</p>
        </div>
        <div className="col-3 m-4 card">
          <h5>Instruções</h5>
          <p>Digite a sua pesquisa na caixa de busca, sendo que qualquer termo digitado será buscado entre nomes de tribunais, números de processos, partes envolvidas, magistrados, assunto, classe, foro e vara.</p>
          <p>Tribunais suportados: TJAL, TJCE, TST.</p>
        </div>
        <div className="col-3 m-4 card">
          <h5>Autoria</h5>
          <h6>Desenvolvedores:</h6>
          <ul>
            <li><a href="https://github.com/aalcara">Anderson</a></li>
            <li><a href="https://github.com/LuccasRMedeiros">Luccas</a></li>
            <li><a href="https://github.com/natflausino">Natasha</a></li>
            <li><a href="https://github.com/rkrocha">Rafael</a></li>
          </ul>
          <h6>Apoio e agradecimentos:</h6>
            <ul>
              <li>Vitor</li>
              <li>Lula</li>
            </ul>
        </div>
      </div>
    </div> */}
