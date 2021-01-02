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
            left_total = 0
            while b > 0:
                c = max(range(b),key = lambda k:height[k])
                left_total += fill(c,b)
                b = c
            return left_total
        def fill_right(b):
            right_total = 0
            while b < len(height)-1:
                c = max(range(b+1,len(height)),key = lambda k:height[k])
                right_total += fill(b,c)
                b = c
            return right_total
        if len(height) == 0:
            return 0
        max_h = max(range(len(height)),key = lambda k:height[k])
        return fill_left(max_h)+fill_right(max_h)

def print_test():
    leet_sol = Solution()
    print(leet_sol.trap([5, 1, 2, 3, 5]))







