def parse_crawl(soup):
    lawsuit = {}
    changes = []

    lawsuit.update({"number": soup.find(
        id="numeroProcesso").get_text(strip=True)})

    move_table = soup.find('tbody', id="tabelaTodasMovimentacoes")
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
