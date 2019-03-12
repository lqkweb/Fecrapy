#!/usr/bin/env python  
# encoding: utf-8  

""" 
@author: lqk  
@contact: 798244092@qq.com 
@site: https://github.com/lqkweb 
@file: urls.py 
@time: 2019/3/12 4:24 PM 
"""

def tbquan(start, end):
    for page in range(start, end+1):
        yield "http://www.tbquan.cn/search?q=%E5%85%85%E7%94%B5%E7%BA%BF&p=" + str(page)