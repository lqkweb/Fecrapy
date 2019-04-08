# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join,Compose


class NewsItem(Item):
    title = Field()
    url = Field()
    website = Field()


class NewsLoader(ItemLoader):
    default_input_processor = TakeFirst()


class ChinaLoader(NewsLoader):
    url_out = Compose(Join,lambda s:s)

