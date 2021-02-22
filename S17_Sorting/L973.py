import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return heapq.nlargest(K, points, key=lambda x: -x[0] ** 2 - x[1] ** 2)


def print_test():
    leet_sol = Solution()
    print(leet_sol.kClosest([[1, 3], [-2, 2]], 1))
