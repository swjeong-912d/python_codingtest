from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bsearch(nums, low, high, target):
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    return mid
            return -high

        high = len(numbers) - 1
        for (low, num) in enumerate(numbers):
            if num + numbers[high] >= target:
                high = bsearch(numbers, low + 1, high, target - num)
            else:
                continue
            if high > 0:
                return [low + 1, high + 1]
            else:
                high *= -1


def print_test():
    leet_sol = Solution()
    print(leet_sol.twoSum([4, 5, 6, 7, 11], 18))
