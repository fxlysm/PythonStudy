#coding:utf-8

# 爬虫百度图下
# 1.网页源代码
# 2. 找到你要爬取的对象
# 3.下载下来

# 模块:
# 1.urllib  python如何访问互联网，获取URL 抓取远程数据
#              python2 有两个模块urllib and urllib2而python 只有一个urllib
#         https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E7%BE%8E%E6%99%AF&step_word=&hs=0&pn=0&spn=0&di=37624009390&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=683740547%2C4141923065&os=893048754%2C2222175563&simid=4038021300%2C421432194&adpicid=0&lpn=0&ln=1988&fr=&fmq=1490753158024_R&fm=index&ic=0&s=undefined&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fimg.bzcm.net%2Fnews%2Fattachement%2Fjpg%2Fsite2%2F20141103%2F0003ffa94ec915c114ff11.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bkzv4_z%26e3BgjpAzdH3FgjofAzdH3Fda89-88AzdH3FanAzdH3Fv5gpjgp_8ma9mmc_z%26e3Bip4&gsm=0&rpstart=0&rpnum=0
# 2. bs4 解析
# 3.re

from  urllib.request import *
from  bs4 import BeautifulSoup
import re

url='http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1490754906843_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%BE%8E%E5%9B%BE'
html =urlopen(url)
print html

obj= BeautifulSoup(html,'html.parser')