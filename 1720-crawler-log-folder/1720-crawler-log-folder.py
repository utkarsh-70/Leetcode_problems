class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st=[]
        for i in logs:
            if i=='./':
                pass
            elif i=='../':
                if st:
                    st.pop(-1)
            else:
                st.append(i)
        return len(st)        