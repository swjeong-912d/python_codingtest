from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        cum_gas = 0
        index = -1
        for i in range(len(gas)):
            cum_gas += gas[i] - cost[i]
            if cum_gas < 0:
                index = -1
                cum_gas = 0
            elif index == -1:
                index = i
        return index


def print_test():
    leet_sol = Solution()
    print(leet_sol.canCompleteCircuit([1, 2, 3, 4, 3, 2, 4, 1, 5, 3, 2, 4], [1, 1, 1, 3, 2, 4, 3, 6, 7, 4, 3, 1]))
