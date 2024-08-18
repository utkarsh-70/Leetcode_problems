class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        tbl = [-1] * (len(nums) + 1)
        def calc(i):
            if tbl[i] != -1:
                return tbl[i]
            if i == len(nums):
                return 0
            if i == len(nums) - 1:
                return nums[i]
            x = nums[i] + calc(i+2)
            y = calc(i+1)
            tbl[i] = max(x,y)
            return tbl[i]
        return calc(0)