class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        out=[]
        while nums:
            out.append(heapq.heappop(nums))
        return out