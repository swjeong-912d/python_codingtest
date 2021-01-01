from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = defaultdict(list)
        for str in strs:
            ana_dict["".join(sorted(str))].append(str)
        return ana_dict.values()
def print_test():
    leet_sol = Solution()
    print(leet_sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(leet_sol.groupAnagrams([""]))
    print(leet_sol.groupAnagrams(["aa"]))

