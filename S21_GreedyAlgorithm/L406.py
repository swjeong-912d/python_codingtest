from typing import List




class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        order = [[-1,-1]]*len(people)
        people.sort(key = lambda x: x[0]*2001+x[1])
        for p in people:
            count = 0000
            for (i,o) in enumerate(order):
                if count == p[1] and o == [-1,-1]:
                    order[i] = p
                    break
                if o == [-1,-1] or o[0] == p[0]:
                    count += 1
        return order
def print_test():
    leet_sol = Solution()
    print(leet_sol.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))