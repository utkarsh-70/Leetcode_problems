class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        tbl = [[0] * m for _ in range(n)]
        tbl[n-1][m-1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1 , -1):
                if obstacleGrid[i][j] == 1:
                    tbl[i][j] = 0
                    continue
                if i != n - 1:
                    tbl[i][j] += tbl[i + 1][j]
                if j != m - 1:
                    tbl[i][j] += tbl[i][j + 1]
        
        return tbl[0][0]


class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def solve(obstacle,i,j,di):
            if (i,j) in di:
                return di[(i,j)]
            if i==len(obstacle)-1 and j==len(obstacle[0])-1 and obstacle[i][j]!=1:
                return 1
            if i==len(obstacle) or j==len(obstacle[0]):
                return 0
            if obstacle[i][j]==1:
                return 0
            di[(i,j)]=solve(obstacle,i+1,j,di)+solve(obstacle,i,j+1,di)
            return di[(i,j)]
        return solve(obstacleGrid,0,0,{})
