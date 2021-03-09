from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -10 ** 5 - 1
        sum = 0
        for n in nums:
            sum = max(n, sum + n)
            ans = max(ans, sum)
        return ans


def print_test():
    leet_sol = Solution()
    print(leet_sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
