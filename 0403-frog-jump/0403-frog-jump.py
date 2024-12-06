class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[0]!=0 or stones[1]!=1:
            return False
        
        posset=set(stones)
        memo={}
        def cross(curr,k):
            key=(curr,k)
            if key in memo:
                return memo[key]
            if curr==stones[-1]:
                return True
            if curr>stones[-1] or curr not in posset:
                return False
            if k<=0:
                return False
            c1=cross(curr+k,k)
            c2=cross(curr+k-1,k-1)
            c3=cross(curr+k+1,k+1)
            memo[key]= c1 or c2 or c3
            return memo[key]

        return cross(1,1)
