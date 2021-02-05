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
                return (0, True)
            L = dfs(node.left)
            R = dfs(node.right)
            if L[1] and R[1] and abs(L[0] - R[0]) <= 1:
                return (max(L[0], R[0]) + 1, True)
            else:
                return (max(L[0], R[0]) + 1, False)

        if not root:
            return True
        else:
            return dfs(root)[1]
