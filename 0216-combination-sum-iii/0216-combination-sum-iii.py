class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def comb(i, k, n):
            if k == 0 and n == 0:
                return [[]]
            if i > 9 or k < 0 or  n < 0:
                return []
            skipped = comb(i + 1, k, n)
            not_skipped = []
            if n >= i:
                not_skipped = comb(i + 1, k - 1, n - i)
                not_skipped = [x + [i] for x in not_skipped]
            return skipped + not_skipped 
        return comb(1, k, n)