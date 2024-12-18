class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gainfn(passi,totali):
            return (passi+1)/(totali+1)-passi/totali
        heap=[]
        for passi,totali in classes:
            gain=gainfn(passi,totali)
            heapq.heappush(heap,(-gain,passi,totali))
        while extraStudents:
            gain,passi,totali=heapq.heappop(heap)

            newgain=gainfn(passi+1,totali+1)
            heapq.heappush(heap,(-newgain,passi+1,totali+1))
            extraStudents-=1
        total=0
        for _,passi,totali in heap:
            total+=(passi/totali)
        return total/len(classes)