# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyuniversal.get_config import get_config
from scrapyuniversal.configs.rules import rules


class UniversalSpider(CrawlSpider):
    name = 'universal'
    allowed_domains = ['universal']
    start_urls = ['http://universal/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def __init__(self, name, *args, **kwargs):
        config = get_config(name)
        self.config = config
        self.rules = rules.get(config.get("rules"))
        self.start_urls = config.get("start_urls")
        self.allowed_domains = config.get("allowed_domains")
        super(UniversalSpider,self).__init__(*args, **kwargs)

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
