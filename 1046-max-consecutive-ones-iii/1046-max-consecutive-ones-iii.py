class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j=0,0
        maxone=0
        recent=[]
        x=0
        kcount=0
        while j<len(nums):
            if nums[j]==0:
                recent.append(j)
                kcount+=1
            if kcount<=k:
                maxone=max(maxone,j-i+1)
            else:
                i=recent[x]+1
                kcount-=1
                x+=1
            j+=1
        return maxone

