from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target_number, combs, i):
            if target_number == 0:
                results.append(combs)
            elif target_number > 0:
                for (j, c) in enumerate(candidates):
                    if j >= i:
                        dfs(target_number - c, combs + [c], j)

        candidates.sort()
        results = []
        dfs(target, [], 0)
        return results


def print_test():
    leet_sol = Solution()
    print(leet_sol.combinationSum([3, 2, 1], 2))
