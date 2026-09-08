class Solution(object):
    def containsDuplicate(self, nums):
      seen=set()
      for i in nums:
        if i in seen:
            return True
        seen.add(i)
      return False 
cherry=Solution()
x=cherry.containsDuplicate([1,2,3,1])
print(x)