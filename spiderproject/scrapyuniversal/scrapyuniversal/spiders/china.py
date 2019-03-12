# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import NewsItem, ChinaLoader


class ChinaSpider(CrawlSpider):
    name = 'china'
    allowed_domains = ['tech.china.com']
    start_urls = ['http://tech.china.com/articles/']

    rules = (
        Rule(LinkExtractor(allow=r'article\/.*\.html', restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(.,"下一页")]'))
    )

    def parse_item(self, response):
        loader = ChinaLoader(item=NewsItem(), response=response)
        # item["title"] = response.xpath('//h1[@id="chan_newsTitle"]/text()').extract_first()
        # item["url"] = response.url
        # item["website"] = "中华网"
        loader.add_xpath("title", '//h1[@id="chan_newsTitle"]/text()')
        loader.add_value("url", response.url)
        loader.add_value("website", "中华网")
        return loader.load_item()
