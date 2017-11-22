# -*- coding:utf-8 *-
import requests
import json
class request_test:
    def __init__(self):
        self.__url = 'http://httpbin.org'
        self.getData = {'name':'zhanxu'}
    def get(self):
        self.response = requests.get(self.__url+'/get', params=self.getData)
    def print_response(self):
        print(type(self.response))
        print(self.response.status_code)
        print(type(self.response.text))
        print(self.response.cookies)
        #print(response.content)(需要转码)
        print(self.response.content.decode("utf-8"))
    def decode_response(self):
        print(json.loads(self.response.text))
    def upload_file(self):
        file = {"files":open("./json.txt",'rb')}
        self.response = requests.post(self.__url+'/post',files=file)
    def cookie(self):
        s = requests.Session()
        cookiesValue = {'ID':'123','name':'zhanxu'}
        s.get(self.__url+'/cookies/set',params=cookiesValue)
        response = s.get(self.__url+'/cookies')
        print(response.text)
        for key, value in response.cookies.items():
            print(key + "=" + value)
    def https_test(self):
        self.response = requests.get("https://google.com")
        print(self.response.text)
if __name__ == '__main__':
    req = request_test()
    req.https_test()