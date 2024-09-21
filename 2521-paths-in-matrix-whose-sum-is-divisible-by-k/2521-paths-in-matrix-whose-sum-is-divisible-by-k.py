class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        
        for i in range(1, m):
            for x in range(k):
                dp[i][0][(x + grid[i][0]) % k] = dp[i-1][0][x]
        for j in range(1, n):
            for x in range(k):
                dp[0][j][(x + grid[0][j]) % k] = dp[0][j-1][x]
        
        for i in range(1, m):
            for j in range(1, n):
                for x in range(k):
                    dp[i][j][(x + grid[i][j]) % k] = (dp[i-1][j][x] + dp[i][j-1][x]) % MOD
        
        return dp[m-1][n-1][0]