from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cum_arr = []
        cum_prod = 1
        for i in range(len(nums)):
            cum_arr.append(cum_prod)
            cum_prod *= nums[i]
        reverse_cumprod = 1
        for i in reversed(range(len(nums))):
            cum_arr[i] *= reverse_cumprod
            reverse_cumprod *= nums[i]
        return cum_arr
def print_test():
    leet_sol = Solution()
    print(leet_sol.productExceptSelf([6, 2, 6, 5, 1, 2]))
