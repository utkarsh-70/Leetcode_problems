# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self,out=None):
        self.out=out
    def fun(self,head):
        if head==None:
            return None
        if head and not head.next:
            self.out=head
            
        else: 
            if head.next: 
                x=self.fun(head.next)
                x.next=head
                head.next=None

        return head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.fun(head)
        return self.out