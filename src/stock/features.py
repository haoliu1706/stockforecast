# -*- coding:utf-8 -*- 
'''
Created on 2016年3月19日

@author: xuhshen
'''
import localdata
import numpy as np
types = [-9.9,-9,-8,-7,-6,-5,-4,-3,-2,-1,-0.5,0,0.5,1,2,3,4,5,6,7,8,9,9.9]
spreadtypes = [1,2,3,4,5,6]
features = [0]*(len(types)+1)

stocklist = localdata.get_stock_list()

def get_price_spread_rate(code="000001"):
    data = localdata.get_stock_history(code)
    try:
        return [float(data[i]["close"])/float(data[i+1]["close"])-1 for i in xrange(len(data)-1)]
    except:
        print code
        return [float(data[i]["close"])/float(data[i+1]["close"])-1 for i in xrange(len(data)-2)]

def get_price_wave_rate(code="000001"):
    data = localdata.get_stock_history(code)
    try:
        return [(float(data[i]["high"])-float(data[i]["low"]))/float(data[i+1]["close"]) for i in xrange(len(data)-1)]
    except:
        print code
        return [(float(data[i]["high"])-float(data[i]["low"]))/float(data[i+1]["close"]) for i in xrange(len(data)-2)]
    


def get_price_distribution():
    rst = np.array([[0]]*(len(types)+1))
    for stock in stocklist:
        for i in get_price_spread_rate(stock):
            rst += np.array(localdata.get_type(i, types))
    print rst
    
def dividestocks():
    result = []
    for stock in stocklist:
        rst = 0.00
        lst = get_price_wave_rate(stock)
        num = len(lst)
        for i in xrange(num):
            rst += abs(lst[i])
        try:
            result.append(rst/num)
        except:
            print stock
    print result
    return result  

def show_stocks_by_spread(spreadtypes=spreadtypes):
    rst = np.array([[0]]*(len(spreadtypes)+1))
    data = dividestocks()
    for i in data:
        rst += np.array(localdata.get_type(i, spreadtypes))
    print rst  

def test1():
    a=[[  0],[ 11],[165],[900],[959],[355],[158],[ 73],[ 75],[ 47],[ 37],[ 38]]
    number = 0.000
    for i in a:
        number += i[0]
    for i in xrange(len(a)):
        if i==0:
            print "spread_session:           <= %10f  number: %10d      rate: %10f:   " % (spreadtypes[i],a[i][0],100*a[i][0]/number)
        elif i==len(a)-1:
            print "spread_session:            > %10f  number: %10d      rate: %10f:   " % (spreadtypes[i-1],a[i][0],100*a[i][0]/number)
        else:
            print "spread_session:%10f---%10f   number: %10d      rate: %10f:   " % (spreadtypes[i-1],spreadtypes[i],a[i][0],100*a[i][0]/number)
    
def test():
    a = [[ 43029],[ 11392],[  9715],[ 12230],[ 17385],[ 27301],[ 44625],[ 74105], [119769],[182661], [114198], [149218],[137732], [137673], [209656],[132471],[ 85905],[ 55258],[ 35631],[ 22973],[ 14958],[  9783],[  7403],[ 47909]]
    print "price rate distribution:"
    number = 0.000
    for i in a:
        number += i[0]
    print "total numbers:%d" % number    
    for i in xrange(len(a)):
        if i==0:
            print "session:           <= %10f  number: %10d      rate: %10f:   " % (types[i],a[i][0],100*a[i][0]/number)
        elif i==23:
            print "session:            > %10f  number: %10d      rate: %10f:   " % (types[i-1],a[i][0],100*a[i][0]/number)
        else:
            print "session:%10f---%10f   number: %10d      rate: %10f:   " % (types[i-1],types[i],a[i][0],100*a[i][0]/number)
        

if __name__ == '__main__':
#     get_price_distribution()
    show_stocks_by_spread()
#     test1()
    
    
    
    