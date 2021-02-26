import collections


class Solution:
    def remove(self, deq, dircetion, dic, count):
        if dircetion == 'l':
            while not (deq[0] in dic and dic[deq[0]] == count[deq[0]]):
                if deq[0] in dic:
                    dic[deq[0]] -= 1
                deq.popleft()
        elif dircetion == 'r':
            while not (deq[-1] in dic and dic[deq[-1]] == count[deq[-1]]):
                if deq[-1] in dic:
                    dic[deq[-1]] -= 1
                deq.pop()
        return deq

    def minWindow(self, s: str, t: str) -> str:

        dic = {}
        count = {}
        nt = 0
        for str in set(t):
            dic[str] = 0
        for str in t:
            if str in count:
                count[str] += 1
            else:
                count[str] = 1
        tmp = collections.deque()
        ans = s + t
        is_first = True
        for str in s:
            if not (tmp or str in dic):
                continue
            tmp.append(str)
            if str in dic:
                dic[str] += 1
                if dic[str] <= count[str]:
                    nt += 1
            if tmp[0] == tmp[-1] and nt == len(t) and dic[tmp[0]] > count[tmp[0]]:
                if is_first:
                    tmp2 = self.remove(tmp.copy(), 'r', dic.copy(), count)
                    print(id(tmp2), id(tmp))
                    if len(ans) > len(tmp2):
                        ans = ''.join(tmp2)
                    is_first = False
                tmp = self.remove(tmp, 'l', dic, count)
                if len(ans) > len(tmp):
                    ans = ''.join(tmp)
        if nt < len(t):
            return ''
        else:
            tmp = self.remove(tmp, 'l', dic, count)
            tmp = self.remove(tmp, 'r', dic, count)
            if len(ans) > len(tmp):
                ans = ''.join(tmp)
            return ans


# ADBDBCBBAC
# A AD ADB ADBDB ADBDBC ADBDBCB ADBDBCBB CBBA BAC


def print_test():
    leet_sol = Solution()
    print(leet_sol.minWindow('ADOBECODEBANC', 'ABC'))

# ABABC
# A AB BA AB ABC
#
# ABABA
#
