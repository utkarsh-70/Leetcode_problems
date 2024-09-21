class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        @cache
        def dp(i, j, curr):
            if i == m - 1 and j == n - 1: return int(curr == 0)
            res = 0
            for di, dj in [(0, 1), (1, 0)]:
                ni, nj = i + di, j + dj
                if ni < 0 or ni == m or nj < 0 or nj == n: continue
                res = (res + dp(ni, nj, (curr + grid[ni][nj]) % k)) % mod
            return res

        return dp(0, 0, grid[0][0] % k) % mod