# -*- coding:utf-8 -*- 
'''
Created on 2016-3-10

@author: Administrator
'''
import tushare as ts
import os
import sys

class mydata:
    pass

#stocklist="../dataset/all_stocks.csv"
#stocklist_path = os.path.abspath(os.path.join(sys.argv[0], os.path.pardir,stocklist))
#
#allstocks=ts.get_stock_basics()
#allstocks.to_csv(stocklist_path)
print ts.get_index()
szzs = ts.get_h_data('000001', index=True) #上证历史数据
print szzs
#cyb = ts.get_h_data('399006', index=True) #创业板历史数据