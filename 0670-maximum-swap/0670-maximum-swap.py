class Solution:
    def maximumSwap(self, num: int) -> int:
        num=list(str(num))
        idx={num[i]:i for i in range(len(num))}
        for i in range(len(num)):
            for j in range(9,int(num[i]),-1):
                if str(j) in idx and idx[str(j)]>i:
                    num[i],num[idx[str(j)]]=num[idx[str(j)]],num[i]
                    return int(''.join(num))
        return int(''.join(num))
                