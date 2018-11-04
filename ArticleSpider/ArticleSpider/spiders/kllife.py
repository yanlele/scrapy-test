# -*- coding: utf-8 -*-
import scrapy


class MafengwoSpider(scrapy.Spider):
    name = 'kllife'
    allowed_domains = ['kllife.com']
    start_urls = ['http://kllife.com/']

    def parse(self, response):

        re_select = response.xpath('/html/body/header/div[1]/div/div[1]/a[1]/text()').extract()[0]

        print(re_select)

        pass
