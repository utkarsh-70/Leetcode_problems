class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rm=[min(x) for x in matrix]
        cm=[]
        i=0
        j=0
        while j<len(matrix[0]):
            i=0
            cmax=-1
            while i<len(matrix):
                cmax=max(cmax,matrix[i][j])
                i+=1
            cm.append(cmax)
            j+=1
        return list(set(rm) & set(cm))
