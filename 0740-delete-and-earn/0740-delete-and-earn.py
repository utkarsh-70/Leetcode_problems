class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        di={}
        for i in nums:
            if i  in di:
                di[i]+=1
            else:
                di[i]=1
        temp=list(di.keys())
        temp.sort()
        memo={}
        def topd(i,prev,taken):     
            if (i,taken) in memo:
                return memo[(i,taken)]    
            if i==len(temp):
                return 0
            take,skip=0,0
            if temp[i]!=prev+1:       
                take=(di[temp[i]]*temp[i])+topd(i+1,temp[i],True)
           
            skip=topd(i+1,prev,False)
            memo[(i,taken)]=max(take,skip)
            return memo[(i,taken)]
        return topd(0,-1,False)