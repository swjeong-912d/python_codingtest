from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(reg_crs, registered):
            if registered[reg_crs]:
                Possible[0] = False
            elif not checked[reg_crs] and Possible[0]:
                checked[reg_crs] = True
                reg2 = registered[:]
                reg2[reg_crs] = True
                if reg_crs in dic.keys():
                    for c in dic[reg_crs]:
                        dfs(c, reg2)

        dic = {}
        for p in prerequisites:
            if p[0] in dic.keys():
                dic[p[0]].append(p[1])
            else:
                dic[p[0]] = [p[1]]
        checked = [False] * numCourses
        req = [False] * numCourses
        Possible = [True]
        for c in range(numCourses):
            if not checked[c]:
                dfs(c, req)
            if not Possible[0]:
                return False
        return True


def print_test():
    leet_sol = Solution()
    print(leet_sol.canFinish(2, [[0, 1]]))
