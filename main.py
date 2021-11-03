from storage import Storage
from basecrawler import BaseCrawler
import json


# docker run --name jusdb -d mongo:4.4.10
storage = Storage('172.17.0.2:27017')

crawl = BaseCrawler("https://www2.tjal.jus.br/cpopg/search.do?conversationId=&cbPesquisa=NUMPROC&dadosConsulta.valorConsultaNuUnificado=0710802-55.2018.8.02.0001&dadosConsulta.valorConsultaNuUnificado=UNIFICADO&dadosConsulta.valorConsulta=&dadosConsulta.tipoNuProcesso=UNIFICADO&uuidCaptcha=")

# storage.add_lawsuit(crawl.parse_lawsuit())
# print(storage.get_lawsuit())
print(json.dumps(crawl.parse_lawsuit(), ensure_ascii=False, skipkeys=True, indent=4))

# if crawl.soup is not None:
# 	print(storage.count_lawsuits())
# else:
# 	print("Error")
