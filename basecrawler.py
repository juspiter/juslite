import requests
from bs4 import BeautifulSoup

#https://www2.tjal.jus.br/cpopg/show.do?processo.codigo=2C00008XG0000&processo.foro=84&processo.numero=0000001-03.2017.8.02.0084
#0000001-03.2011.8.02.0055

class BaseCrawler:
    def __init__(self, number: str):
        num_t = number.split('.')
        if num_t[2] == "8" and num_t[3] == "02":
            url = f"https://www2.tjal.jus.br/cpopg/search.do?conversationId=&cbPesquisa=NUMPROC&dadosConsulta.valorConsultaNuUnificado={number}&dadosConsulta.valorConsultaNuUnificado=UNIFICADO&dadosConsulta.valorConsulta=&dadosConsulta.tipoNuProcesso=UNIFICADO&uuidCaptcha="
            self.court = "tjal"
        else:
            url = f"https://esaj.tjce.jus.br/cpopg/search.do?conversationId=&cbPesquisa=NUMPROC&dadosConsulta.valorConsultaNuUnificado={number}&dadosConsulta.valorConsultaNuUnificado=UNIFICADO&dadosConsulta.valorConsulta=&dadosConsulta.tipoNuProcesso=UNIFICADO&uuidCaptcha="
            self.court = "tjce"

        try:
            response = requests.get(url, timeout=5)
        except Exception:
            self.soup = None
            return

        self.status_code = response.status_code
        self.found_lawsuit = True if 'show.do' in response.url else False

        if self.status_code == requests.codes.ok and self.found_lawsuit == True:
            self.soup = BeautifulSoup(response.text, 'html.parser')
        else:
            self.soup = None

    def crawl_lawsuit(self) -> dict:
        lawsuit = {}

        if not self.soup:
            return lawsuit

        lawsuit.update({"court": self.court})

        lawsuit.update({"number": self.soup.find(
            id="numeroProcesso").get_text(strip=True)})

        try:
            lawsuit.update({"status": self.soup.find(
                id="labelSituacaoProcesso").get_text(strip=True)})
        except AttributeError:
            lawsuit.update({"status": ""})

        lawsuit.update({"class": self.soup.find(
            id="classeProcesso").get_text(strip=True)})

        lawsuit.update({"subject": self.soup.find(
            id="assuntoProcesso").get_text(strip=True)})

        lawsuit.update({"foro": self.soup.find(
            id="foroProcesso").get_text(strip=True)})

        lawsuit.update({"vara": self.soup.find(
            id="varaProcesso").get_text(strip=True)})

        try:
            lawsuit.update({"judge": self.soup.find(
                id="juizProcesso").get_text(strip=True)})
        except AttributeError:
            lawsuit.update({"judge": ""})

        lawsuit.update({"parties": self.crawl_lawsuit_parties()})
        lawsuit.update({"changes": self.crawl_lawsuit_changes()})
        lawsuit.update({"mov_relevante": self.crawl_lawsuit_mov_relevante(lawsuit['changes'])})
        return lawsuit

    def crawl_lawsuit_parties(self) -> list:
        parties = []

        part_table = self.soup.find('table', id="tableTodasPartes")
        if part_table is None:
            part_table = self.soup.find('table', id="tablePartesPrincipais")

        parties_types_soup = part_table.find_all(
            class_="mensagemExibindo tipoDeParticipacao")
        parties_types = [type.get_text(strip=True) for type in parties_types_soup]

        parties_names_soup = part_table.find_all(class_="nomeParteEAdvogado")
        parties_names = []
        for name_group in parties_names_soup:
            parties_names.append([name for name in name_group.stripped_strings])

        for label, names in zip(parties_types, parties_names):
            party = {}
            party.update({"label": label, "names": names})

            parties.append(party)
        return parties

    def crawl_lawsuit_changes(self) -> list:
        changes = []

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

        return changes

    def crawl_lawsuit_mov_relevante(self, changes: list) -> dict:
        mov_relevante = {}
        for change in changes:
            if 'publicado' in change['title'].lower():
                mov_relevante['titulo'] = change['title']
                mov_relevante['data'] = change['date']
                return mov_relevante
            if 'julgado' in change['title'].lower():
                mov_relevante['titulo'] = change['title']
                mov_relevante['data'] = change['date']
                return mov_relevante
        mov_relevante['data'] = changes[0]['date']
        mov_relevante['titulo'] = changes[0]['title']
        return mov_relevante
