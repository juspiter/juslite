import scrapy


class DjalSpider(scrapy.Spider):
    name = 'djal'
    base_url = "http://www.jusbrasil.com.br/diarios/"
    
    def start_requests(self):
        self.start_urls = [self.base_url + 'DJAL/2022/01/28/Jurisdicional-primeiro-grau']
        # self.start_urls = []
        for url in self.start_urls:
            yield self.make_requests_from_url(url)




    def parse(self, response):
        djid = response.xpath("//a[contains(text(), 'Página')/href]").get()
        djid = djid[8:18]
        print(djid)
        # next_page = self.base_url + djid
        # yield scrapy.Request(next_page, callback=self.parse)
