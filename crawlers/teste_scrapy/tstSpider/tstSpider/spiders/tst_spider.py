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
        file = open('/home/anderson/Dev/42_labs/juslite/crawlers/tst_processos.csv', 'r')
        lines = file.readlines()
        for line in lines:
            self.start_urls.append(make_url(line))
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        processo = {}

        processo['tribunal'] = "tst"
        processo['url'] = response.request.url
        numero = response.xpath("//td[@class='dadosProcesso']/b[contains(text(), 'Processo: ')]/font/text()").get()
        classe_numero = numero.split(sep=' ')
        processo['numero'] = '0' * (25 - len(classe_numero[-1])) + classe_numero[-1]

        processo['situacao'] = response.xpath("//td[@class='dadosProcesso']/b[text()=' - Fase Atual: ']/font/text()").get()

        processo['numeros_alternativos'] = self.get_numeros_alternativos(response.xpath("//td[@class='dadosProcesso']"))

        processo['info_header'] = self.get_info_header(response.xpath("//td[@class='dadosProcesso']//b[font]//text()[1]").getall()[-4:], classe_numero[0])

        processo['partes_todas'] = self.get_partes_todas(response.xpath("//tr[td[@class='titulo']]/following-sibling::tr/td[not(table)]//text()").getall())


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
        info_header['info0'] = {
            "titulo" : "Classe",
            "conteudo" : classe
        }
        info_header['info1'] = {
            "titulo" : "",
            "conteudo" : ""
        }
        info_header['info2'] = {
            "titulo" : "",
            "conteudo" : ""
        }
        info_header['info3'] = {
            "titulo" : header[0].split(':')[0],
            "conteudo" : header[1]
        }
        info_header['info4'] = {
            "titulo" : header[2].split(':')[0],
            "conteudo" : header[3]
        }
        return info_header

    def get_partes_todas(self, partes_raw):
        partes_todas = []

        for i, element in enumerate(partes_raw) :
        # while partes_raw[i] :
            this_parte = {}
            if partes_raw[i] == '\xa0' and i > 0 :
                this_parte['titulo'] = partes_raw[i-4]
                this_parte['nomes'] = [partes_raw[i-3]]
                this_parte['outros'] = [partes_raw[i-2] + partes_raw[i-1]]
                partes_todas.append(this_parte)
        return partes_todas