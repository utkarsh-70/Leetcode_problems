class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return 
        hand.sort()
        i=0
        while i<len(hand):
            c=groupSize
            x=hand[i]
            while c:
                if x in hand:
                    hand.remove(x)
                else:
                    return False
                x+=1
                c-=1
            i=0
        

        if not hand:
            return True
        return False