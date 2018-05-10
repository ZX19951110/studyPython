# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests

class spider_test(object):
    def __init__(self):
        self.url = 'http://www.hshfy.sh.cn/shfy/gweb/ktgg_search_content.jsp'
    def main(self):
        headers = {
            'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        res_list = []
        for i in range(1,3):
            query = {'pagesnum':i}
            req = requests.post(self.url,data=query,headers=headers)
            html = req.text
            bs = BeautifulSoup(html,'lxml')
            tr_list = bs.find('tbody')
            for tr in tr_list.children:















                i = 0
                for td in tr:
                    if i == 15:
                        res_list.append(td.text)
                    i += 1
        print(res_list[1:])
if __name__ == '__main__':
    spider_test().main()