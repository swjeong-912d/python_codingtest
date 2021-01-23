class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_ind = -1
        start_ind = 0
        best_len = 0
        dict = {}
        for (i, ss) in enumerate(s):
            if ss in dict:
                best_len = max(best_len, last_ind - start_ind + 1)
                start_ind = max(start_ind, dict[ss] + 1)
            dict.update({ss: i})
            last_ind = i
        return max(best_len, last_ind - start_ind + 1)


def print_test():
    leetsol = Solution()
    print(leetsol.lengthOfLongestSubstring('abba'))
