# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1,temp2=head,head.next
        while temp2:
            if temp2.val!=0:
                temp1.val+=temp2.val
        
            else:
                if temp2.next:
                    temp1.next=temp2
                else:
                    temp1.next=None
                temp1=temp1.next
            temp2=temp2.next
        
        return head
        