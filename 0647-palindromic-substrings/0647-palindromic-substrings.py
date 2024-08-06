class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        temp=''
        for i in range(len(s)):
            temp=''
            for j in range(i,len(s)):
                temp+=s[j]
                if temp==temp[::-1]:
                    count+=1
        return count
