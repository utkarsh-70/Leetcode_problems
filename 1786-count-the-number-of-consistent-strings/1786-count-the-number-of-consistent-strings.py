class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for i in words:
            fl=0
            for j in i:
                fl=0
                if j not in allowed:
                    fl=1
                    break
            if not fl:
                count+=1
        return count