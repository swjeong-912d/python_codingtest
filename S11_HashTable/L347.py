import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        heap = []
        ans = []
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter.update({n: 1})
        for key in counter.keys():
            heapq.heappush(heap, (-counter[key], key))
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans


def print_test():
    leet_sol = Solution()
    print(leet_sol.topKFrequent([1, 2, 3, 4, 2, 2, 2, 3], 1))
