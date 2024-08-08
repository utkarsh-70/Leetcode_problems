# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        t1,t2=list1,list2
        temp=ListNode(-1)
        ans=temp
        while t1 and t2:
            if t1.val<=t2.val:
                temp.next=t1
                temp=temp.next
                t1=t1.next
            else:
                temp.next=t2
                temp=temp.next
                t2=t2.next
        while t1:
            temp.next=t1
            temp=temp.next
            t1=t1.next
        while t2:
            temp.next=t2
            temp=temp.next
            t2=t2.next
        return ans.next


        