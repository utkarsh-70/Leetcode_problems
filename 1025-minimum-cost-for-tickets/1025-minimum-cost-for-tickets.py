class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def topd(i,prev):
            if i==len(days):
                return 0
            if days[i]<=prev:
                return topd(i+1,prev)
            else:
                c1,c2,c3=float('inf'),float('inf'),float('inf')
                c1=costs[0]+topd(i+1,days[i])
                c2=costs[1]+topd(i+1,days[i]+6)
                c3=costs[2]+topd(i+1,days[i]+29)
                return min(c1,c2,c3)
                
        return topd(0,0)