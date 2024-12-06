class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban={x:-1 for  x in banned}
        currs=0
        count=0
        for x in range(1,n+1):
            if x not in ban:
                currs+=x
            else:
                continue
            if currs<=maxSum:
                count+=1
            else:
                break
        return count

        