from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(routes, tickets2):
            if len(shortest_routes) > 0:
                return
            elif len(tickets2) == 0:
                shortest_routes.append(routes)
            else:
                for (i, ticket) in enumerate(tickets2):
                    if routes[-1] == ticket[0]:
                        dfs(routes + [ticket[1]], tickets2[:i] + tickets2[i + 1:])

        shortest_routes = []
        tickets.sort(key=lambda x: ''.join(x))
        for (i, ticket) in enumerate(tickets):
            if ticket[0] == "JFK" and len(shortest_routes) == 0:
                dfs(tickets[i], tickets[:i] + tickets[i + 1:])
        return shortest_routes


def print_test():
    leet_sol = Solution()
    print(leet_sol.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
