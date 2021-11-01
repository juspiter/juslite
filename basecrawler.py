import requests
from bs4 import BeautifulSoup


"""
1221: <table>
    1238: <tbody id="tabelaUltimasMovimentacoes">
    4522: </tbody>
4527: </table>
"""

class BaseCrawler:
    def __init__(self, url: str):
        self.req = requests.get(url)
        self.soup = BeautifulSoup(self.req.text, 'html.parser')