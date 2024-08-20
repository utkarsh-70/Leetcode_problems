class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        tbl = {}
        def comp(i, j):
            if (i, j) in tbl: return tbl[(i, j)]
            if i == n and j == m: return 1
            if i == n : return 0
            x = comp(i + 1, j)
            if j < m and s[i] == t[j]:
                x += comp(i + 1, j + 1)
            tbl[(i, j)] = x
            return x
        return comp(0,0)