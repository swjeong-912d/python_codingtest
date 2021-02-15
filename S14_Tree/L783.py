# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = pow(10, 5)
    last = -1

    def minDiffInBST(self, root: TreeNode) -> int:
        if root:
            self.minDiffInBST(root.right)
            if self.last > 0:
                self.result = min(self.result, abs(root.val - self.last))
            self.last = root.val
            self.minDiffInBST(root.left)
        return self.result
