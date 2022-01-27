from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from tst_spider import TstSpider
from tstSpider import settings as tst_settings

crawler_settings = Settings()
crawler_settings.setmodule(tst_settings)
process = CrawlerProcess(settings=crawler_settings)
process.crawl(TstSpider)
process.start()
