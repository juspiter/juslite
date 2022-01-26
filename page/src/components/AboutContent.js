const AboutContent = () => {
  return (
    <div className="container">
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
    </div>
  );
}

export default AboutContent;
