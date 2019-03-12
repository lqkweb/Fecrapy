#!/usr/bin/env python  
# encoding: utf-8  

""" 
@author: lqk  
@contact: 798244092@qq.com 
@site: https://github.com/lqkweb 
@file: get_config.py 
@time: 2019/3/12 9:38 AM 
"""

from os.path import realpath, dirname
import json

def get_config(name):
    path = dirname(realpath(__file__))+"/configs/" + name + ".json"
    with open(path, "r", encoding="utf-8") as f:
        return json.loads(f.read())