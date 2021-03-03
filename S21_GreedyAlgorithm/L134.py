from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        for i in range(len(gas)):
            if gas[i - 1] - cost[i - 1] < 0 and gas[i] - cost[i] >= 0:
                start = i
                break
        cum_gas = 0
        index = -1
        n = len(gas)
        for i in range(n):
            cum_gas += gas[(start + i) % n] - cost[(start + i) % n]
            if cum_gas < 0:
                index = -1
                cum_gas = 0
            elif index == -1:
                index = (i + start) % n
        cum_gas = 0
        for i in range(n):
            cum_gas += gas[(index + i) % n] - cost[(index + i) % n]
            if cum_gas < 0:
                return -1
        return index


def print_test():
    leet_sol = Solution()
    print(leet_sol.canCompleteCircuit([1, 2, 3, 4, 3, 2, 4, 1, 5, 3, 2, 4], [1, 1, 1, 3, 2, 4, 3, 6, 7, 4, 3, 1]))
