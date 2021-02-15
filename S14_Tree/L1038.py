# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def search(node):
            if not node:
                data_list.append(node.val)
                search(node.left)
                search(node.right)
        def replace(node):
            if not node:
                node.val = dic[node.val]
                replace(node.left)
                replace(node.right)
        data_list = []
        search(root)
        data_list.sort()
        sum = 0
        dic = {}
        for d in reversed(data_list):
            dic[d] = sum
            sum += d
        replace(root)
        return root