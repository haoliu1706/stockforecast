# -*- coding:utf-8 -*- 
'''
Created on 2016年3月11日

@author: xuhshen
'''
import sys
import os
# import urllib2   #workround for proxy as the api do not support proxy configure
# proxy_handler = urllib2.ProxyHandler({"http" : 'http://10.144.1.10:8080'})
# opener = urllib2.build_opener(proxy_handler)
# urllib2.install_opener(opener)
# lines = opener.open("http://api.finance.ifeng.com/akdaily/?code=sz000875&type=last").read()

stocklist="../dataset/all_stocks.csv"

dataset_path = os.path.abspath(os.path.join(sys.argv[0], os.path.pardir,"../dataset"))
stocklist_path = os.path.join(dataset_path, "all_stocks.csv")


