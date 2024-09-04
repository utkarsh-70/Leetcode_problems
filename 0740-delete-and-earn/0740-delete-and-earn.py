class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        has = {}
        for i in nums:
            if i not in has:
                has[i] = 0
            has[i] += 1

        @cache
        def earn(i):
            if i > unique[-1]:
                return 0
            if i not in has:
                has[i] = 0
            return max(earn(i + 1), has[i] * i + earn(i + 2) )

        return earn(1)

class Solution1:
    def deleteAndEarn(self, nums: List[int]) -> int:
        di={}
        def topd(i,s1):
            if (i,s1) in di:
                return di[(i,s1)]
            if i==len(nums):
                return 0
            x=0
            for j in range(i,len(nums)):
                if nums[j] not in s1:
                    s1.append(nums[j]+1)
                    s1.append(nums[j]-1)
                    y=nums[j]+topd(j+1,s1)
                    s1.remove(nums[j]+1)
                    s1.remove(nums[j]-1)
                    x=max(x,y)
            di[(i,s1)]=x 
            return di[(i,s1)]
        return topd(0,())
                