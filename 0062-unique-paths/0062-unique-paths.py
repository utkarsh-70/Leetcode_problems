class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def topd(i,j):
            if i==m-1 and j==n-1:
                return 1
            if i>=m or j>=n:
                return 0
            right=topd(i,j+1)
            down=topd(i+1,j)
            return right+down
        return topd(0,0)