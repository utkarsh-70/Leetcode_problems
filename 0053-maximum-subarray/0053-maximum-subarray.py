class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tots=0
        maxs=-999999
        for i in range(len(nums)):
            tots+=nums[i]
            if tots>=nums[i]:
                nums[i]=tots
            else:
                tots=nums[i]
            maxs=max(maxs,nums[i])
        return maxs