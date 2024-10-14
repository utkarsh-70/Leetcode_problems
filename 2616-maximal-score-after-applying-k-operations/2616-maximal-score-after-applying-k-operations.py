class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums=[-x for x in nums]
        heapq.heapify(nums)
        score=0
        while k:
            x=-1*heapq.heappop(nums)
            score+=x
            heapq.heappush(nums,-1*ceil(x/3))
            k-=1
        return score