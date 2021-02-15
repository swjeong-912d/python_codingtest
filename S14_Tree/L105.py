# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def buildTree_pre(node,start,end):
            if start < end:
                node = TreeNode(preorder[self.ind])
                self.ind += 1
                mid = inorder.index(node.val,start,end)
                node.left = buildTree_pre(node.left,start,mid)
                node.right = buildTree_pre(node.right,mid+1,end)
                return node
            else:
                return None
        self.ind = 0
        return buildTree_pre(None,0,len(preorder))

def print_test():
    leet_sol = Solution()
    leet_sol.buildTree([3,9,20,15,7], [9,3,15,20,7])