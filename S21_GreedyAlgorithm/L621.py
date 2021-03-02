import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        active = []
        sleep = []
        total = {}
        for t in tasks:
            if t in total.keys():
                total[t] += 1
            else:
                total[t] = 1
        for t in set(tasks):
            heapq.heappush(active, [-total[t], t])
        time = 0
        while len(sleep) + len(active) > 0:
            time += 1
            if len(active) > 0:
                task = heapq.heappop(active)
                task[0] += 1
                if task[0] < 0:
                    heapq.heappush(sleep, (time, task))
            while len(sleep) > 0 and time - sleep[0][0] >= n:
                heapq.heappush(active, heapq.heappop(sleep)[1])
        return time


def print_test():
    leet_sol = Solution()
    print(leet_sol.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))
