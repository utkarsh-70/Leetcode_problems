class Solution:
    def numSplits(self, s: str) -> int:
        count=0
        left=[0]*len(s)
        right=[0]*len(s)
        se=set()
        for i in range(len(s)):
            if not se:
                se.add(s[0])
                left[0]=1
            elif s[i] in se:
                left[i]=left[i-1]
            else:
                se.add(s[i])
                left[i]=left[i-1]+1
        se=set()
        for i in range(len(s)-1,-1,-1):
            if not se:
                se.add(s[-1])
                right[-1]=1
            elif s[i] in se:
                right[i]=right[i+1]
            else:
                se.add(s[i])
                right[i]=right[i+1]+1
        left.pop(-1)
        right.pop(0)
        for i in range(len(left)):
            if left[i]==right[i]:
                count+=1
        
        return count
