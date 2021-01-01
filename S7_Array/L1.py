
from typing import List
from bisect import bisect_left
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_inds = sorted(range(len(nums)),key = lambda k : nums[k])
        snums = []
        for i in range(len(nums)):
            snums.append(nums[sorted_inds[i]])
        t = len(nums)
        for (s, sval) in enumerate(snums):
            b = target-sval
            t = bisect_left(snums, b, s+1, t)
            if t < len(nums) and snums[t]+sval == target:
                return [sorted_inds[s],sorted_inds[t]]


def print_test():
    leet_sol = Solution()
    print(leet_sol.twoSum([1,9,3,4,5,7,11],13))

