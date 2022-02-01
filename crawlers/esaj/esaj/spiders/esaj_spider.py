import scrapy
import datetime


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
        file = open('tjal_processos.csv', 'r')
        lines = file.readlines()
        file.close()
        file = open('tjce_processos.csv', 'r')
        lines += file.readlines()
        file.close()
        for line in lines:
            self.start_urls.append(self.make_url(line))
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        processo = {}
        processo['data_atualizacao'] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        sob_sigilo = False if response.xpath("//span[@id='numeroProcesso']/text()").get() else True
        if sob_sigilo == False:
            processo['sigilo'] = False
            numero = response.xpath("//span[@id='numeroProcesso']/text()").get()
            processo['numero'] = ''.join([c for c in numero if c in "0123456789.-"])

            tribunal = response.xpath("//a[@class='header__navbar__brand__initials']/text()").get()
            processo['tribunal'] = tribunal.strip().lower()

            processo['url'] = response.request.url

            processo['situacao'] = response.xpath("//span[@id='labelSituacaoProcesso']/text()").get()

            processo['moves'] = self.get_info_moves(response.xpath("//tbody[@id='tabelaTodasMovimentacoes']"), response)
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

    def get_info_moves(self, moves, response):
        info_moves = []

        for move in moves.xpath("./tr"):
            this_move = {}
            this_move['data'] = move.xpath("./td[@class='dataMovimentacao']/text()").get().strip('\n\t ')
            this_move['titulo'] = move.xpath("./td[@class='descricaoMovimentacao']/text()").get().strip('\n\t ')
            if this_move['titulo'] == "":
                this_move['titulo'] = move.xpath("./td[@class='descricaoMovimentacao']/a/text()").get().strip('\n\t ')
            this_move['conteudo'] = move.xpath("./td[@class='descricaoMovimentacao']/span/text()").get().strip('\n\t ')
            this_move['doc'] = move.xpath("./td/a[@class='linkMovVincProc']/@href").get()
            if this_move['doc'] == "#liberarAutoPorSenha":
                this_move['doc'] = "doc_sigilo"
            elif this_move['doc'] is not None and 'http' not in this_move['doc']:
                this_move['doc'] = "https://" + response.request.url.split('/')[2] + this_move['doc']
            info_moves.append(this_move)
        return info_moves

    def get_info_header(self, header):
        info_header = {}

        raw_header = header.xpath("./div[2]/div")
        for i in range(5):
            this_header = {}
            if len(raw_header) > i:
                head = raw_header[i]
                this_header['titulo'] = head.xpath("./span/text()").get().strip('\n\t ')
                this_header['conteudo'] = head.xpath("./div/span/text()").get().strip('\n\t ')
                info_header['info' + str(i)] = this_header
            else:
                info_header['info' + str(i)] = {"titulo": "", "conteudo": ""}
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
