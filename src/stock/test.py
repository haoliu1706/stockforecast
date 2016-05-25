# -*- coding:utf-8 -*- 
'''
Created on 2016年5月24日

@author: 04yyl
'''
import tushare as ts

if __name__ == '__main__':
    print ts.fund_holdings(2016, 1)
#     ts.set_token('14a9186596c5cd0a6e74b994434d620c5ddaab9611d686f6e201768e1aa957cb')
# #   获取secid    
#     mt = ts.Master()
#     secid = mt.SecID(assetClass="E",cnSpell="",ticker="300027")
# 
#     print secid
#     fd = ts.Subject()
#     df = fd.NewsByCompany(field='newsPublishTime,newsTitle,relatedScore,sentiment,newsPublishSite,newsInsertTime',partyID=35390,beginDate='20160524')
# #     df = df.sort('insertTime', ascending=False)
#     print df