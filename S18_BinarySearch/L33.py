from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        pivot = low
        if target < nums[0]:
            low, high = pivot + 1, len(nums) - 1
        elif target > nums[0]:
            if pivot == 0:
                low, high = 0, len(nums) - 1
            else:
                low, high = 0, pivot
        else:
            return 0
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return -1


def print_test():
    leet_sol = Solution()
    print(leet_sol.search([4, 5, 6, 7, 1, 2, 3], 3))
