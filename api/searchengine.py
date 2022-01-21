from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from suitparser import SuitParser
import re


COURT_LIST = ['tjal', 'tjce', 'tst']

class SearchEngine:
    def __init__(self, addr) -> None:
        self.es = Elasticsearch([addr])
        if not self.es.ping():
            raise ValueError("ElasticSearch connection failed")

    def get_results(self, string: str, sort_method: str) -> dict:
        lawsuit = SuitParser(string)
        if re.match('^[0-9.-]+$', string):
            return self.get_by_number(lawsuit)

        court_filter = []
        term_list = string.split()
        for term in term_list:
            if term in COURT_LIST:
                court_filter.append(term)
        for court in court_filter:
            term_list.remove(court)
        string = ' '.join(term_list)

        if court_filter:
            return self.get_term_by_court(string, court_filter, sort_method)
        return self.get_by_term(string, sort_method)

    def get_term_by_court(self, term: str, court: list, sort: str) -> dict:
        if not term:
            s = Search(using=self.es, doc_type="lawsuit", index=court)
        else:
            s = Search(using=self.es, doc_type="lawsuit", index=court).query('multi_match',
            query=term,
            fields=['numero', 'situacao', 'info_header.info*.conteudo', 'partes_todas*.nomes'])
        if sort == 'recente':
            s = s.sort('-ultima_mov.data')
        res = s.execute()
        if res.hits == []:
            return{"response": [], "status_code": 5, "status": "Nenhum resultado encontrado"}
        return {"response": [hit.to_dict() for hit in res.hits], "status_code": 0, "status": "OK"}

    def get_by_term(self, term: str, sort: str) -> dict:
        s = Search(using=self.es, doc_type="lawsuit").query('multi_match',
            query=term,
            fields=['tribunal', 'numero', 'situacao', 'info_header.info*.conteudo', 'partes_todas*.nomes'])
        if sort == 'recente':
            s = s.sort('-ultima_mov.data')
        res = s.execute()
        if res.hits == []:
            return{"response": [], "status_code": 5, "status": "Nenhum resultado encontrado"}
        return {"response": [hit.to_dict() for hit in res.hits], "status_code": 0, "status": "OK"}

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
