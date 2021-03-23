from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def compute(l, op, r):
            result = []
            for n1 in l:
                for n2 in r:
                    if op == '-':
                        result.append(int(n1) - int(n2))
                    elif op == '*':
                        result.append(int(n1) * int(n2))
                    elif op == '+':
                        result.append(int(n1) + int(n2))
            return result

        ans = []
        for (i, s) in enumerate(input):
            if s in '-*+':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                ans += compute(left, s, right)
        if not ans:
            return [int(input)]
        return ans


def print_test():
    leet_sol = Solution()
    print(leet_sol.diffWaysToCompute("11"))
