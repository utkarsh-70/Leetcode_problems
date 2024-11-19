class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        string=['abcde','fghij','klmno','pqrst','uvwxy','z    ']
        coord={}
        for i in range(len(string)):
            for j in range(len(string[0])):
                coord[string[i][j]]=[i,j]
                if string[i][j]=='z':
                    break
        initial=[0,0]
        out=''
        for i in range(len(target)):
            t=coord[target[i]]
            for j in range(abs(initial[1]-t[1])):
                if t[1]<initial[1]:
                    out+='L'
                else:
                    out+='R'
            for x in range(abs(initial[0]-t[0])):
                if t[0]<initial[0]:
                    out+='U'
                else:
                    out+='D'
            
            out+='!'
            if i<len(target)-1 and target[i+1]!='z' and target[i]=='z':
                out+='U'
                initial=[4,0]
            else:
                initial=t
        return out
