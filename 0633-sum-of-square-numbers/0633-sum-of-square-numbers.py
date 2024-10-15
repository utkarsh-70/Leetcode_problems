class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i,j=0,int(c**0.5)
        while i<=j:
            temp=i*i+j*j
            if temp==c:
                return True
            elif temp<c:
                i+=1
            else:
                j-=1
        return False