import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


def print_test():
    leet_sol = Solution()
    print(leet_sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
