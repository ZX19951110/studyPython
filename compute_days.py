# -*- coding:utf-8 -*-
import time
import sys
def compute_days():
    if len(sys.argv) == 1 :
        today = time.time()
    else:
        today = sys.argv[1]
        today = time.mktime(time.strptime(today + ' 00:00:00','%Y-%m-%d %H:%M:%S'))
    start_time = time.mktime(time.strptime('2017-09-24 00:00:00','%Y-%m-%d %H:%M:%S'))
    print('这一天是我们到意大利的第%d天'% int((today-start_time)/(3600*24)))
if __name__ == '__main__':
    compute_days()
