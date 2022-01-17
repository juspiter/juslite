import scrapy


#"https://www2.tjal.jus.br/cpopg/search.do?conversationId=&cbPesquisa=NUMPROC&dadosConsulta.valorConsultaNuUnificado={number}&dadosConsulta.valorConsultaNuUnificado=UNIFICADO&dadosConsulta.valorConsulta=&dadosConsulta.tipoNuProcesso=UNIFICADO&uuidCaptcha="


class EsajSpider(scrapy.Spider):
    name = 'esaj_spider'

    def make_url(self, number: str) -> str:
        num_t = number.split('.')
        if num_t[2] == "8" and num_t[3] == "02":
            url = f"https://www2.tjal.jus.br/cpopg/search.do?conversationId=&cbPesquisa=NUMPROC&dadosConsulta.valorConsultaNuUnificado={number}&dadosConsulta.valorConsultaNuUnificado=UNIFICADO&dadosConsulta.valorConsulta=&dadosConsulta.tipoNuProcesso=UNIFICADO&uuidCaptcha="
            self.court = "tjal"
        else:
            url = f"https://esaj.tjce.jus.br/cpopg/search.do?conversationId=&cbPesquisa=NUMPROC&dadosConsulta.valorConsultaNuUnificado={number}&dadosConsulta.valorConsultaNuUnificado=UNIFICADO&dadosConsulta.valorConsulta=&dadosConsulta.tipoNuProcesso=UNIFICADO&uuidCaptcha="
            self.court = "tjce"
        return url

    def start_requests(self):
        # self.start_urls = []
        # file = open('/home/rafa/Documents/projects/juslite/crawlers/tjal_processos.csv', 'r')
        # lines = file.readlines()
        # for line in lines:
        #     self.start_urls.append(self.make_url(line))
        # for url in self.start_urls:
        #     yield self.make_requests_from_url(url)
        yield scrapy.Request("https://www2.tjal.jus.br/cpopg/show.do?processo.codigo=01000O7550000&processo.foro=1&processo.numero=0710802-55.2018.8.02.0001", self.parse)

    def parse(self, response):
        processo = {}

        numero = response.xpath("//span[@id='numeroProcesso']/text()").get()
        processo['numero'] = ''.join([c for c in numero if c in "0123456789.-"])

        tribunal = response.xpath("//a[@class='header__navbar__brand__initials']/text()").get()
        processo['tribunal'] = tribunal.strip().lower()

        processo['url'] = response.request.url

        # Método que checa se o processo está sob sigilo
            # processo['sigilo'] = True
            # yield processo

        processo['sigilo'] = False
        processo['situacao'] = response.xpath("//span[@id='labelSituacaoProcesso']/text()").get()

        processo['moves'] = self.get_info_moves(response.xpath("//tbody[@id='tabelaTodasMovimentacoes']"))
        processo['ultima_mov'] = {"data": processo['moves'][0]['data'], "titulo": processo['moves'][0]['titulo']}
        processo['info_header'] = self.get_info_header(response.xpath("//div[@id='containerDadosPrincipaisProcesso']"))
        # processo['partes_todas'] = self.get_info_partes_todas(response.xpath("//table[@id='tableTodasPartes']/tbody/tr"))
        processo['partes_principais'] = self.get_info_partes_principais(response.xpath("//table[@id='tablePartesPrincipais']"))
        yield processo

    def get_info_moves(self, moves):
        info_moves = []

        for move in moves.xpath("./tr"):
            this_move = {}
            this_move['data'] = move.xpath("./td[@class='dataMovimentacao']/text()").get().strip('\n\t ')
            this_move['titulo'] = move.xpath("./td[@class='descricaoMovimentacao']/text()").get().strip('\n\t ')
            this_move['conteudo'] = move.xpath("./td[@class='descricaoMovimentacao']/span/text()").get().strip('\n\t ')
            this_move['doc'] = move.xpath("./td/a[@class='linkMovVincProc']/@href").get()
            info_moves.append(this_move)
        return info_moves

    def get_info_header(self, header):
        info_header = []  # lista de dicts conforme novo template

        for head in header.xpath("./div[2]/div"):
            this_header = {}
            this_header['titulo'] = head.xpath("./span/text()").get().strip('\n\t ')
            this_header['conteudo'] = head.xpath("./div/span/text()").get().strip('\n\t ')
            info_header.append(this_header)
        return info_header

    # def get_info_partes_todas(self, partes):
    #     info_partes = [] # lista de dicts?
    #     return info_partes

    def get_info_partes_principais(self, partes):
        info_partes = {}
        info_partes['parte1'] = partes.xpath(".//tr[1]/td[@class='nomeParteEAdvogado'][1]/text()[1]").get().strip('\n\t ')
        info_partes['parte2'] = partes.xpath(".//tr[2]/td[@class='nomeParteEAdvogado'][1]/text()[1]").get().strip('\n\t ')
        return info_partes
