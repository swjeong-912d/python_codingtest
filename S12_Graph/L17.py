from typing import List


class Solution:
    def dfs(self, letters, letter, digits, result):
        if len(digits) == 0:
            result.append(letter)
        else:
            d = digits[0]
            digits.pop(0)
            for l in letters[int(d) - 2]:
                self.dfs(letters, ''.join((letter, l)), digits[:], result)

    def letterCombinations(self, digits: str) -> List[str]:
        letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = []
        self.dfs(letters, "", list(digits)[:], result)
        return result


def print_test():
    leet_sol = Solution()
    print(leet_sol.letterCombinations("23"))
