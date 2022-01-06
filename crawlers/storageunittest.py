from time import sleep
import unittest
from storage import Storage


class TestStorage(unittest.TestCase):
    conn = Storage('juslite_elastic:9200')

    def test_1_if_storage_return_elasticsearch_client(self):
        self.assertTrue(self.conn.es.ping())

    def test_2_if_add_lawsuit_adds_one_new_lawsuit(self):
        new_dict = {
            "court":"lala",
            "number": "9999999-xx.2018.8.02.0001",
            "changes": [
            {
                "date": "22/02/2021",
                "title": "Remetido recurso eletrônico ao Tribunal de Justiça/Turma de recurso",
                "content": ""
            },
            {
                "date": "10/02/2021",
                "title": "Juntada de Documento",
                "content": "Nº Protocolo: WMAC.21.70031538-2 Tipo da Petição: Contrarrazões Data: 10/02/2021 19:27"
            },
            {
                "date": "06/01/2021",
                "title": "Ato Publicado",
                "content": "Relação :0003/2021 Data da Publicação: 21/01/2021 Número do Diário: 2738"
            }
            ]}
        self.conn.add_lawsuit(new_dict)
        sleep(1)
        self.assertEqual(new_dict,
        self.conn.search_lawsuits("9999999-xx.2018.8.02.0001")[0])
        self.conn.es.delete(index="lala", id="9999999-xx.2018.8.02.0001")
