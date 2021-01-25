from typing import List


class Solution:
    def visit_land(self, grid: List[List[str]], i, j):
        if i < 0 or i >= len(grid):
            return
        if j < 0 or j >= len(grid[i]):
            return
        if grid[i][j] == "1":
            grid[i][j] = "2"
            self.visit_land(grid, i - 1, j)
            self.visit_land(grid, i + 1, j)
            self.visit_land(grid, i, j - 1)
            self.visit_land(grid, i, j + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        num_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    num_island += 1
                    self.visit_land(grid, i, j)
        return num_island


def print_test():
    leet_sol = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(leet_sol.numIslands(grid))
