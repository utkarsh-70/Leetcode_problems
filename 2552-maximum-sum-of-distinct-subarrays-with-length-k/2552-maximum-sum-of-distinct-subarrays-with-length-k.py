class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        dup=dict()
        out,temps=0,0
        dupc=0
        for i in range(k):
            if nums[i] not in dup:
                dup[nums[i]]=1
            else:
                dup[nums[i]]+=1
            if dup[nums[i]]==2:
                dupc+=1
            temps+=nums[i]
        if not dupc:
            out=max(out,temps)

        i,j=0,k
        while i<len(nums) and j<len(nums):
            
            dup[nums[i]]-=1
            if dup[nums[i]]==1:
                dupc-=1
            temps-=nums[i]
            i+=1
            temps+=nums[j]
            if nums[j] in dup:
                if dup[nums[j]]==1:
                    dupc+=1
                dup[nums[j]]+=1
            else:
                dup[nums[j]]=1
            if dupc==0:
                out=max(out,temps)
            j+=1
            
        return out
