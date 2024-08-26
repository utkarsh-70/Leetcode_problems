class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        di={}
        def topd(i,skips):
            if (i,skips) in di:
                return di[(i,skips)]
            if i==len(prices):
                return 0
            x,y=float('inf'),float('inf')
            x=prices[i]+topd(i+1,2*i+1)
            if i<=skips:
                y=topd(i+1,skips)

            di[(i,skips)]=min(x,y)
            return di[(i,skips)]
        return prices[0]+topd(1,1)
    