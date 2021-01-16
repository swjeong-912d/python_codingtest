import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        dic = collections.defaultdict(lambda:False)
        for ss in reversed(s):
           if dic[ss] == False:
               stack.append(ss)
               dic[ss] = True
           elif stack[-1] > ss:
               for (i,elm) in enumerate(stack):
                   if elm == ss:
                       stack.pop(i)
                       stack.append(ss)
                       break
        return ''.join(stack[::-1])

def print_test():
    leet_sol = Solution()
    print(leet_sol.removeDuplicateLetters("bcabc"))
