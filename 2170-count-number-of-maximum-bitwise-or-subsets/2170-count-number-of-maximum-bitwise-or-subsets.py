class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxbit=0
        for x in nums:
            maxbit=maxbit|x
        count=0
        def backt(i,Or):
            nonlocal count
           
            if i==len(nums):
                if Or==maxbit:
                    count+=1
                return 0
            backt(i+1,Or|nums[i])
            backt(i+1,Or)

        backt(0,0)
        return count

                
        