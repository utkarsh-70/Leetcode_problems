class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        totsum=sum(cardPoints)
        wins=0
        maxsc=0
        n=len(cardPoints)
        for i in range(n-k):
            wins+=cardPoints[i]
        maxsc=totsum-wins
        i,j=0,n-k
        while j<n:
            wins-=cardPoints[i]
            i+=1
            wins+=cardPoints[j]
            j+=1
            maxsc=max(maxsc,totsum-wins)
        return maxsc