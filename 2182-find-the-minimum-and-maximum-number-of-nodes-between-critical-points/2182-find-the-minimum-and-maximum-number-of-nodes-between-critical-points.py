# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head.next is None or head.next.next is None:
            return [-1,-1]
        prev,curr=head,head.next
        crp=[]
        idx=1
        while curr.next:
            if prev.val<curr.val and curr.next.val<curr.val:
                crp.append(idx)
            elif prev.val>curr.val and curr.next.val>curr.val:
                crp.append(idx)
            idx+=1
            prev=curr
            curr=curr.next
        min1,max1=999999999,-1
        crp.sort()
        print(crp)
        for i in range(1,len(crp)):
            min1=min(min1,crp[i]-crp[i-1])
        return [min1 if len(crp)>1 else -1,crp[-1]-crp[0] if len(crp)>1 else -1]
        