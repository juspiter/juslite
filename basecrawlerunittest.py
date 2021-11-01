from unittest import TestCase
from basecrawler import BaseCrawler
import requests


class TestBaseCrawler(TestCase):
    def test_request_html(self):
        crawl = BaseCrawler("https://www2.tjal.jus.br/cpopg/search.do?conversationId=&cbPesquisa=NUMPROC&dadosConsulta.valorConsultaNuUnificado=0710802-55.2018.8.02.0001&dadosConsulta.valorConsultaNuUnificado=UNIFICADO&dadosConsulta.valorConsulta=&dadosConsulta.tipoNuProcesso=UNIFICADO&uuidCaptcha=")
        self.assertEqual(crawl.req.status_code, requests.codes.ok)
