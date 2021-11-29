from unittest import TestCase

from searchengine import SearchEngine
from storage import Storage


class TestSearchEngine(TestCase):
    search = SearchEngine('172.17.0.2:9200')

    def test_01_search_by_number_return_one_lawsuit(self):
        num = "0000001-03.2011.8.02.0055"
        res = self.search.get_results(num)
        self.assertEqual(1, len(res['response']))

    def test_02_search_by_number_return_right_lawsuit(self):
        num = "0000001-03.2011.8.02.0055"
        res = self.search.get_results(num)
        self.assertEqual(num, res['response'][0]['number'])

    def test_03_search_valid_term_return_list(self):
        term = "Dano"
        res = self.search.get_results(term)
        self.assertNotEqual(0, len(res['response']))

    def test_04_search_invalid_court_return_error_message(self):
        num = "0000001-03.2011.9.03.0055"
        res = self.search.get_results(num)
        self.assertEqual({"response": [], "status_code": 2, "status": "Tribunal não suportado"}, res)

    def test_05_search_invalid_year_return_error_message(self):
        num = "0000001-03.2911.8.02.0055"
        res = self.search.get_results(num)
        self.assertEqual({"response": [], "status_code": 3, "status": "Ano inválido"}, res)

# testar "0000001-03.2111.8.02.0055" == invalido
# testar "00000010320119030055" == valido
# testar "0000001-03.2011.8.02.005599999999999999999999999999999999999999999999999999999" == inválido(?)
