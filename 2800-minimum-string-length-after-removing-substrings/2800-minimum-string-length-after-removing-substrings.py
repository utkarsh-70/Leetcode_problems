class Solution1:
    def minLength(self, s: str) -> int:
        if len(s)==1:
            return 1
        s=list(s)

        while 'AB' in s or 'CD' in s:
            i,j=0,1
            while i<len(s) and j<len(s):
                if s[i]+s[j]=='AB' or s[i]+s[j]=='CD':
                    s.pop(j)
                    s.pop(i)
                else:
                    i+=1
                    j+=1
                
        return len(s)


class Solution:
    def minLength(self, s: str) -> int:
        while 'AB' in s or 'CD' in s:
            if 'AB' in s:
                idx=s.index('AB')
                s=s[:idx]+s[idx+2:]
            if 'CD' in s:
                idx=s.index('CD')
                s=s[:idx]+s[idx+2:]
        return len(s)