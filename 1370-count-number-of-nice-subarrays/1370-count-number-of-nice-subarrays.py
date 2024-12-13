class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums=[0 if x%2==0  else 1 for x in nums]
        n=len(nums)
        def countfn(goal):
            if goal==-1:
                return 0
            i,j=0,0
            curr,count=0,0
            while j<n:
                curr+=nums[j]
                while curr>goal and i<n:
                    curr-=nums[i]
                    i+=1
        
                if curr<=goal:
                    count+=(j-i+1)
                j+=1
           
            return count
        return countfn(k)-countfn(k-1) 