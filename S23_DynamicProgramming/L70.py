class Solution:
    def climbStairs(self, n: int) -> int:
        F = [0, 1]
        for i in range(1, n + 1):
            ans = F[0] + F[1]
            F[0], F[1] = F[1], ans
        return F[1]
