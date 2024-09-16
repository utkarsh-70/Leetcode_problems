class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @cache
        def topd(i,st,end):
            if i>=len(multipliers) or st>=len(nums) or end<0:
                return 0
            start=nums[st]*multipliers[i]+topd(i+1,st+1,end)
            end1=nums[end]*multipliers[i]+topd(i+1,st,end-1)
            return max(start,end1)
        return topd(0,0,len(nums)-1)