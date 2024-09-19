class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        ans=[]
        for i,j in dic.items():
            if j>len(nums)/3:
                ans.append(i)
            else:
                continue
        return ans