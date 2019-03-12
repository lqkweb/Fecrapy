# -*- coding: utf-8 -*-
import scrapy


class TbquanSpider(scrapy.Spider):
    name = 'tbquan'
    allowed_domains = ['tbquan.cn']
    start_urls = ['http://tbquan.cn/']

    def parse(self, response):
        pass
