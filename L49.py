from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = defaultdict(list)
        ga = [[]]
        dict_no = 0
        for str in strs:
            ss = "".join(sorted(str))
            if not ss in ana_dict.keys():
                ana_dict.update({ss:dict_no})
                dict_no += 1
            if len(ga) > ana_dict[ss]:
                ga[ana_dict[ss]].append(str)
            else:
                ga.append([str])
        return ga

def print_test():
    leet_sol = Solution()
    print(leet_sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(leet_sol.groupAnagrams([""]))
    print(leet_sol.groupAnagrams(["aa"]))

