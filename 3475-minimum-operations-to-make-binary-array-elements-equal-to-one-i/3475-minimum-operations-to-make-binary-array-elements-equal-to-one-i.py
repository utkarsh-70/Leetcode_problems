class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)-2):
            if nums[i]!=1:
                for x in range(i,i+3):
                    nums[x]^=1
                c+=1
        for i in nums:
            if i==0:
                return -1
        return c