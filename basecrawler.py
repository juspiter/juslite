import requests
from bs4 import BeautifulSoup


class BaseCrawler:
    def __init__(self, url: str):
        self.req = requests.get(url)
        self.soup = BeautifulSoup(self.req.text, 'html.parser')
