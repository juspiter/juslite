from storage import Storage
from basecrawler import BaseCrawler
import json

# https://www2.tjal.jus.br/cpopg/search.do?conversationId=&cbPesquisa=NUMPROC&dadosConsulta.valorConsultaNuUnificado=0710802-55.2018.8.02.0001&dadosConsulta.valorConsultaNuUnificado=UNIFICADO&dadosConsulta.valorConsulta=&dadosConsulta.tipoNuProcesso=UNIFICADO&uuidCaptcha=

# docker run --name jusdb -d mongo:4.4.10
storage = Storage('172.17.0.2:27017')

# crawl = BaseCrawler("0710802-55.2018.8.02.0001")

# print(json.dumps(crawl.parse_lawsuit(), ensure_ascii=False, skipkeys=True, indent=4))

# file = open('tjal_processos.csv', 'r')
# lines = file.readlines()

# for line in lines:
#     crawl = BaseCrawler(line[:-1])
#     storage.add_lawsuit(crawl.parse_lawsuit())

# print(storage.count_lawsuits())
print(storage.get_lawsuit("0000001-30.2007.8.02.0059"))
