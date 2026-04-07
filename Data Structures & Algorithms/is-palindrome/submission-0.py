class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for i in s:
            if i.isdigit():
                st+=i
            if i.isalpha():
                st+=i

        print(st, s)

        return st[::-1].lower() == st.lower()
        