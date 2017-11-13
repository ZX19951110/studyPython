# -*- coding:utf-8 -*-
import time
def compute_days(today = time.time()):
    start_time = time.mktime(time.strptime('2017-09-24 00:00:00','%Y-%m-%d %H:%M:%S'))
    print('今天是我们到意大利的第%d天'% int((today-start_time)/(3600*24)))
if __name__ == '__main__':
    compute_days()