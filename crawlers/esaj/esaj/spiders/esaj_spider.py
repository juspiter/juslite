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
        self.start_urls = []
        file = open('/home/anderson/Dev/42_labs/juslite/crawlers/tjal_processos.csv', 'r')
        lines = file.readlines()
        for line in lines:
            self.start_urls.append(self.make_url(line))
        for url in self.start_urls:
            yield self.make_requests_from_url(url)
        # yield scrapy.Request("https://www2.tjal.jus.br/cpopg/search.do?conversationId=&cbPesquisa=NUMPROC&dadosConsulta.valorConsultaNuUnificado=asdasdasdsa&dadosConsulta.valorConsultaNuUnificado=UNIFICADO&dadosConsulta.valorConsulta=&dadosConsulta.tipoNuProcesso=UNIFICADO&uuidCaptcha=", self.parse)

        # yield scrapy.Request("https://www2.tjal.jus.br/cpopg/search.do?conversationId=&cbPesquisa=NUMPROC&dadosConsulta.valorConsultaNuUnificado=0000001-03.2017.8.02.0084&dadosConsulta.valorConsultaNuUnificado=UNIFICADO&dadosConsulta.valorConsulta=&dadosConsulta.tipoNuProcesso=UNIFICADO&uuidCaptcha=", self.parse)

    # def check_validity(self, response):
    #     numero = response.xpath("//span[@id='numeroProcesso']/text()").get()
    #     if numero is None:
    #         yield "NOT_VALID"
    #     else:
    #         self.parse(response)

    def parse(self, response):
        processo = {}
        sob_sigilo = False if response.xpath("//span[@id='numeroProcesso']/text()").get() else True
        if sob_sigilo == False:
            processo['sigilo'] = False
            numero = response.xpath("//span[@id='numeroProcesso']/text()").get()
            processo['numero'] = ''.join([c for c in numero if c in "0123456789.-"])

            tribunal = response.xpath("//a[@class='header__navbar__brand__initials']/text()").get()
            processo['tribunal'] = tribunal.strip().lower()

            processo['url'] = response.request.url

            processo['situacao'] = response.xpath("//span[@id='labelSituacaoProcesso']/text()").get()

            processo['moves'] = self.get_info_moves(response.xpath("//tbody[@id='tabelaTodasMovimentacoes']"))
            processo['ultima_mov'] = {"data": processo['moves'][0]['data'], "titulo": processo['moves'][0]['titulo']}
            processo['info_header'] = self.get_info_header(response.xpath("//div[@id='containerDadosPrincipaisProcesso']"))
            processo['partes_todas'] = self.get_info_partes_todas(response.xpath("//table[@id='tableTodasPartes']/tr"))
            if processo['partes_todas'] == []:
                processo['partes_todas'] = self.get_info_partes_todas(response.xpath("//table[@id='tablePartesPrincipais']/tr"))
            processo['partes_principais'] = self.get_info_partes_principais(response.xpath("//table[@id='tablePartesPrincipais']"))
        elif "show.do" in response.request.url:
            processo['sigilo'] = True
            processo['url'] = response.request.url
            processo['tribunal'] = processo['url'].split('.')[1]
            processo['numero'] = processo['url'].split('=')[-1]

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
        info_header = []

        for head in header.xpath("./div[2]/div"):
            this_header = {}
            this_header['titulo'] = head.xpath("./span/text()").get().strip('\n\t ')
            this_header['conteudo'] = head.xpath("./div/span/text()").get().strip('\n\t ')
            info_header.append(this_header)
        return info_header

    def get_info_partes_todas(self, partes):
        info_partes = []
        for parte in partes:
            this_parte = {}
            this_parte['titulo'] = parte.xpath("./td[1]/span/text()").get().strip()
            nomes = parte.xpath("./td[2]//text()").getall()
            this_parte['nomes'] = [nomes.pop(0).strip()]

            outros = []
            for i, outro in enumerate(nomes):
                if outro.strip() != '':
                    continue
                outros.append(nomes[i + 1].strip() + " " + nomes[i + 2].strip())

            this_parte['outros'] = outros
            info_partes.append(this_parte)
        return info_partes

    def get_info_partes_principais(self, partes):
        info_partes = {}
        info_partes['parte1'] = partes.xpath(".//tr[1]/td[@class='nomeParteEAdvogado'][1]/text()[1]").get().strip('\n\t ')
        info_partes['parte2'] = partes.xpath(".//tr[2]/td[@class='nomeParteEAdvogado'][1]/text()[1]").get().strip('\n\t ')
        return info_partes
