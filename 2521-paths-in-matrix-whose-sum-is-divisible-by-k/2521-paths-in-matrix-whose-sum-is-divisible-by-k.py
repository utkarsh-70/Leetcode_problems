class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        mod = 10**9+7
        di={}
        def bt(i,j,sum1):
            if (i,j,sum1) in di:
                return di[(i,j,sum1)]
            if i>=m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                if((sum1+grid[i][j])%k==0):
                    return 1
                else:
                    return 0
            # print(sum1) 
            currsum = (sum1 + grid[i][j]) % k
            di[(i,j,sum1)] = ((bt(i+1,j,currsum)%mod)+(bt(i,j+1,currsum)%mod))%mod
            return di[(i,j,sum1)]
        return bt(0,0,0)