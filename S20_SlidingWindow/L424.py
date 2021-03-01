import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        counter = collections.Counter()
        for (right) in range(1, len(s) + 1):
            counter[s[right - 1]] += 1
            mode_len = counter.most_common(1)[0][1]
            if mode_len + k < right - left:
                counter[s[left]] -= 1
                left += 1
        return right - left


def print_test():
    leet_sol = Solution()
    print(leet_sol.characterReplacement('BAAB', 2))
