# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    title = scrapy.Field()
    movieInfo = scrapy.Field()
    url = scrapy.Field()
    score = scrapy.Field()
    time = scrapy.Field()
