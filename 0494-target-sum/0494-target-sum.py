class Solution1:
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def func(nums,i,target,n):
            if i==n:
                return 1 if target==0 else 0
            return func(nums,i+1,target-nums[i],n)+func(nums,i+1,target+nums[i],n)
        return func(nums,0,target,len(nums))
        
class Solution:
    def findCount(self, nums, index, target, mem):
        if(index == len(nums)):
            if(target == 0):
                return 1
            else:
                return 0
        elif (index, target) in mem:
            return mem[(index, target)]

        mem[(index, target)] = self.findCount(nums, index+1, target-nums[index], mem) + self.findCount(nums, index+1, target+nums[index], mem)

        return mem[(index, target)]
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem = {}
        return self.findCount(nums, 0, target, mem)   
