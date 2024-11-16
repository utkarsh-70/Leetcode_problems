class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def check(arr):
            for i in range(1,len(arr)):
                if arr[i]<arr[i-1] or arr[i]!=arr[i-1]+1:
                    return -1
            return max(arr)
        temp=[]
        alla=[]
        for i in range(k):
            temp.append(nums[i])
        i=k
        alla.append(temp[:])
        while i<len(nums):
            temp.pop(0)
            temp.append(nums[i])
            alla.append(temp[:])
            i+=1
    
        out=[]
        for i in alla:
            out.append(check(i))
        return out
        
