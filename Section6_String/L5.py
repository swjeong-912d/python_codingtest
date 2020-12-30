import re
from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_s = ""
        ls = s.lower()
        for i in range(len(s)):
            for eo in range(2):
                st = i - 1
                if eo == 1:
                    et = i+1
                else:
                    et = i
                while st >= 0 and et < len(s):
                    if ls[st] == ls[et]:
                        st -= 1
                        et += 1
                    else:
                        if len(ls[st+1:et]) > len(max_s):
                            max_s = s[st+1:et]
                        break
                if len(ls[st + 1:et]) > len(max_s):
                    max_s = s[st + 1:et]
        return max_s

def print_test():
    leet_sol = Solution()
    print(leet_sol.longestPalindrome("aaaaacaabaacaaaaa"))

