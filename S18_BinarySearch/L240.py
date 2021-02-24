from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bsearch(nums, low, high, i, isRow):
            while low <= high:
                mid = (low + high) // 2
                if isRow:
                    midval = nums[mid][i]
                else:
                    midval = nums[i][mid]
                if midval > target:
                    high = mid - 1
                elif midval < target:
                    low = mid + 1
                else:
                    return mid
            return -low - 1

        m = len(matrix)
        n = len(matrix[0])
        if m == 1 and n == 1:
            return matrix[0][0] == target
        col = bsearch(matrix, 0, n - 1, 0, False)
        if col >= 0:
            return True
        else:
            for i in range(-col - 1):
                j = bsearch(matrix, 1, m - 1, i, True)
                if j > 0:
                    return True
            return False
