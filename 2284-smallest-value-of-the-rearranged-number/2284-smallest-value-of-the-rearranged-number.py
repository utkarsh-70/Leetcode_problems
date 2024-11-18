class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:
            return 0
        if num<0:
            num*=-1
            li=list(str(num))
            li=sorted(li,reverse=True)
            return -1*int("".join(li))
        else:
            li=list(str(num))
            li=sorted(li)
            i=0
            while i<len(li) and li[i]=='0':
                i+=1
            li[0],li[i]=li[i],li[0]
            return int("".join(li))