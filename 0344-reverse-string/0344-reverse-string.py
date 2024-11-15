class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        def solve(i):
            if i==n//2:
                return 
            s[i],s[n-i-1]=s[n-i-1],s[i]
            solve(i+1)
        solve(0)
            