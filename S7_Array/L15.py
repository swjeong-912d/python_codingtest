from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        threesum_list = []
        for (i,num) in enumerate(nums):
            if i > 1 and nums[i-1] == nums[i]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[l]+nums[r]+num > 0:
                    r -= 1
                    while nums[r] == nums[r+1] and r > l:
                        r -= 1
                elif nums[l]+nums[r]+num < 0:
                    l += 1
                    while nums[l] == nums[l-1] :
                        l += 1
                else:
                    threesum_list.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    r -= 1
                    while nums[r] == nums[r+1] and r > l:
                        r -= 1
        return threesum_list

def print_test():
    leet_sol = Solution()
    print(leet_sol.threeSum([-1,0,1,0]))




