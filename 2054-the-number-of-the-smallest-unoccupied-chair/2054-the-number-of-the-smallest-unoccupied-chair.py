class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target=times[targetFriend]
        times.sort()
        heap=[]
        emp=[]
        heapq.heapify(emp)
        idx=0
        heapq.heapify(heap)
        for i in range(len(times)):
            while heap and heap[0][0]<=times[i][0]:
                x=heapq.heappop(heap)
                heapq.heappush(emp,x[1])
            if emp:
                temp=heapq.heappop(emp)
                if times[i]==target:
                    return temp
                heapq.heappush(heap,[times[i][1],temp])
            else:
                if times[i]==target:
                    return idx
                heapq.heappush(heap,[times[i][1],idx])
                idx+=1
    
        return -1
                  
        return idx
