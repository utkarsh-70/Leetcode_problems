class Solution:
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