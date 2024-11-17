class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for i in range(len(asteroids)):
            if not st  or st[-1]<0 and asteroids[i]<0 or st[-1]>0 and asteroids[i]>0 :
                st.append(asteroids[i])
            else:
                if st and st[-1]>0 and asteroids[i]<0 and -1*st[-1]==asteroids[i]:
                    st.pop(-1)
                elif asteroids[i]<0:
                    fl=0
                    while st and st[-1]>0:
                        if abs(st[-1])<abs(asteroids[i]):
                            st.pop(-1)
                        elif abs(st[-1])==abs(asteroids[i]) and st[-1]>0:
                            st.pop(-1)
                            fl=1
                        else:
                            break
                    if not fl and (not st or st[-1]<0):
                        st.append(asteroids[i])
                    
                else:
                    st.append(asteroids[i])
        return st
