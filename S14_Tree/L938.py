# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return
            elif node.val >= low and node.val <= high:
                self.result += node.val
            dfs(node.left)
            dfs(node.right)

        self.result = 0
        dfs(root)
        return self.result
