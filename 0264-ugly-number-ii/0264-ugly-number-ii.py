class Solution1:
    def nthUglyNumber(self, n: int) -> int:
        temp=[2,3,5]
        def bottomUp(i,t1,out):
            if t1>=n:
                print(out)
                return out
            x=[]
            for j in range(i,len(temp)):
                out.append(temp[j]*t1)
                print(out)
                x=bottomUp(j+1,temp[j]*t1,out)
            return x
        
        out=bottomUp(0,1,[])
        print(out)
        return 0


class Solution2:
    def nthUglyNumber(self, n: int) -> int:
        temp=[2,3,5]
        def topD(i,t1):
            if t1>=n:
                return []
            for j in range(i,len(temp)):
                return [t1*temp[j]]+topD(j+1,t1*temp[j])
        out=topD(0,1)
        print(out)
        return 0
        

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        out=[1]
        temp=[2,3,5]
        x=1
        idx=0
        while x<n:
            for i in range(3):
                val=out[idx]*temp[i]
                if val not in out:
                    out.append(val)
                    
            idx=idx+1
            x+=1
            out.sort()

        return out[n-1]