from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, tokenizer
from suitparser import SuitParser
import re


COURT_LIST = ['todos', 'tjal', 'tjce', 'tst']
FILTER_DICT = {
    "todos": ['numero', 'situacao', 'info_header.info*.conteudo', 'partes_todas*.nomes'],
    "parte": ['partes_todas*.nomes'],
    "adv": ['partes_todas*.outros'],
    "classe": ['info_header.info0.conteudo'],
    "assunto": ['info_header.info1.conteudo'],
    "foro": ['info_header.info2.conteudo'],
    "vara": ['info_header.info3.conteudo'],
    "juiz": ['info_header.info4.conteudo'],
}


class SearchEngine:
    def __init__(self, addr) -> None:
        self.es = Elasticsearch([addr])
        if not self.es.ping():
            raise ValueError("ElasticSearch connection failed")

    def get_results(self, string: str, sort: str, court: str, field: str, page: int) -> dict:
        lawsuit = SuitParser(string)
        if re.match('^[0-9.-]+$', string):
            return self.get_by_number(lawsuit)

        if court not in COURT_LIST or field not in FILTER_DICT.keys():
            return{"response": [], "status_code": 5, "status": "Nenhum resultado encontrado"}
        if court == "todos":
            court = "*"

        s = Search(using=self.es, doc_type="lawsuit", index=court).query('query_string', analyzer="brazilian",
            query=string, fields=FILTER_DICT.get(field))
        if sort == 'recente':
            s = s.sort('-ultima_mov.data')
        index = (int(page) - 1) * 10
        res = s[index : index + 10].execute()
        if res.hits == []:
            return{"response": [], "status_code": 5, "status": "Nenhum resultado encontrado"}
        return {"response": [hit.to_dict() for hit in res.hits], "status_code": 0, "status": "OK", "count": res.hits.total.value}

    def get_by_number(self, lawsuit) -> dict:
        if not lawsuit.is_valid:
            return{"response": [], "status_code": 1, "status": "Número inválido"}

        if not lawsuit.court_is_valid():
            return {"response": [], "status_code": 2, "status": "Tribunal não suportado"}

        if not lawsuit.year_is_valid():
            return{"response": [], "status_code": 3, "status": "Ano inválido"}

        s = Search(using=self.es, doc_type='lawsuit') \
            .query('ids', values=[lawsuit.formatted_number])
        res = s.execute()

        if res.hits == []:
            return{"response": [], "status_code": 4, "status": "Processo desconhecido"}

        return {"response": [hit.to_dict() for hit in res.hits], "status_code": 0, "status": "OK"}
