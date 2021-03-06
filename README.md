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

Cada tribunal pode oferecer diferentes sistemas e maneiras de se pesquisar e acessar informações sobre processos jurídicos. O objetivo do Juslite é agregar estas informações em um único site que seja fácil de utilizar e que tenha um layout constante independente da origem de um processo.

No momento são suportados os seguintes tribunais:
- TJAL (Tribunal de Justiça do Alagoas, 1º grau)
- TJCE (Tribunal de Justiça do Ceará, 1º grau)
- TST (Tribunal Superior do Trabalho)

## Stack

### Backend
* [Python](https://www.python.org/)
* [Scrapy](https://scrapy.org/), framework de [web crawling](https://pt.wikipedia.org/wiki/Rastreador_web)
* [Elasticsearch](https://www.elastic.co/pt/), motor de busca
* [FastAPI](https://fastapi.tiangolo.com/), API
* [Docker](https://www.docker.com/)
* [nginx](https://nginx.org/en/)

### Frontend
* [React](https://reactjs.org/), biblioteca de JavaScript
* [Bootstrap](https://getbootstrap.com/), toolkit de CSS
* [Sass](https://sass-lang.com/), extensão de CSS

## Componentes

### [Crawlers](https://github.com/juspiter/juslite/tree/main/crawlers)
Acessam os sites de tribunais, baixando os HTMLs de páginas de processos jurídicos, coletando sua informação relevante e encaminhando-a para o Elasticsearch. Este componente é composto por dois diferentes projetos do Scrapy: um deles capaz de coletar informações do [e-SAJ](https://www.softplan.com.br/solucoes/saj-tribunais/) (Sistema de Automação da Justiça) usado pelos tribunais TJAL e TJCE; enquanto o segundo projeto foi feito para coletar informações do [sistema próprio do TST](http://aplicacao4.tst.jus.br/consultaProcessual/consultaTstNumUnica.do).

### [API e motor de busca](https://github.com/juspiter/juslite/tree/main/api)
Composto pelo banco de dados e motor de busca do Elasticsearch, onde são guardados os dados coletados pelos crawlers; e pela API que recebe requisições feitas pelo site e retorna respostas buscadas pelo módulo do Elasticsearch e nele contidas.

### [Site](https://github.com/juspiter/juslite/tree/main/page)
Cada página, script e componente do React que compõe o site, assim como seus estilos CSS.

### [Proxy reverso](https://github.com/juspiter/juslite/tree/main/proxy)
Um componente simples para rotear acessos à página e API.

## Setup

É fácil rodar sua própria instância do Juslite visto que o projeto está 100% containerizado, e sendo assim suas únicas dependências são o Docker e docker-compose.

1. Clone ou baixe o repositório do Juslite.
2. Modifique o endereço do host/servidor no arquivo [.env](https://github.com/juspiter/juslite/blob/main/page/.env).
3. Dentro da pasta do Juslite, execute o comando abaixo:
```sh
docker-compose up -d
```
Feito isso, serão baixadas todas as imagens necessárias e subidos todos os containers. No momento o projeto conta com uma amostra de aproximadamente 10 mil processos, sendo que pode levar várias horas até que sejam coletados dos tribunais os dados de todos esses processos.


## Autoria

O Juslite foi desenvolvido por:
* [Anderson](https://github.com/aalcara)
* [Luccas](https://github.com/LuccasRMedeiros)
* [Natasha](https://github.com/natflausino)
* [Rafael](https://github.com/rkrocha)

Com o apoio de:
* [Vitor](https://github.com/vdemario)
* [Lula](https://twitter.com/lulacode?s=20)
