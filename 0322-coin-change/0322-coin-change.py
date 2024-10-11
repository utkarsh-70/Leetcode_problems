class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        di={}
        coins.sort()
        def topd(amount):
            if amount==0:
                return 0
            if amount<0:
                return float('inf')
            if  amount in di:
                return di[amount]

            min_val=float('inf')
            for j in range(0,n):
                if amount-coins[j]>=0:
                    min_val=min(min_val,1+topd(amount-coins[j]))
                else:
                    break
            di[amount]=min_val
            return di[amount]
        x=topd(amount)
        return x if x!=float('inf') else -1 
        