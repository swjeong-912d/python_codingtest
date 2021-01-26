from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(subset, numbers):
            if len(numbers) == 0:
                result.append(subset)
            else:
                dfs(subset + [], numbers[:-1])
                dfs(subset + [numbers[-1]], numbers[:-1])

        result = []
        dfs([], nums)
        return result


def print_test():
    leet_sol = Solution()
    print(leet_sol.subsets([1, 2, 3]))
