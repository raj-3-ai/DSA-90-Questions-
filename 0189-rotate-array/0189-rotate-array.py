class Solution():
    def rotate(self, nums, k):
      k=k%len(nums)
      nums[:]=nums[-k:]+nums[:-k]
      return nums[:]
cherry=Solution()
nums=[1,2,3,4,5,6,7]
x=cherry.rotate(nums,3)
print(x)        