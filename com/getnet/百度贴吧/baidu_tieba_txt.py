# _*_ coding:utf-8 _*_

import  urllib2,re

class BDTB:

    baseUrl='http://tieba.baidu.com/p/4945553679?see_lz=1'

    #打开网页，获取源码
    def getPage(self): #  有self参数，必须要位于第一位
        try:
            url =self.baseUrl
            request =urllib2.Request(url) #用地址创建一个对象

            response = urllib2.urlopen(request)
            a=response.read()
            #  打印源码
            # print  a
            return a
        except Exception ,e:
            print e

    #匹配标题
    # 正则表达式

    def Title(self):
        html=self.getPage()
        reg =re.compile(r'<h3 class="core_title_txt pull-left text-overflow  " title="(.*?)" style=')  #编译

        items =re.findall(reg,html) #findall(正则表达式，源码）
        # print items[0]

        # 索引 取中文 items[0]
        # for in

        # for items in items:
        #     return items

        # 写入text1.txt 文件中
        for item in items:
            f = open('text1.txt','w')  #自动新建，写的方式打开
            f.write('标题'+'\t'+item)
            f.close()

        return  items

    #匹配正文

    def Text(self):
        html=self.getPage()
        reg =re.compile(r'class="d_post_content j_d_post_content ">            (.*?)</div><br>',re.S)  #编译
        #  re.S  匹配换行符

        items_text =re.findall(reg,html) #findall(正则表达式，源码）
        # print items_text[0]

        # 索引 取中文 items[0]
        # for in

        for i in items_text:
            q = re.compile('<a.*?>|</a>')  # 需要过滤的标签
            t = re.compile('<img.*?>')
            y = re.compile('http.*?.html')

            i = re.sub(q,"",i)
            i = re.sub(t, "", i)
            i = re.sub(y, "", i)
            i = i.replace('<br>','')   #直接将<br>标签 用替换为空
            print i
            # 写入text1.txt 文件中
            f = open('text1.txt','a')
            f.write('\n\n'+i)
            f.close()


        # for item in items:
        #     f = open('text1.txt','w')  #自动新建，写的方式打开
        #     f.write('正文'+'\t'+item)
        #     f.close()

        return  items_text


bdtb =BDTB() #实例化这个类
bdtb.getPage()
bdtb.Title()
bdtb.Text()


#解决禁止爬虫 ：加上头部信息，