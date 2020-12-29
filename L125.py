# L125. valid palindrom
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z\d]','',s)
        return s == s[::-1]
def print_test():
    leet_sol = Solution()
    print(leet_sol.isPalindrome(""))
    print(leet_sol.isPalindrome("12321"))
    print(leet_sol.isPalindrome("12 3 2 1"))
    print(leet_sol.isPalindrome("512 3 2 :1 5"))
    print(leet_sol.isPalindrome("as dfaf :dsfa"))
    print(leet_sol.isPalindrome("a sd fafDs:a"))
    print(leet_sol.isPalindrome("a@$@#%#@%#@ sd F___afDs:a"))
