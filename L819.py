from typing import List
import collections
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub('[^a-z]', ' ', paragraph.lower())
        word_freqs = collections.Counter(paragraph.split())
        for word in banned:
            if word in word_freqs.keys():
                word_freqs[word] = 0
        item = word_freqs.most_common(1)
        return item[0][0]
def print_test():
    leet_sol = Solution()
    print(leet_sol.mostCommonWord("Bob hit a ball, the   hit BALL flew far after it was hit.",["hit"]))
