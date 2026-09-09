class Solution(object):
    def singleNumber(self, nums):
       non_repeated=0
       for i in nums:
         non_repeated^=i
       return non_repeated
cherry=Solution()
nums=[1,2,2,1,3]
x=cherry.singleNumber(nums)     
print(x)    



        