from storage import Storage
from basecrawler import BaseCrawler
from scrapy.crawler import CrawlerProcess
from teste_scrapy.tstSpider.tstSpider.spiders.tst_spider import TstSpider

# export ES_JAVA_OPTS="-Xms512m -Xmx512m"
# docker run -d --name juslitedb -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" --memory="1g" elasticsearch:7.14.2


storage = Storage('juslite_elastic:9200')

file = open('tjce_processos.csv', 'r')
lines = file.readlines()

for line in lines:
    crawl = BaseCrawler(line[:-1])
    storage.add_lawsuit(crawl.crawl_lawsuit())
    print("crawled process: " + line[:-1])

file = open('tjal_processos.csv', 'r')
lines = file.readlines()

for line in lines:
    crawl = BaseCrawler(line[:-1])
    storage.add_lawsuit(crawl.crawl_lawsuit())
    print("crawled process: " + line[:-1])

process = CrawlerProcess(settings={
    "FEEDS": {
        "processotrabalhista.json": {"format": "json"}
    },
})

process.crawl(TstSpider)
process.start()

# crawl = BaseCrawler("0218226-29.2020.8.06.0001")
# print(crawl.crawl_lawsuit())


# curl -X PUT "localhost:9200/tjal?pretty"
# curl -X PUT "localhost:9200/tjce?pretty"
# curl -X PUT "localhost:9200/tst?pretty"
# curl -X PUT "localhost:9200/_all/_mappings?pretty" -H 'Content-Type: application/json' -d'
# {
#     "dynamic_date_formats": ["dd/MM/yyyy"]
# }
# '

# export PYTHONPATH=/home/rafa/Documents/projects/juslite:/home/rafa/Documents/projects/juslite/teste_scrapy/tstSpider/tstSpider
