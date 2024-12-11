class Solution:
    def characterReplacement(self, nums: str, k: int) -> int:
        freq=[0]*26

        def valid():
            x=max(freq)
            sum1=sum(freq)
            return sum1-x<=k
        i,j=0,0
        out=0
        while j<len(nums):
            while i<len(nums) and not valid():
                freq[ord(nums[i])-65]-=1
                i+=1  
            freq[ord(nums[j])-65]+=1
    
            if valid():
                out=max(out,j-i+1)
            j+=1
        return out
            
