#!/usr/bin/python
# -*- coding: UTF-8 -*-
import scrapy


class AuthorSpider(scrapy.Spider):
    name = "author"

    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        for href in response.css(".author + a::attr(href)"):
            yield response.follow(href, self.parse_author)
        for href in response.css("li.next a::attr(href)"):
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        yield {
            "name": response.css("h3.author-title::text").extract_first(),
            "birthdate": response.css("span.author-born-date::text").extract_first(),
        }
