# -*- coding:utf-8 -*- 
'''
Created on 2016-3-10

@author: Administrator
'''
import tushare as ts
from setting import *
from localdata import get_stock_list
import threading

def store_index():
    index_path = os.path.join(dataset_path, "all_stock.csv")
    allstocks=ts.get_stock_basics()
    allstocks.to_csv(index_path)

def store_stock_history(code='000875'):
    stock_path = os.path.join(dataset_path, code+".csv")
    df = ts.get_hist_data(code)
    df.to_csv(stock_path)
    
def store_zhishu_history(code='000001'):
    stock_path = os.path.join(dataset_path, "szzs.csv")
    df = ts.get_h_data(code, start='2013-03-13', end='2016-03-13',index=True)
    df.to_csv(os.path.join(dataset_path, stock_path))


def thread_store_all_stock():
    for i in get_stock_list():
        while  len(threading.enumerate())>=80:
            print len(threading.enumerate())
            print i
        t = threading.Thread(target=store_stock_history,args=(i,))
        t.setDaemon(True)
        t.start()
    t.join()

if __name__ == '__main__':
    thread_store_all_stock()

         
# store_zhishu_history()
# store_stock_history()
# print ts.get_index()
