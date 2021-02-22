import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = {c: i for i, c in enumerate(s)}
        contain = collections.defaultdict(bool)
        output = []
        for i, c in enumerate(s):
            if not contain[c]:
                while output and output[-1] > c and dic[output[-1]] > i:
                    contain[output[-1]] = False
                    output.pop()
                output.append(c)
                contain[c] = True
        return ''.join(output)

def print_test():
    leet_sol = Solution()
    print(leet_sol.removeDuplicateLetters("bcabcd"))
