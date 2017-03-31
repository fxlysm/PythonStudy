#coding:utf-8
from  urlparse import urljoin
from  bs4 import BeautifulSoup
import  html5lib
import csv
import requests


URL = 'http://bj.ganji.com/fang1/o%7Bpage%7Dp%7Bprice%7D/'
ADDR ='http://bj.ganji.com/'

start_page =1
eng_page =10
price =7


with open('user.csv','wb')as f:
    csv_writer =csv.writer(f,delimiter=',')
    print 'start'

    while start_page < eng_page:
        start_page += 1

        print  'get:{0}'.format(URL.format(page=start_page,price=price))

        response = requests.get(URL.format(page=start_page, price=price))
        html = BeautifulSoup(response.text, 'html.parser')
        house_list = html.select('.f-list > .f-list-item > .f-list-item-wrap')

        if not house_list:
            break
        for house in house_list:
            house_title = house.select('.title > a')[0].string.encode('utf-8')
            house_addr = house.select('.area > a')[-1].string.encode('utf-8')
            house_price = house.select('.num')[0].string.encode('utf-8')
            house_url = urljoin(ADDR, house.select('.title > a')[0]['href'])
            csv_writer.writerow([house_title, house_addr, house_price, house_url])

    print  'end'








