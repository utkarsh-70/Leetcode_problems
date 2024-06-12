class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i,j=0,n-1
        for x in range(n):
            while j>=0 and nums[j]==2:
                j-=1
            if j>=0 and nums[x]==2 and x<j:
                nums[j],nums[x]=nums[x],nums[j]
                j-=1
        for x in range(n-1,0,-1):
            while i<n and nums[i]==0:
                i+=1
            if i<n and nums[x]==0 and x>i:
                nums[i],nums[x]=nums[x],nums[i]
                i+=1