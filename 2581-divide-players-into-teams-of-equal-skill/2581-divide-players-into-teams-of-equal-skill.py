class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i,j=0,len(skill)-1
        chem=0
        fl=-1
        while i<=j:
            if fl>0 and skill[i]+skill[j]!=fl:
                return -1
            else:
                fl=skill[i]+skill[j]
                chem+=skill[i]*skill[j]
                i+=1
                j-=1
        return chem
