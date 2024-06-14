class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        nums.sort()
        totc=0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                inc=nums[i-1]-nums[i]+1
                nums[i]+=inc
                totc+=inc
                
        return totc