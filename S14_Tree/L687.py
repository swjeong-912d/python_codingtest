# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node, value):
            if not node:
                return 0
            else:
                L = dfs(node.left, node.val)
                R = dfs(node.right, node.val)
                self.ans = max(self.ans, L + R)
                if node.val == value:
                    return max(L, R) + 1
                else:
                    return 0

        self.ans = 0
        dfs(root, -1)
        return self.ans


def print_test():
    leet_sol = Solution
