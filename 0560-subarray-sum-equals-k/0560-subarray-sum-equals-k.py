class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hs={0:1}
        pre=0
        count=0
        for x in nums:
            pre+=x
            if pre-k in hs:
                count+=hs[pre-k]
            if pre not in hs:
                hs[pre]=1
            else:
                hs[pre]+=1
        return count