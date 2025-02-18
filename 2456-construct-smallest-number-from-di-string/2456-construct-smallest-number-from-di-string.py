class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def backtrack(currs,i,taken):
            if i==len(pattern):
                
                return currs
            cu=int(currs[-1])
            if pattern[i]=='I':
                fl=0
                for x in range(cu+1,10):
                    if not taken[x]:
                        fl=1
                        taken[x]=1
                        res=backtrack(currs+str(x),i+1,taken)
                        taken[x]=0
                        if res:
                            return res
                if not fl:
                    return ''
            else:
                fl=0
                for x in range(1,cu):
                    if not taken[x]:
                        fl=1
                        taken[x]=1
                        res=backtrack(currs+str(x),i+1,taken)
                        taken[x]=0
                        if res:
                            return res
                if not fl:
                    return ''
        
        for i in range(1,10):
            taken=[0]*10
            taken[i]=1
            out=backtrack(str(i),0,taken)
            if out:
                return out
            taken[i]=0
        return ""

                        
                        
                