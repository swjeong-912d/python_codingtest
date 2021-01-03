from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cum_arr = []
        cum_r_arr = []
        for i in range(len(nums)):
            if i == 0:
                cum_arr.append(1)
                cum_r_arr.append(1)
            else:
                cum_arr.append(cum_arr[i-1]*nums[i-1])
                cum_r_arr.append(cum_r_arr[i-1]*nums[len(nums)-i])
        cum_r_arr = cum_r_arr[::-1]
        output = []
        for i in range(len(nums)):
            output.append(cum_arr[i]*cum_r_arr[i])
        return output

def print_test():
    leet_sol = Solution()
    print(leet_sol.productExceptSelf([6, 2, 6, 5, 1, 2]))
