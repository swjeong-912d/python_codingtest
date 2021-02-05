# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return 0
            L = dfs(node.left)
            R = dfs(node.right)
            if L != -1 and R != -1 and abs(L - R) <= 1:
                return max(L, R) + 1
            else:
                return -1
        if not root:
            return True
        else:
            return dfs(root) != -1
