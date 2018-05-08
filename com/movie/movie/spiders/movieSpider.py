#!/usr/bin/python
# -*- coding: UTF-8 -*-
import scrapy

from com.movie.movie.items import MovieItem


class movieSpider(scrapy.Spider):
    name = 'movie'
    start_urls = [r"https://movie.douban.com/top250", ]

    def parse(self, response):
        item = MovieItem()
