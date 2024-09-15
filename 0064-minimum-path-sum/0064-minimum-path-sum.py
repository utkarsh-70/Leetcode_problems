class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        memo={}
        def topd(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i==m-1 and j==n-1:
                return grid[i][j]
            if i>=m or j>=n:
                return float('inf')
            right=grid[i][j]+topd(i,j+1)
            bott=grid[i][j]+topd(i+1,j)
            memo[(i,j)]=min(right,bott)
            return memo[(i,j)]
        return topd(0,0)