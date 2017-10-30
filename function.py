from _functools import reduce
def fuck_motta(i):
    return "fuckyoumotta",i
print(list(map(fuck_motta,[1,2,3,3])))
def plus(x,y):
    return x*10+y
print(reduce(plus,[1,2,3,4,5]))
def upToCase(word):
    res = ''
    ch = chr(ord(word[0])-32)
    print(ch)
    res = ch + word[1:]
    return res

print(list(map(upToCase,['test','china','motta'])))
print("fuck you %s %d times" % ("motta",10000))

def fli(x):
    return x%2 == 0
print(list(filter(fli,[1,2,3,4,5,6,7,8,9])))