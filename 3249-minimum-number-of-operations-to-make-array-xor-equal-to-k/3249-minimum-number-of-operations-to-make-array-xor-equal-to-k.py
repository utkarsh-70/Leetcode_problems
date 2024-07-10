class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        bin1=0
        outc=0
        for i in nums:
            bin1^=i
        bin1=bin(bin1)[2:]
        k=bin(k)[2:]
        while len(bin1)<len(k):
            bin1='0'+bin1
        while len(k)<len(bin1):
            k='0'+k
    
        for i in range(len(bin1)):
            if bin1[i]!=k[i]:
                outc+=1
        return outc
