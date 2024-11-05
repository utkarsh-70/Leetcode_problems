class Solution:
    def compressedString(self, word: str) -> str:
        count=1
        out=''
        for i in range(1,len(word)):
            if word[i]!=word[i-1] or count==9:
                out+=str(count)
                out+=word[i-1]
                count=1
            else:
                count+=1
        out+=str(count)
        out+=word[-1]

        return out