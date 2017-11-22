# -*- coding:utf-8 -*-
class Two_Sum(object):
    def main(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(target == nums[i]+nums[j]):
                    return i,j

obj = Two_Sum()
print(obj.main([1,2,3,4,5,6,7,8,9,6,5,4,4,2,3,6,6,6,6,6,99,8,5,5,22,3,9,99,9,6,6],556))