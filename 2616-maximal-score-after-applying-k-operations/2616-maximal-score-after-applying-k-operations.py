class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        out=0
        nums=[-1*x for x in nums]
        heapq.heapify(nums)
        while k:
            x=heapq.heappop(nums)
            out+=(-1*x)
            heapq.heappush(nums,x//3)
            k-=1
        return out
