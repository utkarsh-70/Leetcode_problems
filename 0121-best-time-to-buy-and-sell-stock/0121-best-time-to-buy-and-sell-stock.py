class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totp=0
        min1=999999999
        min2=[]
        for i in range(len(prices)):
            min1=min(min1,prices[i])
            min2.append(min1)
            
        for i in range(len(prices)):
            totp=max(prices[i]-min2[i],totp)
        return totp

        