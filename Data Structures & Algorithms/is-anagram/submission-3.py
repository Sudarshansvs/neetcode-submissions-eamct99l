class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        jdict= dict()
        sdict = dict()

        for i in s:
            if i in sdict :
                sdict[i] +=1
            else:
                sdict[i]=1
        for j in t :
            if j in jdict :
                jdict[j] +=1
            else:
                jdict[j]=1
        #print(sdict, jdict)
        return sdict == jdict


        