# -*- coding: utf-8 -*-
from multiprocessing import Process,Pool
import os,time,random
def run(id):
    start = time.time()
    time.sleep(3)
    end = time.time()
    print(id,'process %s is running... in %s' % (os.getpid(),start - end))

if __name__ == '__main__':
    print("my pid is %s"  % (os.getpid()))
    pool = Pool(10)
    for i in range(11):
        pool.apply_async(run,args=(i,))
    pool.close()
    pool.join()