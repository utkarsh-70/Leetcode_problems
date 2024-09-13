class Solution:
    def uniquePathsWithObstacles(self, ob: List[List[int]]) -> int:
        m=len(ob)
        n=len(ob[0])
        di={}
        def topd(i,j):
            if (i,j) in di:
                return di[(i,j)]
            if i==m-1 and j==n-1:
                if not ob[i][j]:
                    return 1
                return 0
            if i>=m or j>=n:
                return 0
            if ob[i][j]==1:
                return 0
            right=topd(i,j+1)
            bott=topd(i+1,j)
            di[(i,j)]=right+bott
            return di[(i,j)]
        return topd(0,0)

