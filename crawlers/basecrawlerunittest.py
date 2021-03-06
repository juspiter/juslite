from unittest import TestCase
from basecrawler import BaseCrawler
import requests


class TestBaseCrawler(TestCase):
    crawl = BaseCrawler("0000001-03.2011.8.02.0055")
    lawsuit = crawl.crawl_lawsuit()

    def test_01_request_html(self):
        self.assertEqual(self.crawl.status_code, requests.codes.ok)

    def test_02_if_found_lawsuit_is_true(self):
        self.assertTrue(self.crawl.found_lawsuit)

    def test_03_if_found_lawsuit_is_false(self):
        fail_crawl = BaseCrawler("0710x02-55.2018.8.02.0001")
        self.assertFalse(fail_crawl.found_lawsuit)

    def test_04_if_soup_is_not_none(self):
        self.assertIsNotNone(self.crawl.soup)

    def test_05_if_lawsuit_number_is_correct(self):
        result = self.lawsuit
        self.assertEqual(result["number"], "0000001-03.2011.8.02.0055")

    def test_06_if_lawsuit_least_recent_date_is_correct(self):
        result = self.lawsuit
        result = result["changes"][-1]
        self.assertEqual(result["date"], "04/01/2011")

    def test_07_if_lawsuit_title_is_correct(self):
        result = self.lawsuit
        result = result["changes"][-5]
        self.assertEqual(result["title"], "Conclusos")

    def test_08_if_lawsuit_content_is_correct(self):
        result = self.lawsuit
        result = result["changes"][-4]
        self.assertEqual(result["content"], "Certidão recebimento dos autos, mediante sistema de distribuição.")

    def test_09_if_lawsuit_status_is_correct(self):
        result = self.lawsuit
        self.assertEqual(result["status"], "Baixado")

    def test_10_if_lawsuit_class_is_correct(self):
        result = self.lawsuit
        self.assertEqual(result["class"], "Execução de Título Extrajudicial")

    def test_11_if_lawsuit_subject_is_correct(self):
        result = self.lawsuit
        self.assertEqual(result["subject"], "Cédula Hipotecária")

    def test_12_if_lawsuit_judge_is_correct(self):
        result = self.lawsuit
        self.assertEqual(result["judge"], "Marina Gurgel da Costa")

    def test_13_if_lawsuit_foro_is_correct(self):
        result = self.lawsuit
        self.assertEqual(result["foro"], "Foro de Santana do Ipanema")

    def test_14_if_lawsuit_vara_is_correct(self):
        result = self.lawsuit
        self.assertEqual(result["vara"], "2ª Vara de Santana do Ipanema (Sucessões)")

    def test_15_if_lawsuit_most_relevant_date_is_correct(self):
        result = self.lawsuit
        self.assertEqual(result["mov_relevante"]["data"], "06/11/2013")
        self.assertEqual(result["mov_relevante"]["titulo"], "Transitado em Julgado")

    def test_16_if_lawsuit_dont_have_judged_or_published(self):
        new_crawl = BaseCrawler("0000000-25.2007.8.02.0001")
        result = new_crawl.crawl_lawsuit()
        self.assertEqual(result["mov_relevante"]["data"], "03/09/2014")
        self.assertEqual(result["mov_relevante"]["titulo"], "Arquivado Definitivamente")
