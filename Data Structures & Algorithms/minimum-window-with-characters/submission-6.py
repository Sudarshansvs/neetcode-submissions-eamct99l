from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" :return ""
        thash = Counter(t)
        shash = {}
        have, need = 0, len(thash)
        res, reslen = [-1, -1], float("infinity")
        l =0
        for r  in range(len(s)):
            c = s[r]
            shash[c] = 1+ shash.get(c, 0)

            if c in thash and shash[c] == thash[c]:
                have+=1
            while have == need:
                if (r-l+1)<reslen:
                    res = [l,r]
                    reslen = r-l+1

                shash[s[l]] -=1
                if s[l] in thash and shash[s[l]]<thash[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if reslen !=float("infinity") else ""


            
            
