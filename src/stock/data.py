'''
Created on 2016-3-10

@author: Administrator
'''
import tushare as ts
import os
import sys

class mydata:
    pass

stocklist="../dataset/all_stocks.csv"

stocklist_path = os.path.abspath(os.path.join(sys.argv[0], os.path.pardir,stocklist))
allstocks=ts.get_stock_basics()
allstocks.to_csv(stocklist_path)

