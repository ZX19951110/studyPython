# -*- coding:utf-8 *-
import requests
from bs4 import BeautifulSoup
import urllib.request
data = urllib.request.urlopen('https://www.zhihu.com')
print(print(data.read().decode('utf-8')))