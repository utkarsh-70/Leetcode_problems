class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp=arr[:]
        temp.sort()
        di={}
        r=1
        for i in temp:
            if i not in di:
                di[i]=r
                r+=1
        out=[]
        for i in arr:
            out.append(di[i])
        return out