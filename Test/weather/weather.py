# -*- coding: utf-8 -*-
from urllib.request import urlopen, Request
import urllib
import bs4

location = '서울'
enc_location = urllib.parse.quote(location + '+날씨')

url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location

req = Request(url)
page = urlopen(req)
html = page.read()
soup = bs4.BeautifulSoup(html,'html5lib')
print('현재 ' + location + ' 날씨는 ' + soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text + '도 입니다.')
print(url)