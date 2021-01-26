from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(num, fnums):
            if len(fnums) == 0:
                results.append(num)
            else:
                for (i, n) in enumerate(fnums):
                    dfs(num + [n], fnums[:i] + fnums[i + 1:])

        results = []
        dfs([], nums)
        return results


def print_test():
    leet_sol = Solution()
    print(leet_sol.permute([1, 2, 3]))
