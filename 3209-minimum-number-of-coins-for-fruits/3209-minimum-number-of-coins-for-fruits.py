class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        @cache
        def topd(i,skips):
            if i>=len(prices):
                return 0
            x,y=float('inf'),float('inf')
            x=prices[i]+topd(i+1,2*i+1)
            if i<=skips:
                y=topd(i+1,skips)

            return min(x,y)
        return prices[0]+topd(1,1)
    