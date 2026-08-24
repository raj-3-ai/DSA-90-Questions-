class Solution():
    def removeDuplicates(self,nums):
        slow=0
        for i in range (1,len(nums)):
            if nums[i]!=nums[slow]:
                slow+=1
                nums[slow]=nums[i]
        return slow+1 
solution=Solution()       
x=solution.removeDuplicates([1,1,2])
print(x)