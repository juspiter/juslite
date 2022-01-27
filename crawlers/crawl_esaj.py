from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from esaj_spider import EsajSpider
from esaj import settings as esaj_settings

crawler_settings = Settings()
crawler_settings.setmodule(esaj_settings)
process = CrawlerProcess(settings=crawler_settings)
process.crawl(EsajSpider)
process.start()
