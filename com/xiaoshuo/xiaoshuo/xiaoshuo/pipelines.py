# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
from scrapy.exceptions import DropItem
from com.util.mysqlutil import mysqlutil as msql
from com.util.sendemailutil import sendemail


class XiaoshuoPipeline(object):
    logger = logging.getLogger()

    def process_item(self, item, spider):
        # self.logger.info(item)
        # sendemail().send(title, '自己', '自己', content)
        # mysql.updataAddress(bean['id'], needAdress)
        sendemail().send(item['title'], '自己', '自己', item['content'])
        mysqlutil = msql()
        mysqlutil.updataAddress(item['id'], item['newAddress'])
        return item

    def open_spider(self, spider):
        # self.logger.info("XiaoshuoPipeline___open_spider")
        mysqlutil = msql()
        spider.data = mysqlutil.getUrlBean()

        # spider.start_urls = ['http://pythonscraping.com/pages/cookies/login.html']
        # self.client = pymongo.MongoClient(self.mongo_uri)
        # self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        pass
# self.logger.info("XiaoshuoPipeline___close_spider")
# self.client.close()
