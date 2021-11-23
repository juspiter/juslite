from storage import Storage
from basecrawler import BaseCrawler


# export ES_JAVA_OPTS="-Xms512m -Xmx512m"
# docker run -d --name juslitedb -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" --memory="1g" elasticsearch:7.14.2
storage = Storage('172.17.0.2:9200')



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

# crawl = BaseCrawler("0218226-29.2020.8.06.0001")
# print(crawl.crawl_lawsuit())
