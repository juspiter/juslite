"""
{
		"number": "0710802-55.2018.8.02.0001",
		"changes":
		[
			{
				"date": "22/02/2021",
				"title": "Remetido recurso eletrônico ao Tribunal de Justiça/Turma de recurso",
				"content": ""
			},
			{
				"date": "10/02/2021",
				"title": "Juntada de Documento",
				"content": "Nº Protocolo: WMAC.21.70031538-2 Tipo da Petição: Contrarrazões Data: 10/02/2021 19:27"
			}
		]
	}
"""

import re

def parse_crawl(soup):
    lawsuit = {}
    changes = []
    lawsuit.update({"number": soup.find(id="numeroProcesso").get_text().strip()})
    all_move = soup.find(id="tabelaTodasMovimentacoes")
    moves = all_move.find_all('tr')

    for move in moves:
        change = {}
        change.update({"date": move.find(class_="dataMovimentacao").get_text().strip()})
        desc = re.sub('[\t]+', ' ', move.find(class_="descricaoMovimentacao").get_text())
        desc = desc.strip().splitlines()
        desc = list(filter(None, desc))
        desc[:] = [item for item in desc if item != ' ']
        change.update({"title": desc[0]})
        change.update({"content": " ".join(desc[1:])})
        changes.append(change)

    lawsuit.update({"changes": changes})
    return lawsuit
