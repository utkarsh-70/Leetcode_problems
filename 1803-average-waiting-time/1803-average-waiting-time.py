class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        currt=customers[0][0]+customers[0][1]
        tott=currt-customers[0][0]
        fl=1
        for i in customers:
            if fl==1:
                fl=0
                pass
            else:
                if currt>i[0]:
                    currt+=i[1]
                    tott+=(currt-i[0])
                    
                else:
                    currt=0
                    currt+=(i[1]+i[0])
                    tott+=(currt-i[0])

        return tott/len(customers)