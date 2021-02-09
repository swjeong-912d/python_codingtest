from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        mid = int(len(nums) / 2)
        stack = []
        left = 0
        right = len(nums) - 1
        visited = [False] * len(nums)
        root = TreeNode(nums[mid])
        visited[mid] = True
        stack.append((root, mid, left, right))
        while len(stack) > 0:
            node, mid, left, right = stack.pop()
            lmid = int((left + mid - 1) / 2)
            if not visited[lmid]:
                visited[lmid] = True
                node.left = TreeNode(nums[lmid])
                stack.append((node.left, lmid, left, mid - 1))
            rmid = int((mid + 1 + right) / 2)
            if not visited[rmid]:
                visited[rmid] = True
                node.right = TreeNode(nums[rmid])
                stack.append((node.right, rmid, mid + 1, right))
        return root


def print_test():
    leet_sol = Solution()
    leet_sol.sortedArrayToBST([-10, -3, 0, 5, 9])
