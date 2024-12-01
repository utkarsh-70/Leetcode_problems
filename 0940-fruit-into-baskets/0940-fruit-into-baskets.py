class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i,j=0,0
        freq=defaultdict(int)
        fcount=0
        maxnum=0
        while j<len(fruits):
            if fruits[j] not in freq or freq[fruits[j]]==0:
                fcount+=1
            freq[fruits[j]]+=1
            if fcount<=2:
                maxnum=max(maxnum,j-i+1)
            while i<len(fruits) and fcount>2:
                freq[fruits[i]]-=1
                if freq[fruits[i]]==0:
                    fcount-=1
                i+=1
            j+=1
        return maxnum