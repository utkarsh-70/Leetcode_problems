class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        memo={}
        def solve(i,j):
            key=(i,j)
            if key in memo:
                return memo[key]
            if j>=n:
                return False
            x,y=False,False
            if s[i:j+1] in wordDict:
                if j==n-1:
                    return True

                x=solve(j+1,j+1)
           
            y=solve(i,j+1)
            memo[key]= x or y
            return memo[key]
        return solve(0,0)



        