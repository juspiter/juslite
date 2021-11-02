import re


def parse_crawl(soup):
    lawsuit = {}
    changes = []
    lawsuit.update({"number": soup.find(id="numeroProcesso").get_text().strip()})
    move_table = soup.find(id="tabelaTodasMovimentacoes")
    moves = move_table.find_all('tr')

    for move in moves:
        change = {}
        change.update({"date": move.find(
            class_="dataMovimentacao").get_text().strip()})
        desc = re.sub('[\t]+', ' ', move.find(
            class_="descricaoMovimentacao").get_text())
        desc = desc.strip().splitlines()
        desc = list(filter(None, desc))
        desc[:] = [item for item in desc if item != ' ']
        change.update({"title": desc[0]})
        change.update({"content": " ".join(desc[1:])})
        changes.append(change)

    lawsuit.update({"changes": changes})
    return lawsuit
