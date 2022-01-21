from scrapy.crawler import CrawlerProcess

from teste_scrapy.tstSpider.tstSpider.spiders.tst_spider import TstSpider

from esaj_spider import EsajSpider
from esaj import settings as my_settings

from scrapy.settings import Settings

# export ES_JAVA_OPTS="-Xms512m -Xmx512m"
# docker run -d --name juslitedb -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" --memory="1g" elasticsearch:7.14.2


crawler_settings = Settings()
crawler_settings.setmodule(my_settings)

process = CrawlerProcess(settings=crawler_settings)

# process.crawl(TstSpider)
process.crawl(EsajSpider)
process.start()

# print(storage.search_lawsuits("marili"))
