# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from storage import Storage
from itemadapter import ItemAdapter


class StoragePipeline:
    def open_spider(self, spider):
        self.storage = Storage('juslite_elastic:9200')

    def process_item(self, item, spider):
        self.storage.add_lawsuit(ItemAdapter(item))
        return item
