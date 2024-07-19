class Solution:
    def countVowelStrings(self, n: int) -> int:
        li=[1,1,1,1,1]
        for _ in range(n-1):
            li1=[1]
            for i in range(1,5):
                li1.append(li[i]+li1[i-1])
            li=li1
        return sum(li)
                