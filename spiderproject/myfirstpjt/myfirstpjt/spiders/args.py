# -*- coding: utf-8 -*-
import scrapy


class ArgsSpider(scrapy.Spider):
    name = 'args'
    allowed_domains = ['tbquan.cn']
    start_urls = ['http://tbquan.cn/']

    def __init__(self, myurl=None, *args, **kwargs):
        super(ArgsSpider, self).__init__(*args, **kwargs)
        self.start_urls = ["%s"%myurl]

    def parse(self, response):
        pass
