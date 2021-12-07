import scrapy
from storage import Storage


def make_url(number: str) -> str:
    split1 = number.split(sep='-')
    split2 = split1[1].split(sep='.')
    return f'http://aplicacao4.tst.jus.br/consultaProcessual/consultaTstNumUnica.do?conscsjt=&numeroTst={split1[0]}&digitoTst={split2[0]}&anoTst={split2[1]}&orgaoTst=5&tribunalTst=02&varaTst={split2[-1]}&consulta=Consultar/'

# 0000441-05.2012.5.02.0058

class TstSpider(scrapy.Spider):
    name = 'tst_spider'

    def start_requests(self):
        self.start_urls = []
        file = open('tst_processos.csv', 'r')
        lines = file.readlines()
        for line in lines:
            self.start_urls.append(make_url(line))
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        processo = {}

        processo['court'] = "tst"

        numero = response.xpath("//td[@class='dadosProcesso']/b[text()='Processo:  ']/font/text()").get()
        numero = numero.split(sep=' ')[-1]
        numero = '0' * (25 - len(numero)) + numero
        processo['number'] = numero

        # processo['numero_alt_titulo'] =
        # processo['numero_alt_numero'] =
        processo['status'] = ""
        processo['class'] = ""
        processo['subject'] = ""

        # processo['juiz_titulo'] = "Relator"
        processo['judge'] = response.xpath("//td[@class='dadosProcesso']/b[contains(text(), 'Relator')]/font/text()").get()

        # processo['orgao_titulo'] = "Órgão Judiciante"
        processo['foro'] = response.xpath("//td[@class='dadosProcesso']/b[text()='Órgão Judicante: ']/font/text()").get()
        processo['vara'] = ""

        # Movimentações/histórico
        movs = []
        mov_tr = response.xpath("//tr[@class='historicoProcesso']")
        for row in mov_tr:
            mov = {}
            mov['date'] = row.xpath("./descendant::font[1]/text()").get()
            title = row.xpath("./descendant::font[2]/descendant-or-self::*/text()[1]").get()
            mov['title'] = title.replace("&nbsp", "")
            mov['content'] = ""
            movs.append(mov)
        processo['changes'] = movs

        # Movimentação mais relevante
        mov_relevante = {}
        for change in processo['changes']:
            if 'publicado' in change['title'].lower():
                mov_relevante['titulo'] = change['title']
                mov_relevante['data'] = change['date']
                break
            if 'julgado' in change['title'].lower():
                mov_relevante['titulo'] = change['title']
                mov_relevante['data'] = change['date']
                break
        if mov_relevante == {}:
            mov_relevante['data'] = processo['changes'][0]['date']
            mov_relevante['titulo'] = processo['changes'][0]['title']
        processo['mov_relevante'] = mov_relevante

        # Partes
        partes = []
        partes_td = response.xpath("//td[@class='titulo' and text()='Partes do processo']/following::td[@class='dadosProcesso']")
        titulos = partes_td.xpath("./b/text()").getall()
        nomes = partes_td.xpath("./text()").getall()
        for titulo, nome in zip(titulos, nomes):
            parte = {}
            parte['label'] = titulo
            parte['names'] = []
            parte['names'].append(nome)
            partes.append(parte)
        processo['parties'] = partes

        storage = Storage('172.17.0.2:9200')
        storage.add_lawsuit(processo)

        yield processo
