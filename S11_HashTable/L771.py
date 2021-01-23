from collections import defaultdict


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        isjewels = defaultdict(bool)
        for jewel in jewels:
            isjewels[jewel] = True
        count = 0
        for stone in stones:
            if isjewels[stone]:
                count += 1
        return count


def print_test():
    leet_sol = Solution()
    print(leet_sol.numJewelsInStones('aA', 'aAAbbbbbbbbbbdfsgregfdbcvbb'))
