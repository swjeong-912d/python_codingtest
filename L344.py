from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s = s[::-1]
        return s
        """
        Do not return anything, modify s in-place instead.
        """
def print_test():
    leet_sol = Solution()
    print(leet_sol.reverseString(list("I am a boy")))
