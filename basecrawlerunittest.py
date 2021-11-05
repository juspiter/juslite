from unittest import TestCase
from basecrawler import BaseCrawler
import requests


class TestBaseCrawler(TestCase):
    crawl = BaseCrawler("0710802-55.2018.8.02.0001")

    def test_1_request_html(self):
        self.assertEqual(self.crawl.status_code, requests.codes.ok)

    def test_2_if_found_lawsuit_is_true(self):
        self.assertTrue(self.crawl.found_lawsuit)

    def test_3_if_found_lawsuit_is_false(self):
        fail_crawl = BaseCrawler("0710x02-55.2018.8.02.0001")
        self.assertFalse(fail_crawl.found_lawsuit)

    def test_4_if_soup_is_not_none(self):
        self.assertIsNotNone(self.crawl.soup)

    def test_5_if_lawsuit_number_is_correct(self):
        result = self.crawl.parse_lawsuit()
        self.assertEqual(result["number"], "0710802-55.2018.8.02.0001")

    def test_6_if_lawsuit_least_recent_date_is_correct(self):
        result = self.crawl.parse_lawsuit()
        result = result["changes"][-1]
        self.assertEqual(result["date"], "02/05/2018")

    def test_7_if_lawsuit_title_is_correct(self):
        result = self.crawl.parse_lawsuit()
        result = result["changes"][-5]
        self.assertEqual(result["title"], "Audiência Designada")

    def test_8_if_lawsuit_content_is_correct(self):
        result = self.crawl.parse_lawsuit()
        result = result["changes"][-5]
        self.assertEqual(result["content"], "Conciliação Data: 24/09/2018 Hora 14:00 Local: Sala de Audiência Situacão: Realizada")
