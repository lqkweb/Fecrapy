#!/usr/bin/env python  
# encoding: utf-8  

""" 
@author: lqk  
@contact: 798244092@qq.com 
@site: https://github.com/lqkweb 
@file: main.py 
@time: 2019/3/11 9:31 AM 
"""

from scrapy.cmdline import execute


import sys
import os

# 启动爬虫
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(['scrapy', 'crawlall'])
execute(['scrapy', 'crawl', "args", "-a", "myurl=http://www.lqkweb.com"])