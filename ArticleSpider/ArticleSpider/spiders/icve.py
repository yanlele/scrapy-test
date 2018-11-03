# -*- coding: utf-8 -*-
import scrapy


class IcveSpider(scrapy.Spider):
    name = 'icve'
    allowed_domains = ['icve.com.cn']
    start_urls = ['http://www.icve.com.cn/']

    def parse(self, response):
        pass
