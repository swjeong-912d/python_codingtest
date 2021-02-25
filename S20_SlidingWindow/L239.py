import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        result = []
        for (i, n) in enumerate(nums):
            if dq and dq[0] == i - k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result

def print_test():
    leet_sol = Solution()
    print(leet_sol.maxSlidingWindow([5, 4, 3, 2, 1], 2))
