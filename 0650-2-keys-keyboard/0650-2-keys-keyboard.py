class Solution:
    def minSteps(self, n: int) -> int:
        di={}
        def solve(ac, prev):
            if (ac,prev) in di:
                return di[(ac,prev)]
            if ac==n:
                return 0
            if ac>n:
                return 1000
            if prev == 0:
                return 2 + solve(ac + ac, ac)
            x=1+solve(ac+prev,prev)
            y=2+solve(ac+ac,ac)
            di[(ac,prev)]=min(x,y)
            return di[(ac,prev)]
        return solve(1, 0)