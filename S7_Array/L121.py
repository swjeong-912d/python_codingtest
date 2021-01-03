from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diffs = []
        for (pi,price) in enumerate(prices[1:]):
            diffs.append(price-prices[pi])
        current_sum = 0
        best_sum = 0
        for d in diffs:
           current_sum = max(0,d+current_sum)
           best_sum = max(best_sum,current_sum)
        return best_sum

def print_test():
    leet_sol = Solution()
    print(leet_sol.maxProfit([6, 2, 6, 5, 6, 5, 7]))
