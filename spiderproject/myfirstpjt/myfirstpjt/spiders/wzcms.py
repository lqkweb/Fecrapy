# -*- coding: utf-8 -*-
import scrapy
from ..items import MyfirstpjtItem


class WzcmsSpider(scrapy.Spider):
    name = 'wzcms'
    allowed_domains = ['wzzbtb.com']
    start_urls = ['http://ggzy.wzzbtb.com:6081/wzcms/zfcgcggg/30516.htm']

    def parse(self, response):
        item = MyfirstpjtItem()
        item["title"] = response.xpath("//div[@class='Content-Main FloatL']/span[@class='Bold']")
        item["url"] = response.url
        pass
