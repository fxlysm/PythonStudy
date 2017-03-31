#coding:utf-8
from  urlparse import urljoin
from  bs4 import BeautifulSoup
import  html5lib
import csv
import requests



URL = 'http://www.qiushibaike.com/hot/page/%7Bpage%7Dp'
ADDR ='http://bj.ganji.com/'


start_page =1
eng_page =10
price =7


with open('user.csv','wb')as f:
    csv_writer =csv.writer(f,delimiter=',')
    print 'start'

    while start_page < eng_page:
        start_page += 1

        print  'get:{0}'.format(URL.format(page=start_page))

        response = requests.get(URL.format(page=start_page))
        html = BeautifulSoup(response.text, 'html.parser')
        joke_list = html.select('.article block untagged mb15 > .content ')



        if not joke_list:
            break
        for joke in joke_list:
            joke_title = joke.select('.content > a')[0].string.encode('utf-8')
            print  joke_title

            csv_writer.writerow([joke_title])

    print  'end'