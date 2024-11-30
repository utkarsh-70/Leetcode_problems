class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j=0,0
        maxone=0
        kcount=0
        while j<len(nums):
            if nums[j]==0:
                kcount+=1
            if kcount<=k:
                maxone=max(maxone,j-i+1)
            else:
                while  kcount>k and i<len(nums):
                    if nums[i]==0:
                        kcount-=1
                    i+=1
            j+=1
        return maxone

