# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def buildTree_post(start,end):
            if start < end:
                node = TreeNode(postorder[self.ind])
                self.ind -= 1
                mid = inorder.index(node.val,start,end)
                node.right = buildTree_post(mid+1,end)
                node.left = buildTree_post(start,mid)
                return node
            else:
                return None
        self.ind = len(postorder)-1
        return buildTree_post(0,len(postorder))

def print_test():
    leet_sol = Solution()
    leet_sol.buildTree([9,3,15,20,7], [9,15,7,20,3])