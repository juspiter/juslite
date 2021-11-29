from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from suitparser import SuitParser
import re


class SearchEngine:
    def __init__(self, addr) -> None:
        self.es = Elasticsearch([addr])
        if not self.es.ping():
            raise ValueError("ElasticSearch connection failed")

    def get_results(self, string: str) -> dict:
        lawsuit = SuitParser(string)
        if re.match('^[0-9.-]+$', string):
            return self.get_by_number(lawsuit)
        else:
            return self.get_by_term(string)

    def get_by_term(self, term: str) -> dict:
        s = Search(using=self.es, doc_type="lawsuit").query('multi_match',
            query=term,
            fields=['court', 'status', 'class', 'subject', 'judge', 'parties.names'])
        res = s.execute()
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
        return {"response": [hit.to_dict() for hit in res.hits], "status_code": 0, "status": "OK"}
