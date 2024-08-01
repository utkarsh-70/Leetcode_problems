class Solution:
    def countSeniors(self, details: List[str]) -> int:
        lesc=0
        for i in details:
            if int(i[-4:-2])>60:
            
                lesc+=1
        return lesc