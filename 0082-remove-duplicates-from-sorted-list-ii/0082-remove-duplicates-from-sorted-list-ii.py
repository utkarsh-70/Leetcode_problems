# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        st=[]
        fl=0
        t2=ListNode(-1)
        out=t2
        while temp:
            if not st:
                st.append(temp)
            else:         
                if temp.val==st[-1].val:
                    fl=1
                else:
                    if fl==1:
                        st.pop()
                        fl=0
                    st.append(temp)
            temp=temp.next
        if fl:
            st.pop(-1)
        while st:
            t2.next=st.pop(0)
            t2=t2.next
            if not st:
                t2.next=None
           
        return out.next
        