import unittest

from pymongo import response
from storage import Storage


class TestStorage(unittest.TestCase):
    conn = Storage('172.17.0.3:27017')

    def test_if_storage_return_mongo_client(self):
        self.assertIsNotNone(self.conn)

    def test_if_get_lawsuit_gets_lawsuit(self):
        response = self.conn.get_lawsuit()
        self.assertIsNotNone(response)

    def test_if_add_lawsuit_add_one_new_lawsuit(self):
        prev_qnt = self.conn.count_lawsuits()
        self.conn.add_lawsuit()
        new_qnt = self.conn.count_lawsuits()
        self.assertEqual(prev_qnt + 1, new_qnt)

    def test_if_delete_lawsuit_delete_one_lawsuit(self):
        prev_qnt = self.conn.count_lawsuits()
        self.conn.delete_lawsuit()
        new_qnt = self.conn.count_lawsuits()
        self.assertEqual(prev_qnt - 1, new_qnt)

    def test_if_lawsuit_content_is_the_same(self):
        self.conn.add_lawsuit()
        response = self.conn.get_lawsuit()
        self.assertEqual(response["number"], "0710802-55.2018.8.02.0001")
        self.assertEqual(response["changes"], [
                {
                    "date": "22/02/2021",
                    "title": "Remetido recurso eletrônico ao Tribunal de Justiça/Turma de recurso",
                    "content": ""
                },
                {
                    "date": "10/02/2021",
                    "title": "Juntada de Documento",
                    "content": "Nº Protocolo: WMAC.21.70031538-2 Tipo da Petição: Contrarrazões Data: 10/02/2021 19:27"
                }
            ])
        self.conn.delete_lawsuit()
