class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        di={}
        out=[]
        for i in nums2:
            while st and st[-1]<i:
                x=st.pop()
                di[x]=i
            st.append(i)
        while st:
            x=st.pop()
            di[x]=-1
    
        for j in nums1:
            out.append(di[j])
        return out