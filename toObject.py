# -*- coding: utf-8 -*-
import sys
class test(object):
    sys = sys
    def __init__(self,name):
        print(__name__)
        print(sys.__name__)
        self.name = name
    def prt(self):
        print(sys.argv[1])
    def setName(self,name):
        self.__name = name
    @property
    def getName(self):
        print(self.__name)
test = test('zhanxu')
test.setName('motta')
print(test.name)
test.getName