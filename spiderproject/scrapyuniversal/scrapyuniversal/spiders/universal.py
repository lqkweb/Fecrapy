# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyuniversal.get_config import get_config
from scrapyuniversal.urls import tbquan
from scrapyuniversal.configs.rules import rules
from ..items import NewsItem, ChinaLoader


class UniversalSpider(CrawlSpider):
    name = 'tbquan'
    # allowed_domains = ['universal']
    # start_urls = ['http://universal/']
    #
    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    def __init__(self, name="tbquan", *args, **kwargs):
        config = get_config(name)
        self.config = config
        self.name = config.get("spider")
        self.rules = rules.get(config.get("rules"))

        start_urls = config.get("start_urls")
        if start_urls:
            if start_urls.get("type") == "static":
                self.start_urls = start_urls.get("value")
            elif start_urls.get("type") == "dynamic":
                self.start_urls = list(eval(start_urls.get("method"))(*start_urls.get("args", [])))
        self.allowed_domains = config.get("allowed_domains")
        super(UniversalSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        item = self.config.get("item")
        if item:
            cls = eval(item.get("class"))
            loader = eval(item.get("loader"))(cls, response=response)
            for key, value in item.get("attrs").items():
                for extractor in value:
                    if extractor.get("method")=="xpath":
                        loader.add_xpath(key, *extractor.get("args"), **{"re": extractor.get("re")})
                    if extractor.get("method") == "css":
                        loader.add_css(key, *extractor.get("args"), **{"re": extractor.get("re")})
                    if extractor.get("method")=="attr":
                        loader.add_value(key, getattr(response,  *extractor.get("args")))
                    if extractor.get("method")=="value":
                        loader.add_xpath(key, *extractor.get("args"), **{"re": extractor.get("re")})
            yield loader.load_item()
