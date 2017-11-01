# 装饰器
def decorator(fun):
    def log(*l):
        print("%s is running" % fun.__name__)
        return fun(*l)
    return log

@decorator
def sum(*l,name=123):
    res = 0
    for i in l:
        res += i
    print(res+name)
sum(1,2,3,4)

def test(): #闭包测试
    def prt():
        print("hahahaha")
        return
    return prt
test()#得不到返回
a = test() #得到test()返回，即是prt函数 a是prt可以这么认为
a() #闭包 得到返回即执行prt