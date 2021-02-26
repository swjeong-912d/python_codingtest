import collections
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = collections.defaultdict(int)
        for t in time:
            dic[t % 60] += 1
        ans = 0
        for j in range(31):
            if j == 0 or j == 30:
                ans += dic[j] * (dic[j] - 1) // 2
            else:
                ans += dic[j] * dic[60 - j]
        return ans
