class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        comp_list = set()
        t_list = []
        if len(s) != len(t):
            return False
        for j in t:
            t_list.append(j)
        for i in s:
            if i not in t_list:
                return False
            else:
                t_list.remove(i)
        return True
             