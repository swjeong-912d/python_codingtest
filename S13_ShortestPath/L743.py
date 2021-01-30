import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        path = [float('inf')] * (n + 1)
        path[k] = 0
        edges = defaultdict(list)
        for e in times:
            edges[e[0]].append(e[1:])
        pque = []
        heapq.heappush(pque, (path[k], k))
        while len(pque) > 0:
            u = heapq.heappop(pque)[1]
            for v, w in edges[u]:
                if path[u] + w < path[v]:
                    path[v] = path[u] + w
                    heapq.heappush(pque, (path[v], v))
        if max(path[1:]) == float('inf'):
            return -1
        else:
            return max(path[1:])


def print_test():
    leet_sol = Solution()
    print(leet_sol.networkDelayTime([[1, 2, 1], [2, 1, 3]], 2, 2))
