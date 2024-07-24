class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        n=max(nums)
        min1=min(nums)
        if min1<0:
            f=[0]*(n-min1+1)
        else:
            f=[0]*(n+1)
        print(f)
        out=[]
        for i in nums:
            if min1<0:
                f[i-min1]+=1
            else:
                f[i]+=1
        print(f)
        x=0
        n=n-min1+1 if min1<0 else n
        while x<=n:
            min2=float('inf')
            minidx=-1
            for i in range(len(f)):
                if f[i]!=0 and f[i]<=min2:
                    min2=f[i]
                    minidx=i
        
            temp=f[minidx]
            print(f,temp,minidx)
            f[minidx]=0
            while temp:
                if min1<0:
                    print
                    out.append(minidx+min1)
                else:
                    out.append(minidx)
                temp-=1
            
            x+=1
        return out

        