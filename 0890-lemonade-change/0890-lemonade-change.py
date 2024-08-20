class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        temp=[]
        for i in bills:
            if i==5:
                temp.append(5)
            elif i==10:
                if 5 not in temp:
                    return False
                else:
                    temp.append(10)
                    temp.remove(5)
            elif i==20:
                if 10 in temp and 5  in temp:
                    temp.append(20)
                    temp.remove(5)
                    temp.remove(10)
                elif temp.count(5)>=3:
                    temp.remove(5)
                    temp.remove(5)
                    temp.remove(5)
                else:
                    return False
        return True
