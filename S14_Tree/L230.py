# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        node = root
        while (True):
            if node:
                stack.append(node)
                node = node.left
            elif not stack:
                break
            else:
                node = stack.pop()
                k -= 1
                if k == 0:
                    return node.val
                node = node.right

def print_test():
    leet_sol = Solution