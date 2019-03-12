#!/usr/bin/env python  
# encoding: utf-8  

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

rules = {
    "tbquan": (
    Rule(LinkExtractor(allow=r'.*?search.*?'),
         callback='parse_item', follow=True),
)
}