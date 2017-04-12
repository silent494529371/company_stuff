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

       #price_current = ("%-6s" % float(data[8]))
       #change_percent = (float(data[3]) - float(data[2]) )*100 / float(data[2])
       #change_percent = "%-6s" % round (change_percent, 2)
       #print("code:{0} name:{1 }rising:{2} new:{2}".format(name, change_percent, price_current) )
       print("name %s new: %f" %(name, float(data[8])) )
 #print("name {0} ring:{1} new:{2} code:{3} ".format(code, change_percent, price_current,code) )
def get_all_price(code_list):
   for code in code_list:
       get_price(code)
code_list = ['I1709','SM1705','CU1705','C1709','ZC1705','JM1705'
             ]


get_all_price(code_list)

''
