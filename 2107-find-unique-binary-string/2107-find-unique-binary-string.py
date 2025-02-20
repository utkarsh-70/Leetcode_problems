class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        def backtrack(curr):
            if len(curr)==n:
                if curr not in nums:
                    return curr
                return ''
            take,skip='',''
            take=backtrack(curr+'0')
            if take:
                return take
            skip=backtrack(curr+'1')
            if skip:
                return skip
        return backtrack('')