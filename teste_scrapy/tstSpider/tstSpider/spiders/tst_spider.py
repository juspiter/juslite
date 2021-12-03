import scrapy


class TstSpider(scrapy.Spider):
    name = "tstspider"
    start_urls = ['http://aplicacao4.tst.jus.br/consultaProcessual/consultaTstNumUnica.do?conscsjt=&numeroTst=1001074&digitoTst=51&anoTst=2018&orgaoTst=5&tribunalTst=02&varaTst=0005&consulta=Consultar']

    def parse(self, response):
        titles = []
        for title in response.xpath('//td[@class="dadosProcesso"]/b/text()').getall():
            if not '\t' in title:
                titles.append(title)

        header_info = []
        for info in response.xpath('//td[@class="dadosProcesso"]/b/font/text()').getall():
            if not '\t' in info:
                header_info.append(info)

        parties = []
        # for party in response.xpath('//tr/td[@class="dadosProcesso"]/../*/text()').getall():
            # if not '\t' in party:
                # parties.append(party)
        for member in response.xpath('//tr/td[@class="dadosProcesso"]'):
            party = {}
            appellant = member.xpath('.//b[text()="Recorrente(s): "]/parent/sibling::text()').get()
            attorney = member.xpath('.//b[text()="Advogado:"]/parent/sibling::text()').get()
            party['appellant'] = appellant
            party['attorney'] = attorney
            parties.append(party)

        changes = []
        for change in response.xpath('//td[@class="historicoProcesso"]/*/descendant::text()').getall():
            if not '\t' in change:
                changes.append(change)

        yield {
            'referendary': response.xpath('//b[text()="Relator: "]/font/text()').get(),
            'titles': titles,
            'header_info': header_info,
            'parties': parties,
            'changes': changes,
        }

