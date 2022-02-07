<br/>
<p align="center">
  <a href="https://juslite.42sp.org.br/">
    <img src="https://github.com/juspiter/juslite/raw/main/page/public/image/logo.svg" alt="Logo Juspiter" width="150" height="150">
  </a>
  <a href="https://juslite.42sp.org.br/">
    <h3 align="center">Juslite</h3>
  </a>
</p>


## Sobre o projeto

O Juslite é um site gratuito e de código aberto para consulta processual, que agrega informações públicas de tribunais brasileiros. É um projeto fruto de colaboração entre a [42 São Paulo](https://www.42sp.org.br/) e o [Jusbrasil](https://www.jusbrasil.com.br/home).

Cada tribunal pode oferecer diferentes sistemas e maneiras de se pesquisar e acessar informações públicas sobre processos jurídicos. O objetivo do Juslite é agregar estas informações em um único site que seja fácil de utilizar e que tenha um layout constante independente da origem de um processo.

No momento são suportados os seguintes tribunais:
- TJAL (Tribunal de Justiça do Alagoas, 1º grau)
- TJCE (Tribunal de Justiça do Ceará, 1º grau)
- TST (Tribunal Superior do Trabalho)

## Stack

### Backend
* [Python](https://www.python.org/)
* [Scrapy](https://scrapy.org/), framework de [web crawling](https://pt.wikipedia.org/wiki/Rastreador_web)
* [Elasticsearch](https://www.elastic.co/pt/), motor de busca
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) API
* [Docker](https://www.docker.com/)
* [nginx](https://nginx.org/en/)

### Frontend
* [React](https://reactjs.org/), biblioteca de JavaScript
* [Bootstrap](https://getbootstrap.com/), toolkit de CSS
* [Sass](https://sass-lang.com/), extensão de CSS

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_





-----------------------------------

# "A" JUSLITE

A Juslite é um <a href="https://juslite.42sp.org.br">site gratuito</a> <a href="https://github.com/juspiter/juslite"> código aberto</a> para consulta processual, que agrega informações públicas de tribunais brasileiros. É um projeto fruto de colaboração entre a <a href="https://www.42sp.org.br/">42 São Paulo</a> e a <a href="https://www.jusbrasil.com.br/">Jusbrasil</a>

Qual o problema que ele resolve?
  Facilita o acesso e busca de informações dos processos de tribunais brasileiros.
  
A solução implementada: 
  - Crawling dos tribunais e amazenar as informação no banco de dados, permitindo buscas mais eficientes.
  - Layout simples e um site facil de utilizar.

Tecnologias utilizadas:
  - Python;
  - ElasticSearch;
  - ReactJS;
  - Docker;
  - Nginx;
  - Flask;
  - Scrapy;

Desafios enfrentados:
  - Aprender as novas ferramentas, nunca utilizadas pelos integrantes do grupo;
  - Acessar os tribunais e crawlear as informações;
  - Diferentes layouts e HTMLs dos tribunais;
  - Entender as necessidades dos usuarios da Juslite;
  - Formular o design ideal para as páginas;

Perspectivas para o futuro do produto:
  - Mais informações e tribunais no banco de dados;
  - Coleção de referencias;
