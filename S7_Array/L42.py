from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        def fill(a,b):
            sub_rain = 0
            max_h = min(height[a],height[b])
            for j in range(a+1,b):
                sub_rain += max_h-height[j]
            return sub_rain
        def fill_left(b):
            if b == 0:
                return 0
            c = max(range(b),key = lambda k:height[k])
            return fill(c,b) + fill_left(c)
        def fill_right(b):
            if b == len(height)-1:
                return 0
            c = max(range(b+1,len(height)),key = lambda k:height[k])
            return fill(b,c) + fill_right(c)
        if len(height) == 0:
            return 0
        max_h = max(range(len(height)),key = lambda k:height[k])
        return fill_left(max_h)+fill_right(max_h)

def print_test():
    leet_sol = Solution()
    print(leet_sol.trap([]))







