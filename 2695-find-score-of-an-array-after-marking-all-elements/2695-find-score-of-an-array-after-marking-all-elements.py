class Solution:
    def findScore(self, nums: List[int]) -> int:
        n=len(nums)
        num=[[nums[i],i] for i in range(n)]
        heapq.heapify(num)
        marked=[0]*n
        out=0
        while num:
            x=heapq.heappop(num)
            if  not marked[x[1]]:
                out+=x[0]
                marked[x[1]]=1
                if x[1]>0:
                    marked[x[1]-1]=1
                if x[1]<n-1:
                    marked[x[1]+1]=1
        return out


