class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        out=[-1]*n
        st=[]
        idx=[0]*n
        pc=0
        for i in range(n):
            while st and st[-1]<nums[i]:
                x=st.pop()
                ind=idx.pop()
                out[ind]=nums[i]
            st.append(nums[i])
            idx.append(i)
        for i in range(n):
            while st and st[-1]<nums[i]:
                x=st.pop()
                ind=idx.pop()
                out[ind]=nums[i]
        
        return out