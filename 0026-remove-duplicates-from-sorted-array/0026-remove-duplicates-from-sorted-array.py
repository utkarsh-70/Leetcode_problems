class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,1
        fl=0
        while j<len(nums):
            if nums[i]==nums[j]:
                nums.pop(j)
            else:
                j+=1
                i+=1
        return len(nums)