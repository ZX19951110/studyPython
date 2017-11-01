print(sorted([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)],key=lambda x : x[1]))#lambda为一个匿名函数
def lazy_sum(*l): # 闭包 闭包不要返回使用循环变量
    def sum():
        res = 0
        for i in l:
           res += i
        return res
    return sum
f = lazy_sum(1,2,3,4,5)
print(f())