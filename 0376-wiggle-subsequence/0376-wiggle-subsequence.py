class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        @cache
        def solve(i,prev,fl):
            if i==n:
                return 0
            take,take2,skip=0,0,0
            if nums[i]>prev and fl:
                take=1+solve(i+1,nums[i],0)
            if nums[i]<prev and not fl:
                take2=1+solve(i+1,nums[i],1)
            skip=solve(i+1,prev,fl)
            return max(take,take2,skip)
        return max(solve(0,1000,0),solve(0,-1,1))