class Solution:
    def numSquares(self, n: int) -> int:
        if n**0.5==int(n**0.5):
            return 1
        @cache
        def topd(n):
            if n==0:
                return 0
            if n<0:
                return float('inf')
            out=float('inf')
            for i in range(1,math.ceil(n**0.5)+1):
                out=min(out,1+topd(n-i**2))
            return out
        return topd(n) 