class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        out=[]
        ex=[]
        di={}
        for i in arr1:
            if i not in di:
                di[i]=1
            else:
                di[i]+=1
        for i in arr2:
            val=di[i]
            while val:
                out.append(i)
                val-=1
        for i in arr1:
            if i not in arr2:
                ex.append(i)
        return out+sorted(ex)