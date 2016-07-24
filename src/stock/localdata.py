# -*- coding:utf-8 -*- 
'''
Created on 2016年3月11日

@author: xuhshen
'''
from setting import *
import csv
from datetime import datetime
import numpy as np
import network
import random
# import tushare as ts

resulttype = [-5,-4,-3,-2,-1,-0.5,0,0.5,1,2,3,4,5,]
input_type = [-0.8,-0.6,-0.4,-0.2,0,0.1,0.2,0.4,0.6,0.8,1,2,3]

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

def get_session_feature(lst,base):
    ''' input: a list of a session
        output:[high/base,low/base,average_turnover]
    '''
    close = float(base['close'])
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
            turnover += float(i['turnover'])/float(base['turnover'])
        except:
            turnover += float(i['volume'])/float(base['volume'])
    result = []
    for i in [high,low]:
        result.append([i/(5*close)])
    result.append([turnover/days])
    return result

def get_latest_feature(lst,close):
    close = float(close)
    keylst = ['high','low','open','close']
    result = []
    for i in keylst:
        result.append([float(lst[i])/(5*close)])
    try :
        result.append([float(lst['turnover'])/100]) 
    except:
        result.append([float(lst['volume'])/90000000000]) 
    return result

def get_type(x,types=[4]):
#     types = [-5,-4,-3,-2,-1,-0.5,0,0.5,1,2,3,4,5,]
    result = [[0]]*(len(types)+1)
    for i in xrange(len(types)):
        if x*100<=types[i]:
            result[i] = [1]
            return result
    result[-1] = [1]
    return result
        
def get_result(lst,close):
    result = []
#     output = ['high','low','open','close']
    output = ['close']
    for i in output:
        result.extend(get_type((float(lst[i])-float(close))/float(close)))
#         print (float(lst[i])-float(close))/float(close)
    return np.array(result)

def divide_stk_his_data(sz_lst,stock_lst):
    '''根据上证交易数据补全个股历史数据, 同时以上证交易日为基准，对股票里的非交易日数据进行剔除
    '''
    j=0
    new_lst=[]
    for i in xrange(len(sz_lst)):
        szday = str2time(sz_lst[i]['date'])
        stday = str2time(stock_lst[j]['date'])
        k = j
        if szday < stday:
            while szday < str2time(stock_lst[j]['date']):
                j += 1
        elif szday > stday:
            while szday > str2time(stock_lst[j]['date']):
                new_lst.append(stock_lst[k])
                j -= 1
            j += 1
            continue
        new_lst.append(stock_lst[j])
        j += 1
    return new_lst
        
def str2time(mystr):
    return datetime.strptime(mystr, "%Y-%m-%d")

def get_features(data,historys=0,latest_days=15,session_days=10,sessions=23):
    '''input data should be like [[],[]],the second list is the stock need to forecast
    '''
    data_set = []
    if historys:
        start = 2
        nums = historys-latest_days-session_days*sessions
    else:
        start = 0
        nums = 2
    for i in xrange(start,nums):
        feature = []
        for l in xrange(15):
            for dt in data:
                feature.extend(get_latest_feature(dt[i+l],dt[i+l+1]['close']))
        for session in xrange(sessions):
            start = i+latest_days+session*session_days
            end = i+latest_days+(session+1)*session_days
            for dt in data:
                feature.extend(get_session_feature(dt[start:end],dt[i]))
        result = get_result(data[1][i-1],data[1][i]['close'])
        data_set.append([np.array(feature),result])
    if nums==2:
        print 
        print result
    return data_set


if __name__ == '__main__':
    szzs = get_stock_history('szzs')
    stock = get_stock_history('000875')
    new_stockhistory = divide_stk_his_data(szzs,stock)
    
    data_set = get_features([szzs,new_stockhistory],historys = len(szzs))
    value_set = get_features([szzs,new_stockhistory])
    
    numlist = random.sample(xrange(len(data_set)), 300)
    training_data = [data_set[i] for i in numlist]
    testing_data = [data_set[i] for i in xrange(len(data_set)) if i not in numlist]
    for i in value_set:
        for j in i:
            print j 
            print len(j)
    net = network.Network([288, 30, 2])
    net.SGD(training_data, 10000, 2, 2.9, test_data=testing_data,value_data=value_set)

#     





