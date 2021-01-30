import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        edges = defaultdict(list)
        for u, v, w in flights:
            edges[u].append((v, w))
        Q = []
        heapq.heappush(Q, [0, 0, src])
        while len(Q):
            p, t, u = heapq.heappop(Q)
            if u == dst and t <= K + 1:
                return p
            if t <= K:
                for v, w in edges[u]:
                    heapq.heappush(Q, [p + w, t + 1, v])
        return -1


def print_test():
    leet_sol = Solution()
    print(
        leet_sol.findCheapestPrice(6, [[0, 1, 6], [0, 2, 3], [0, 3, 1], [3, 4, 1], [2, 1, 2], [4, 1, 1], [1, 5, 1]], 0,
                                   5, 3))
