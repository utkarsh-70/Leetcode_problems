class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        for i in range(len(arr)):
            arr[i]%=k
        di={}
        for i in arr:
            if i not in di:
                di[i]=1
            else:
                di[i]+=1
        print(di)
        for i in di:
            if i == 0:
                if di[i] % 2 != 0:
                    return False
            else:
                if k - i not in di or di[k - i] != di[i]: 
                    return False
        return True