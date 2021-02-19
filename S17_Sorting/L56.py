from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        for interval in intervals:
            if result and result[-1][1] >= interval[0]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result


def print_test():
    leet_sol = Solution()
    print(leet_sol.merge([[1, 3], [2, 6], [4, 9], [11, 17], [15, 18], [8, 10]]))
