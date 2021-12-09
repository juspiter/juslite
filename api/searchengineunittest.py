from unittest import TestCase
from searchengine import SearchEngine


class TestSearchEngine(TestCase):
    search = SearchEngine('juslite_elastic:9200')

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

    def test_06_search_invalid_number_return_error_message(self):
        num = "0000001-03.2011.8.02.005599999999999999999999999999999999999999999999999999999"
        res = self.search.get_results(num)
        self.assertEqual({"response": [], "status_code": 1, "status": "Número inválido"}, res)

    def test_07_search_valid_raw_number_return_lawsuit(self):
        num = "00000010320118020055"
        res = self.search.get_results(num)
        self.assertEqual("0000001-03.2011.8.02.0055", res['response'][0]['number'])

    def test_08_search_valid_raw_number_without_zeros_return_lawsuit(self): #validar no futuro
        num = "10320118020055"
        res = self.search.get_results(num)
        self.assertEqual({"response": [], "status_code": 1, "status": "Número inválido"}, res)

    def test_09_search_invalid_number_return_unknown_lawsuit(self):
        num = "9999999-03.2011.8.02.9999"
        res = self.search.get_results(num)
        self.assertEqual({"response": [], "status_code": 4, "status": "Processo desconhecido"}, res)

