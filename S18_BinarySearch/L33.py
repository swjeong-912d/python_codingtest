from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] > nums[-1]:
            low, high = 1, len(nums) - 1
            tar2 = nums[0]
            pivot = 0
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > tar2:
                    if nums[mid + 1] <= tar2:
                        pivot = mid
                        break
                    else:
                        low = mid + 1
                elif nums[mid] < tar2:
                    if nums[mid - 1] >= tar2:
                        pivot = mid - 1
                        break
                    else:
                        high = mid - 1
            if target < nums[0]:
                low, high = pivot + 1, len(nums) - 1
            elif target > nums[0]:
                low, high = 0, pivot
            else:
                return 0
        else:
            low, high = 0, len(nums) - 1
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
    print(leet_sol.search([1, 2, 3, 4, 5, 6, 7], 3))
