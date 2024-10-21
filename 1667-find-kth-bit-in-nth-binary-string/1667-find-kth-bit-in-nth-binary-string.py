class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rev(st):
            out=''
            for i in reversed(st):
                if i=='0':
                    out=out+'1'
                else:
                    out=out+'0'            
            return out
        def calc(i,s):
            if i==n:
                return s[k-1]
            return calc(i+1,s+'1'+rev(s))
        return calc(0,'0')
