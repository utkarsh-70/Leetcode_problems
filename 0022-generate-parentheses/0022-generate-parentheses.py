class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out=[]
        def backt(op,cl,s):
            if (cl+op)==n*2:
                out.append("".join(s))
            if op<n:
                s.append('(')
                backt(op+1,cl,s)
                s.pop()
            if cl<op:
                s.append(')')
                backt(op,cl+1,s)
                s.pop()
        backt(0,0,[])
        return out