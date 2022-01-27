import scrapy


def make_url(number: str) -> str:
    split1 = number.split(sep='-')
    split2 = split1[1].split(sep='.')
    return f'http://aplicacao4.tst.jus.br/consultaProcessual/consultaTstNumUnica.do?conscsjt=&numeroTst={split1[0]}&digitoTst={split2[0]}&anoTst={split2[1]}&orgaoTst=5&tribunalTst=02&varaTst={split2[-1]}&consulta=Consultar/'

# 0000441-05.2012.5.02.0058

class TstSpider(scrapy.Spider):
    name = 'tst_spider'

    def start_requests(self):
        self.start_urls = []
        file = open('/home/rafa/Documents/projects/juslite/crawlers/tst_processos.csv', 'r')
        lines = file.readlines()
        for line in lines:
            self.start_urls.append(make_url(line))
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        processo = {}

        processo['tribunal'] = "tst"
        processo['url'] = response.request.url
        processo['sigilo'] = False
        numero = response.xpath("//td[@class='dadosProcesso']/b[contains(text(), 'Processo: ')]/font/text()").get()
        classe_numero = numero.split(sep=' ')
        processo['numero'] = '0' * (25 - len(classe_numero[-1])) + classe_numero[-1]
        processo['situacao'] = response.xpath("//td[@class='dadosProcesso']/b[text()=' - Fase Atual: ']/font/text()").get()
        processo['numeros_alternativos'] = self.get_numeros_alternativos(response.xpath("//td[@class='dadosProcesso']"))
        processo['info_header'] = self.get_info_header(response.xpath("//td[@class='dadosProcesso']//b[font]//text()[1]").getall()[-4:], classe_numero[0])
        processo['partes_todas'] = self.get_partes_todas(response.xpath("//td[@class='titulo']/following::td[@class='dadosProcesso']//text()").getall())
        processo['partes_principais'] = self.get_partes_principais(processo['partes_todas'])
        processo['moves'] = self.get_moves(response.xpath("//th[text()='Histórico do processo']/following::tr[@class='historicoProcesso']"))
        processo['ultima_mov'] = {"data": processo['moves'][0]['data'], "titulo": processo['moves'][0]['titulo']}

        yield processo

    def get_numeros_alternativos(self, numeros_alternativos):
        numeros_antigos = []
        numero_alt = {}
        numero_antigo = numeros_alternativos.xpath("./b[text()='Numeração antiga: ']/font/text()").get()
        if numero_antigo is not None:
            numero_alt['titulo'] = "Numeração antiga"
            numero_alt['numero'] = numero_antigo
            numeros_antigos.append(numero_alt)
        numero_alt = {}
        numero_alt['titulo'] = "Número no TRT de Origem"
        numero_alt['numero'] = numeros_alternativos.xpath("./b[contains(text(), 'Número no TRT de Origem: ')]/font/text()").get()
        numeros_antigos.append(numero_alt)
        return numeros_antigos

    def get_info_header(self, header, classe):
        info_header = {}
        info_header['info0'] = {"titulo": "Classe", "conteudo": classe}
        info_header['info1'] = {"titulo": "", "conteudo": ""}
        info_header['info2'] = {"titulo": "", "conteudo": ""}
        info_header['info3'] = {"titulo": header[0].split(':')[0], "conteudo": header[1]}
        info_header['info4'] = {"titulo": header[2].split(':')[0],"conteudo": header[3]}
        return info_header

    def get_partes_todas(self, partes_raw):
        partes_todas = []
        partes_format = []

        for i, string in enumerate(partes_raw):
            if ':' not in string:
                continue
            partes_format.append(partes_raw[i] + partes_raw[i + 1])

        this_parte = {}
        outros = []
        for parte in partes_format:
            if 'Advogad' not in parte and 'Procurador' not in parte.split(':')[0]:
                if this_parte != {}:
                    this_parte['outros'] = outros
                    outros = []
                    partes_todas.append(this_parte)
                    this_parte = {}
                split = str(parte).split(':')
                this_parte['titulo'] = split[0]
                this_parte['nomes'] = [split[1].strip()]
            else:
                outros.append(parte)
        this_parte['outros'] = outros
        partes_todas.append(this_parte)
        return partes_todas

    def get_partes_principais(self, partes_todas):
        partes_principais = {}
        partes_principais['parte1'] = partes_todas[0]['nomes'][0]
        partes_principais['parte2'] = partes_todas[1]['nomes'][0]
        return partes_principais

    def get_moves(self, moves_raw):
        moves = []
        for move in moves_raw:
            this_move = {}
            texts = move.xpath(".//text()").getall()
            new_texts = [item for item in texts if any(char.isalnum() for char in item.strip('&nbsp'))]
            this_move['data'] = new_texts[0]
            if 'Movimentação' in new_texts:
                new_texts.remove('Movimentação')
            this_move['titulo'] = new_texts[1].strip('&nbsp')
            if len(new_texts) > 2:
                this_move['conteudo'] = " ".join(new_texts[2:])
            doc = move.xpath(".//a/@href").get()
            if doc is not None:
                if 'http://' not in doc:
                    this_move['doc'] = "http://aplicacao4.tst.jus.br/consultaProcessual/" + doc
                else:
                    this_move['doc'] = doc
            moves.append(this_move)
        return moves
