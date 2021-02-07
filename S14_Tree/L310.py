from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        emap = defaultdict(list)
        for edge in edges:
            emap[edge[0]].append(edge[1])
            emap[edge[1]].append(edge[0])
        node_list = list(range(n))
        while len(node_list) > 2:
            leaf = []
            for i in range(n):
                if len(emap[i]) == 1:
                    leaf.append(i)
            for i in leaf:
                j = emap[i][0]
                emap[j].pop(emap[j].index(i))
                emap[i] = []
                node_list.pop(node_list.index(i))
        return node_list


def print_test():
    leet_sol = Solution()
    print(leet_sol.findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
