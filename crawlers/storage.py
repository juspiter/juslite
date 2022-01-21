from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


class Storage:
    def __init__(self, addr: str):
        self.es = Elasticsearch([addr])
        if not self.es.ping():
            raise ValueError("ElasticSearch connection failed")

    def add_lawsuit(self, lawsuit: dict):
        if lawsuit == {}:
            return
        self.es.index(index=lawsuit["tribunal"], id=lawsuit["numero"], body=lawsuit)

    def search_lawsuits(self, term: str) -> list:
        s = Search(using=self.es, doc_type="lawsuit").query('multi_match',
            query=term,
            fields=['tribunal', 'numero', 'situacao', 'info_header.info*.conteudo', 'partes_todas*.nomes'])

        res = s.execute()
        return {"response": [hit.to_dict() for hit in res.hits]}

    def count_lawsuits(self) -> int:
        return Search(using=self.es, doc_type="lawsuit").count()
