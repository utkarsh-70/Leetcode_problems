class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def solve(ac, prev):
            if ac==n:
                return 0
            if ac>n:
                return 1000
            if prev == 0:
                return 2 + solve(ac + ac, ac)
            x=1+solve(ac+prev,prev)
            y=2+solve(ac+ac,ac)
            return min(x,y)
        return solve(1, 0)