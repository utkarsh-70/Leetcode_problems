class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        di={}
        def topd(i,fl):
            if (i,fl) in di:
                return di[(i,fl)]
            if i==len(prices):
                return 0
            x,y=0,0
            if not fl:
                x=-1*prices[i]+topd(i+1,1)
            else:
                y= prices[i]-fee+topd(i+1,0)
            z=topd(i+1,fl)
            di[(i,fl)]=max(x,y,z)
            return di[(i,fl)]
        return topd(0,0)