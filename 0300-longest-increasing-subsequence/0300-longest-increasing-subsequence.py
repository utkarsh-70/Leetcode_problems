class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        di={}
        def topd(i,prev,taken):
            if (i,taken) in di:

                return di[(i,taken)]
            if i==len(nums):
                return 0
            take,skip=0,0
            if prev<nums[i]:
                take=1+topd(i+1,nums[i],True)
            skip=topd(i+1,prev,False)
            if taken:
                di[(i,taken)]=max(take,skip)
                return di[(i,taken)]
            return max(take,skip)
        return topd(0,-10001,False)

