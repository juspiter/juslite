import re
from storage import Storage
from basecrawler import BaseCrawler
from parsecrawler import parse_crawl


# storage = Storage('172.17.0.3:27017')

crawl = BaseCrawler("https://www2.tjal.jus.br/cpopg/search.do?conversationId=&cbPesquisa=NUMPROC&dadosConsulta.valorConsultaNuUnificado=0710802-55.2018.8.02.0001&dadosConsulta.valorConsultaNuUnificado=UNIFICADO&dadosConsulta.valorConsulta=&dadosConsulta.tipoNuProcesso=UNIFICADO&uuidCaptcha=")


print(parse_crawl(crawl.soup))