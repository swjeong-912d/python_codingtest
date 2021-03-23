class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        F = [nums[0], nums[1], nums[2] + nums[0]]
        ans = max(F)
        for i in range(3, len(nums)):
            tmp = nums[i] + max(F[0], F[1])
            ans = max(ans, tmp)
            F[0], F[1], F[2] = F[1], F[2], tmp
        return ans
