from typing import List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_freqs = {}
        for word in paragraph.split():
            word = re.sub('[^a-z]','',word.lower())
            if word in word_freqs.keys():
                word_freqs[word] += 1
            else:
                word_freqs[word] = 1
        for word in banned:
            word_freqs[word] = 0
        best = max(word_freqs.values())
        for word, key in word_freqs.items():
            if key == best:
                return word


def print_test():
    leet_sol = Solution()
    print(leet_sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))
