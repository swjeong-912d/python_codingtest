from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cnt = 0
        while g and s:
            while g and g[-1] > s[-1]:
                g.pop()
            if g:
                cnt += 1
                g.pop()
            s.pop()
        return cnt


def print_test():
    leet_sol = Solution()
    print(leet_sol.findContentChildren([1, 2, 3, 3, 5], [1, 2, 30, 2, 4]))
