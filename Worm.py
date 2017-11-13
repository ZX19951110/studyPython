# -*- coding:utf-8 *-
import requests
from bs4 import BeautifulSoup
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a hrief="http://example.com/elsie" class="sster" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
res = requests.get('http://google.it')
soup = BeautifulSoup(html)
for a in soup.a:
    print(a)
#print(res.encoding,res.status_code,res.cookies)

# def test(str):
#     length = len(str)
#     output = ''
#     if str[0] == '-':
#         output += '-'
#         while (length > 1):
#             output += (str[length-1])
#             length -= 1
#         print(output)
#     else:
#         while (length > 0):
#             output += (str[length - 1])
#             length -= 1
#         print(output)
#  test('123456789123')
# test('-210')