class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row=len(matrix)
        col=len(matrix[0])
        @cache
        def topd(i,j):
            if i==row-1 and j>=0 and j<col:
                return matrix[i][j]
            if j<0 or i>=row or j>=col:
                return float('inf')
            bott=matrix[i][j]+topd(i+1,j)
            rdiag=matrix[i][j]+topd(i+1,j+1)
            ldiag=matrix[i][j]+topd(i+1,j-1)
            return min(bott,rdiag,ldiag)
        min1=float('inf')
        for j in range(col):
            min1=min(min1,topd(0,j))
        return min1
        