class Solution:
    def fib(self, n: int) -> int:
        F = [0, 1]
        for i in range(2, n + 1):
            ans = F[0] + F[1]
            F[0] = F[1]
            F[1] = ans
        if n == 0:
            return F[0]
        else:
            return F[1]
