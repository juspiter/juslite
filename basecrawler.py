import requests
from bs4 import BeautifulSoup

#https://www2.tjal.jus.br/cpopg/show.do?processo.codigo=2C00008XG0000&processo.foro=84&processo.numero=0000001-03.2017.8.02.0084

class BaseCrawler:
    def __init__(self, number: str):
        url = f"https://www2.tjal.jus.br/cpopg/search.do?conversationId=&cbPesquisa=NUMPROC&dadosConsulta.valorConsultaNuUnificado={number}&dadosConsulta.valorConsultaNuUnificado=UNIFICADO&dadosConsulta.valorConsulta=&dadosConsulta.tipoNuProcesso=UNIFICADO&uuidCaptcha="
        try:
            response = requests.get(url, timeout=5)
        except:
            self.soup = None
            return

        self.status_code = response.status_code
        self.found_lawsuit = True if 'show.do' in response.url else False

        if self.status_code == requests.codes.ok and self.found_lawsuit == True:
            self.soup = BeautifulSoup(response.text, 'html.parser')
        else:
            self.soup = None

    def parse_lawsuit(self) -> dict:
        lawsuit = {}
        changes = []

        if not self.soup:
            return lawsuit

        lawsuit.update({"number": self.soup.find(
            id="numeroProcesso").get_text(strip=True)})

        move_table = self.soup.find('tbody', id="tabelaTodasMovimentacoes")
        moves = move_table.find_all('tr')

        for move in moves:
            change = {}

            change.update({"date": move.find(
                'td', class_="dataMovimentacao").get_text(strip=True)})

            desc = move.find(
                'td', class_="descricaoMovimentacao").get_text('\n', strip=True)
            desc = desc.splitlines()

            change.update({"title": desc[0]})
            change.update({"content": ' '.join(desc[1:])})

            changes.append(change)

        lawsuit.update({"changes": changes})
        return lawsuit
