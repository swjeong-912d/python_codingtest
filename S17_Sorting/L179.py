from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comp(a, b):
            A = str(a) + str(b)
            B = str(b) + str(a)
            return A > B

        def merge(A, B):
            a = 0
            b = 0
            C = []
            while a < len(A) and b < len(B):
                if comp(A[a], B[b]):
                    C.append(A[a])
                    a += 1
                else:
                    C.append(B[b])
                    b += 1
            while a < len(A):
                C.append(A[a])
                a += 1
            while b < len(B):
                C.append(B[b])
                b += 1
            return C

        def mergeSort(nums):
            if len(nums) > 1:
                mid = len(nums) // 2
                a = mergeSort(nums[:mid])
                b = mergeSort(nums[mid:])
                return merge(a, b)
            else:
                return nums

        ans = ''
        nums = mergeSort(nums)
        while len(nums) > 1 and nums[0] == 0:
            nums = nums[1:]
        for num in nums:
            ans += str(num)
        return ans


def print_test():
    leet_sol = Solution()
    print(leet_sol.largestNumber([3, 30, 34, 5, 9]))
