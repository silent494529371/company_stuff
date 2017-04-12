#! /usr/bin/python3
# coding=utf-8
import urllib.request
def get_price(code):
       url = 'http://hq.sinajs.cn/?list=%s' % code
       req = urllib.request.Request(url)
       #req.set_proxy(‘proxy.XXX.com:911′, ‘http’)
       content = urllib.request.urlopen(req).read()
       str = content.decode('gbk')
       data = str.split('"')[1].split(',')
       name = "%-6s" % data[0]
       price_current = "%-6s" % float(data[3])
       change_percent = (float(data[3]) - float(data[2]) )*100 / float(data[2])
       change_percent = "%-6s" % round (change_percent, 2)
       #print("code:{0} name:{1 }rising:{2} new:{2}".format(name, change_percent, price_current) )
       print("name {0} rise:{1} new:{2}".format(name, change_percent, price_current) )
       print ('start download...')
 #print("name {0} ring:{1} new:{2} code:{3} ".format(code, change_percent, price_current,code) )
def get_all_price(code_list):
   for code in code_list:
       get_price(code)
code_list = ['sh000001','sz399006','sz399005','sz399001','sh600066',
        'sz000028', 'sz000798', 'sz002500'	, 'sh603988','sz000571', 'sh600135', 
             ]


get_all_price(code_list)

