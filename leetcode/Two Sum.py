# -*- coding:utf-8 -*-
class Two_Sum(object):
    def main(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(target == nums[i]+nums[j]):
                    return i,j

obj = Two_Sum()
print(obj.main([1,2,35,55,5,6],7))