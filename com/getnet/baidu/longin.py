# -*- coding: utf-8 -*-
#---------------------------------------
#   程序：山东大学爬虫
#   版本：0.1
#   作者：why
#   日期：2013-07-12
#   语言：Python 2.7
#   操作：输入学号和密码
#   功能：输出成绩的加权平均值也就是绩点
#---------------------------------------
import urllib
import urllib2
import cookielib
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#需要POST的数据#
postdata=urllib.urlencode({
    'stuid':'201100300428',
    'pwd':'921030'
})
#自定义一个请求#
req = urllib2.Request(
    url = 'http://jwxt.sdu.edu.cn:7777/pls/wwwbks/bks_login2.login',
    data = postdata
)
#访问该链接#
result = opener.open(req)
#打印返回的内容#
print result.read()