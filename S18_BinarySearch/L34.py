from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        midl = 0
        start, end = 0, len(nums ) -1
        while start <= end:
            midl = (start +end )//2
            if nums[midl] == target:
                if midl == 0 or nums[midl -1] != target:
                    break
                else:
                    end = midl-1
            elif nums[midl] > target:
                end = midl-1
            elif nums[midl] < target:
                start = midl+1


        start, end = 0, len(nums) -1
        while start <= end:
            midr = (start +end )//2
            if nums[midr] == target:
                if midr == len(nums ) -1 or nums[midr +1] != target:
                    break
                else:
                    start = midr+1
            elif nums[midr] > target:
                end = midr-1
            elif nums[midr] < target:
                start = midr+1

        if not nums or nums[midl] != target and nums[midr] != target:
            return -1,-1
        return midl,midr

def print_test():
    leet_sol = Solution()
    print(leet_sol.searchRange([], 2))
