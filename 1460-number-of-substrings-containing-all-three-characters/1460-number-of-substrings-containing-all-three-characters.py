class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hs={'a':0,'b':0,'c':0}
        size=len(s)
        def valid():
            return hs['a']>0 and hs['b']>0 and hs['c']>0
        i,j=0,0
        count=0
        while j < size:
            hs[s[j]] += 1

            while valid():  
                count += size - j  
                hs[s[i]] -= 1
                i += 1

            j += 1
        return count



