l = [1,2,3,5,6,7,8,9]
print(l[::2])
print([x*x*x for x in range(1,30)])
print ([x for x in ['apple','hello','test','world'] if len(x) ==5])
g = (x for x in range(1,100) if x%2 == 0)
for i in g:
    print(i)
def odd():
    print("test1")
    yield
    print("test2")
    yield
o = odd()
next(o)
next(o)