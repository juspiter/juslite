from storage import Storage
from basecrawler import BaseCrawler
import json

# https://www2.tjal.jus.br/cpopg/search.do?conversationId=&cbPesquisa=NUMPROC&dadosConsulta.valorConsultaNuUnificado=0710802-55.2018.8.02.0001&dadosConsulta.valorConsultaNuUnificado=UNIFICADO&dadosConsulta.valorConsulta=&dadosConsulta.tipoNuProcesso=UNIFICADO&uuidCaptcha=

# docker run --name jusdb -d mongo:4.4.10
storage = Storage('172.17.0.2:27017')

# crawl = BaseCrawler("0000001-24.2009.8.02.0006")
# print(crawl.parse_lawsuit())

# print(json.dumps(crawl.parse_lawsuit(), ensure_ascii=False, skipkeys=True, indent=4))

file = open('tjal_processos.csv', 'r')
lines = file.readlines()

for line in lines:
    crawl = BaseCrawler(line[:-1])
    storage.add_lawsuit(crawl.parse_lawsuit())
    print("crawled process: " + line[:-1])

# print(storage.delete_lawsuit("9999999-xx.2018.8.02.0001"))
# print(storage.get_lawsuit("9999999-xx.2018.8.02.0001"))

# print(storage.count_lawsuits())
# print(storage.get_lawsuit("0710802-55.2018.8.02.0001"))
# json.dumps(storage.get_lawsuit("0710802-55.2018.8.02.0001"), ensure_ascii=False, skipkeys=True, indent=4)
