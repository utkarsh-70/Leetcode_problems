class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row=len(matrix)
        col=len(matrix[0])
        @cache
        def topd(i,j,prev):
            if i<0 or i>=row or j<0 or j>=col  or prev>=matrix[i][j]:
                return 0
            a=1+topd(i+1,j,matrix[i][j])
            b=1+topd(i,j+1,matrix[i][j])
            c=1+topd(i-1,j,matrix[i][j])
            d=1+topd(i,j-1,matrix[i][j])
            
            return max(a,b,c,d)
        maxout=0
        for i in range(row):
            for j in range(col):
                maxout=max(maxout,topd(i,j,-1))
        return maxout