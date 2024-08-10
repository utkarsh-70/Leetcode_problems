# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self,head):
        prev,curr,ne=head,head,head.next
        while ne:
            curr.next=ne.next
            ne.next=prev
            prev=ne
            ne=curr.next
        return prev
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        c=0
        out=None
        fl=0
        temp=head
        curr=head
        pcurr=head
        while temp:
            c+=1
            if c==k:
                te=temp
                temp=temp.next
                te.next=None
                x=self.rev(curr)
                if not fl:
                    out=x
                    fl=1
                else:
                    pcurr.next=x
    
                curr.next=temp
                pcurr=curr
                curr=temp
                c=0
            else:
                temp=temp.next
            
        return out
