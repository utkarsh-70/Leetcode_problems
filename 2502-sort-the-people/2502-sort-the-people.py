class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        di={}
        for i in range(len(names)):
            di[heights[i]]=names[i]
        di=dict(sorted(di.items(), key = lambda x:x[0]))
        # print(di)
        return list(di.values())[::-1]