# -*- coding:utf-8 -*- 
'''
Created on 2016年3月11日

@author: xuhshen
'''
from setting import *
import csv
import time
import tushare as ts

def get_stock_list(value="code"):
    with open(stocklist_path) as f:
        f_csv = csv.DictReader(f)
        return [i[value] for i in f_csv]

def get_stock_history(code="000875"):
    '''input: stock code number
       output: [{volume:,v_ma10:,v_ma20:,ma5:,price_change:,v_ma5:,p_change:,high:,ma20:,low:,date:,close:,open:,ma10:,turnover:,},.....]
        date：日期     
        open：开盘价
        high：最高价
        close：收盘价
        low：最低价
        volume：成交量
        price_change：价格变动
        p_change：涨跌幅
        ma5：5日均价
        ma10：10日均价
        ma20:20日均价
        v_ma5:5日均量
        v_ma10:10日均量
        v_ma20:20日均量
        turnover:换手率[注：指数无此项]
    '''
    stock_path = os.path.join(dataset_path, code+".csv")
    with open(stock_path) as f:
        f_csv = csv.DictReader(f)
        return [i for i in f_csv]

def get_session_feature(lst=[]):
    ''' input: a list of a session
        output:[high/base,low/base,average_turnover]
    '''
    days = len(lst)
    high = 0
    low = 10000
    turnover = 0
    for i in lst:
        if high < float(i['high']):
            high = float(i['high'])
        if low > float(i['low']):
            low = float(i['low'])
        try:    
            turnover += float(i['turnover'])
        except:
            turnover += float(i['volume'])
    return [high,low,turnover/days]

def get_latest_feature(lst):
    return [[float(i['high']),float(i['low']),float(i['turnover'])] for i in lst]


testdata = get_stock_history()
base = get_stock_history()[0]["close"]
print get_session_feature(testdata)
for i in testdata[1:-1]:
    print i
    break

for i in get_stock_history():
    print i
    break


