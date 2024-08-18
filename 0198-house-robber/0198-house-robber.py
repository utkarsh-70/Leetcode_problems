class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        tbl = [-1] * (len(nums) + 1)
        tbl[-1] = 0
        tbl[-2] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            tbl[i] = max(nums[i] + tbl[i+2], tbl[i+1])
        return max(tbl[0], tbl[1])