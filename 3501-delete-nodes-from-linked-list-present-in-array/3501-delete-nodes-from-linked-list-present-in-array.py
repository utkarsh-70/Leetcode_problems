# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find(self,nums,val):
        beg,end=0,len(nums)-1
        while beg<=end:
            mid=(beg+end)//2
            if nums[mid]==val:
                return True
            elif nums[mid]<val:
                beg=mid+1
            else:
                end=mid-1
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        st=[]
        nums.sort()
        while temp:
            
            if self.find(nums,temp.val):
                pass
            else:
                st.append(temp)
            temp=temp.next
        if st:
            st[-1].next=None
        temp=None
        ans=None
        while st:
            x=st.pop(0)
            if not temp:
                temp=x
                ans=x
            else:
                temp.next=x
                temp=temp.next
        return ans
                
        return temp