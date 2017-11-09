# -*- coding: utf-8 -*-
from multiprocessing import Process,Pool
import os,time,random,threading
res = 0
lock = threading.Lock()
def run(id=0):
    start = time.time()
    time.sleep(random.random())
    end = time.time()
    #print(id,'process %s is running... in %s' % (os.getpid(),start - end))
    print("%s is running %0.2f" % (threading.current_thread().name,end - start))
def change(n):
    global res
    res = res + n
    res = res - n
    print(res)
    while True:
        pass
def testLock():
    for i in range(1000000):
        change(i)
if __name__ == '__main__':
    # print("my pid is %s"  % (os.getpid()))
    # pool = Pool(10)
    # for i in range(11):
    #     pool.apply_async(run,args=(i,))
    # pool.close()
    # pool.join()
    # t = threading.Thread(target=run,name='my thread')
    # t.start()
    t1 = threading.Thread(target=testLock)
    t2 = threading.Thread(target=testLock)
    t1.start()
    t2.start()
    t1.join()
    t2.join()