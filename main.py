from storage import Storage
from basecrawler import BaseCrawler
import json

# https://www2.tjal.jus.br/cpopg/search.do?conversationId=&cbPesquisa=NUMPROC&dadosConsulta.valorConsultaNuUnificado=0710802-55.2018.8.02.0001&dadosConsulta.valorConsultaNuUnificado=UNIFICADO&dadosConsulta.valorConsulta=&dadosConsulta.tipoNuProcesso=UNIFICADO&uuidCaptcha=

# export ES_JAVA_OPTS="-Xms512m -Xmx512m"
# docker run -d --name juslitedb -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" --memory="1g" elasticsearch:7.14.2
storage = Storage('172.17.0.2:9200')

# crawl = BaseCrawler("0000001-24.2009.8.02.0006")
# print(crawl.parse_lawsuit())

file = open('tjal_processos.csv', 'r')
lines = file.readlines()

for line in lines:
    crawl = BaseCrawler(line[:-1])
    storage.add_lawsuit(crawl.crawl_lawsuit())
    print("crawled process: " + line[:-1])

# print(storage.search_lawsuits("9999999-xx.2018.8.02.0001"))
