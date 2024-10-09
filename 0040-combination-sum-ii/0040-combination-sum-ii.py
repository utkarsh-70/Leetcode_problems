class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        candidates.sort()
        def backt(i,curr,temp,out):
            if curr==target:
                out.append(temp[:])
                return
            if i==n or curr>target:
                return out

            for j in range(i,n):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                    
                curr+=candidates[j]
                temp.append(candidates[j])
                backt(j+1,curr,temp,out)
                curr-=candidates[j]
                temp.remove(candidates[j])

            return out
        return backt(0,0,[],[])