from typing import List
import re


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            log_key = log.split()[1]
            if log_key.isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        letter_logs.sort(key = lambda x : (x.split()[1:], x.split()[:1]))
        return letter_logs+digit_logs

def print_test():
    leet_sol = Solution()
    print(leet_sol.reorderLogFiles( ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
