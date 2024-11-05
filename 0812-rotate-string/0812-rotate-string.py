class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s==goal:
                return True
            x=s[0]
            s=s[1:]
            s=s+x
        return False