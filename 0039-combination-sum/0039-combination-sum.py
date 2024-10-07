class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        def backt(i,curr,out,temp):
            if curr==target:
                out.append(temp[:])
                return 
            if i==n or curr>target:
                return 
            for j in range(i,n):
                curr+=candidates[j]
                temp.append(candidates[j])
                backt(j,curr,out,temp)
                curr-=candidates[j]
                temp.remove(candidates[j])
            return out
        return backt(0,0,[],[])
