import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        result = []
        for (i, n) in enumerate(nums):
            if i < k - 1:
                heapq.heappush(window, (-n, i))
            else:
                heapq.heappush(window, (-n, i))
                while window[0][1] <= i - k:
                    heapq.heappop(window)
                result.append(-window[0][0])
        return result


def print_test():
    leet_sol = Solution()
    print(leet_sol.maxSlidingWindow([5, 4, 3, 2, 1], 2))
