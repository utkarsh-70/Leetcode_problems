class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        temp=[]
        for i in nums:
            curr=''
            for j in str(i):
                x=int(j)
                curr+=str(mapping[x])
            curr=int(curr) if curr else 0
            temp.append([curr,i])
        print(temp)
        temp=sorted(temp,key=lambda x:x[0])

        return [x[1] for x in temp]