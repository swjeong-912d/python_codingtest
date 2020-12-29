from typing import List
import re


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for i in range(len(logs)):
            log_ind = logs[i].find(' ')
            log_id = logs[i][:log_ind]
            log_item = logs[i][(log_ind+1):]
            t = re.findall("[0-9]",log_item)
            if len(t) == 0:
                letter_logs.append(log_item + " " + log_id)
            else:
                digit_logs.append(logs[i])
        letter_logs.sort()
        for i in range(len(letter_logs)):
            letter_ind = letter_logs[i].rfind(' ')
            letter_logs[i] = letter_logs[i][letter_ind+1:]+" "+letter_logs[i][:letter_ind]
        return letter_logs+digit_logs

def print_test():
    leet_sol = Solution()
    print(leet_sol.reorderLogFiles( ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
