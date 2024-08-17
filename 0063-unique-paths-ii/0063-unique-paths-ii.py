class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
        obstacleGrid[n-1][m-1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1 , -1):
                if obstacleGrid[i][j] == -1:
                    obstacleGrid[i][j] = 0
                    continue
                if i != n - 1:
                    obstacleGrid[i][j] += obstacleGrid[i + 1][j]
                if j != m - 1:
                    obstacleGrid[i][j] += obstacleGrid[i][j + 1]
        
        return obstacleGrid[0][0]

