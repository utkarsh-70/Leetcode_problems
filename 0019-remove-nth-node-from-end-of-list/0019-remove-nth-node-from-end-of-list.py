# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        st=[]
        temp=head
        len1=0
        t1=head
        while t1:
            len1+=1
            t1=t1.next
        while temp:
            st.append(temp)
            temp=temp.next
        c=0
        temp=ListNode(-1)
        ans=temp
        if st:
            st[0].next=None
        
        while st:
            x=st.pop(0)
           
            if c==len1-n:
                x.next=None
                pass
            else:
                temp.next=x
                temp=temp.next
                temp.next=None
                
            c+=1
        return ans.next