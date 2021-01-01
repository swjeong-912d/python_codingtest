import re
from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        pal_list = []
        for i in range(len(s)):
            pal_list.append(expand(i,i+1))
            pal_list.append(expand(i,i+2))
        return max(pal_list,key=len)

def print_test():
    leet_sol = Solution()
    print(leet_sol.longestPalindrome("aaaaaabaacaaaaa"))

