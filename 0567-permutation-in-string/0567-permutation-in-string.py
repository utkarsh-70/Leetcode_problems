class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        if len(s1)==len(s2):
            if sorted(s1)==sorted(s2):
                return True
            return False
        di1={}
        for i in s1:
            if i not in di1:
                di1[i]=1
            else:
                di1[i]+=1
        i,j=0,len(s1)
        di2={}
        for i in range(len(s1)):
            if s2[i] not in di2:
                di2[s2[i]]=1
            else:
                di2[s2[i]]+=1
    
        if di1==di2:
            return True

        i=0
        while j<len(s2):
        
            if di2[s2[i]]==1:
                del di2[s2[i]]
            else:
                di2[s2[i]]-=1
            if s2[j] not in di2:
                di2[s2[j]]=1
            else:
                di2[s2[j]]+=1
            if di1==di2:
                return True
            i+=1
            j+=1
        return False

