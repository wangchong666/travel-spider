# -*- coding: utf-8 -*-
import scrapy


class MeravigliapaperSpider(scrapy.Spider):
    name = 'meravigliapaper'
    allowed_domains = ['http://meravigliapaper.com/en/page/2/']
    start_urls = ['http://http://meravigliapaper.com/en/page/2//']

    def parse(self, response):
        pass
