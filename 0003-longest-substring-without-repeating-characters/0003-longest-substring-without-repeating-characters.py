class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1=set()
        i,j=0,0
        maxl=0
        while j<len(s):
            while s[j] in set1:
                set1.remove(s[i])
                i+=1
            if s[j] not in set1:
                maxl=max(maxl,j-i+1)
                set1.add(s[j])
            j+=1
        return maxl