class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def topd(i,j):
            if i>j:
                return 0
            if s[i]==s[j]:
                return topd(i+1,j-1)
            else:
                return 1+min(topd(i,j-1),topd(i+1,j))
        return topd(0,len(s)-1)