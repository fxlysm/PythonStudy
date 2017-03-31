#coding:utf-8
from  bs4 import BeautifulSoup
import html5lib
import requests

URL = 'http://bj.ganji.com/fang1'
ADDR = 'http://bj.ganji.com/'

start_page=1
end_page=10
price=7
while start_page <end_page:
    start_page+=1
    print  'get:{0}'.format(URL.format(page=start_page, price=price))

    response = requests.get(URL.format(page=start_page, price=price))
    html = BeautifulSoup(response.text, 'html.parser')

    house_list = html.select('.f-list > .f-list-item > .f-list-item-wrap')
