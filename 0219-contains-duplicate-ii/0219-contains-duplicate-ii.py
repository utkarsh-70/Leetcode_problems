class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        di={}
        for i in range(len(nums)):
            if nums[i] not in di:
                di[nums[i]]=[]
                di[nums[i]].append(i)
            else:
                di[nums[i]].append(i)
        for i in di.values():
            for j in range(1,len(i)):
                if i[j]-i[j-1]<=k:
                    return True
        return False