class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        memo = [[-1] * m for _ in range(n)]
        
        def dfs(i: int, j: int) -> int:
            if i == n or j == m:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            if nums1[i] == nums2[j]:
                memo[i][j] = 1 + dfs(i + 1, j + 1)
            else:
                memo[i][j] = 0
            return memo[i][j]
        
        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res, dfs(i, j))
        return res