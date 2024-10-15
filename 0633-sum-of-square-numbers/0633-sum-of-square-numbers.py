class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        temp=[]
        i=0
        while i*i<=c:    
            temp.append(i*i)
            i+=1
        n=i-1
        i,j=0,n
        while i<=j:
            if temp[i]+temp[j]==c:
                return True
            elif temp[i]+temp[j]<c:
                i+=1
            else:
                j-=1
        return False
