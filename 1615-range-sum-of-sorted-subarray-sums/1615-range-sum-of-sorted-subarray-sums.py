class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        temp=[]
        for i in range(len(nums)):
            sum1=nums[i]
            temp.append(sum1)
            for j in range(i+1,len(nums)):
                sum1+=nums[j]
                temp.append(sum1)        
        temp.sort()
       
        return sum(temp[left-1:right])%(10**9+7)