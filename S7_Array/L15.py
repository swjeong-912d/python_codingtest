from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        threesum_list = []
        for (m,num) in enumerate(nums):
            if m == 0 or (m > 1 and nums[m-2] == nums[m]):
                continue
            if nums[m-1] != nums[m]:
                l = 0
            else:
                l = m-1
            r = len(nums)-1
            while l < m and r > m:
                if nums[l]+nums[r]+num > 0:
                    r -= 1
                    while nums[r] == nums[r+1] and r > m:
                        r -= 1
                elif nums[l]+nums[r]+num < 0:
                    l += 1
                    while nums[l] == nums[l-1] and l < m:
                        l += 1
                else:
                    threesum_list.append([nums[l],nums[m],nums[r]])
                    r -= 1
                    while nums[r] == nums[r + 1] and r > m:
                        r -= 1
        return threesum_list

def print_test():
    leet_sol = Solution()
    print(leet_sol.threeSum([-1,0,1,0]))




