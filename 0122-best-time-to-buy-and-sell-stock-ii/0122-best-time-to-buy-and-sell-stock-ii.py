class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        i=0
        cmin,cmax=9999999999,-1
        while i <len(prices)-1:
            if prices[i]<prices[i+1]:
                maxp+=(prices[i+1]-prices[i])    
            
            i+=1
        return maxp
                
            
            
        