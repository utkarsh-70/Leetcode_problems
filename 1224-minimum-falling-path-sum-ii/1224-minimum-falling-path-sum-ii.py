class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid)
        currcol=-100
        for i in range(row-2,-1,-1):
            for k in range(col):
                minv=float('inf')
                for j in range(0,col):
                    if j==k:
                        continue
                    minv=min(minv,grid[i+1][j])
                grid[i][k]+=minv
        return min(x for x in grid[0])
