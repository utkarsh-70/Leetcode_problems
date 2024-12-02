class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        while i<len(nums):
            if nums[i]<=0:
                i+=1
            else:
                break
        if i==len(nums):
            return 1
        x=1
        for j in range(i,len(nums)):
            if j>0 and nums[j]==nums[j-1]:
                continue
            if nums[j]!=x:
                return x       
            x+=1
        return nums[-1]+1