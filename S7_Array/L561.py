from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        for (i,num) in enumerate(nums):
            if i%2 == 0:
                sum+=num
        return sum

def print_test():
    leet_sol = Solution()
    print(leet_sol.arrayPairSum([6,2,6,5,1,2]))
