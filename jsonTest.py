# -*- coding: utf-8 -*-
import json
class test(object):
    arg1 = '123'
    arg2 = 'test'
    def test(self):
        print(self.arg1)
def Test2Json(obj):
    return {'arg1': obj.arg1,'arg2': obj.arg2}
f = open('./json.txt','a')
json.dump(Test2Json(test),f)
print(json.dumps(Test2Json(test)))