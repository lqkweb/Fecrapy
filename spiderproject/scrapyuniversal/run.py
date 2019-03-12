#!/usr/bin/env python  
# encoding: utf-8  

""" 
@author: lqk  
@contact: 798244092@qq.com 
@site: https://github.com/lqkweb 
@file: run.py 
@time: 2019/3/12 9:42 AM 
"""

import sys
from scrapy.utils.project import get_project_settings
from scrapyuniversal.get_config import get_config
from scrapy.crawler import CrawlerProcess

def run():
    name = sys.argv[1]
    custom_settings = get_config(name)
    spider = custom_settings.get("spider")
    project_settings = get_project_settings()
    settings = dict(project_settings.copy())
    settings.update(custom_settings.get("settings"))
    process = CrawlerProcess(settings)
    process.crawl(spider, **{"name":name})
    process.start()


if __name__ == '__main__':
    run()