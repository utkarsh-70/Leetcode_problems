class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1={}
        for i in s:
            if i not in dic1:
                dic1[i]=1
            else:
                dic1[i]+=1
        
        dic2={}
        for i in t:
            if i not in dic2:
                dic2[i]=1
            else:
                dic2[i]+=1


        for i,j in dic1.items():
            if i in dic2:
                if j!=dic2[i]:
                    return False
            else:
                return False
        for i,j in dic2.items():
            if i in dic1:
                if j!=dic1[i]:
                    
                    return False
            else:
                return False
        return True
        